import subprocess
import google.generativeai as palm
import os
from dotenv import load_dotenv

load_dotenv()

palm.configure(api_key=os.getenv('PALM2_API_KEY'))
model = 'models/text-bison-001'



def passes(file_name, argus):
    """
    Assumes file name passed is without .py suffix and it is the same as function name
    args is the test case to be tested, passed in a list form
    file resides in testcases directory, which i turned into a package
    """
    code = f'''
from testcases.{file_name} import {file_name}

{file_name}({", ".join(str(x) for x in argus)})

'''
    result = subprocess.run(['python', '-c', code], stdout=subprocess.PIPE, text=True)
    return result.returncode



global_prompt = """
{variable_prompt}

Buggy Code:
def foo(a, b):
    '''
    The function returns the addition of two integers
    '''
    return a-b

def foo(a, b):
    '''
    The function returns the addition of two integers
    '''
    return a+b

-----------------------------------------------------------------
Buggy Code:
def bar(x):
    '''
    The function doubles each element of the list
    '''
    for i in range(x):
        x[i] *= 2
    
    return x


def bar(x):
    '''
    The function doubles each element of the list
    '''
    for i in range(x):
        x[i] = 2
    
    return x

-----------------------------------------------------------------
Code: {variable_code}
"""



def palm_completion(prompt):
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0.8,
        max_output_tokens=800,
    )
    return completion.result



default_prompt = '''
The following is a buggy code. Please understand what the code does from the doc string. Then output the correct code.
DO NOT OUTPUT ANY OTHER TEXT. ONLY OUTPUT THE CODE. USE PROPER INDENTATION. ONLY RETURN THE CORRECTED CODE. DO NOT RETURN 
'''

code = '''
def works(u, z):
    u += 2
    z /= u
    return 2*z + u
'''
# ex = global_prompt.format(variable_prompt=default_prompt, variable_code=code)
# output = palm_completion(ex)
# print(output)


# code = '\n'
# fp = 'testcases/buggy_6.py'
# with open(fp, 'r') as f:
#     code += f.read()

# code += "\n\n"
# fp2 = 'testcases/test_cases_6.py'
# with open(fp2, 'r') as g:
#     code += g.read()

# print(code)


def bugfix_fitness(prompt):
    file_name = 'buggy_'
    correct = 0

    for i in range(6, 11):
        fp = 'testcases/' + file_name + str(i) + '.py'
        with open(fp, 'r') as f:
            code = f.read()
        this_prompt = global_prompt.format(variable_prompt=prompt, variable_code=code)
        output = palm_completion(this_prompt)

        print("OUTPUT:\n", output)

        ex_code = output + "\n\n"
        fp2 = 'testcases/test_cases_' + str(i) + '.py'

        with open(fp2, 'r') as g:
            ex_code += g.read()

        print("COMPLETE ONE: \n\n\n\n")
        print(ex_code)
        
        
        result = subprocess.run(['python', '-c', ex_code], stdout=subprocess.PIPE, text=True)
        print("RESULT: ", result.returncode)
        print("\n\n\n\n")

        if result.returncode == 0:
            correct += 1
            print("yey")
        
    return correct

