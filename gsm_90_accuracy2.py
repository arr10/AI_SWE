import subprocess
import google.generativeai as palm
import os
from dotenv import load_dotenv
import json
import re

load_dotenv()

palm.configure(api_key=os.getenv('PALM2_API_KEY'))
model = 'models/text-bison-001'

answer_extraction_prompt = {
    "integer": "\n\n--------------------------------------\n\nReturn the answer in integer. Only the answer. No explanation. No extra words. Just one integer.",
    "float":   "\n\n--------------------------------------\n\nReturn the answer in floating point number. Only the answer. No explanation. No extra words. Just one number.",
    "multiple choice": "\n\n--------------------------------------\n\nReturn the answer in one of A, B, C, D, E. Only the answer. No explanation. No extra words. Just one letter."
}

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
ONLY OUTPUT THE CORRECT ANSWER. DO NOT RETURN ANY TEXT
{variable_question}
"""



def palm_completion(prompt):
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0.8,
        max_output_tokens=800,
    )
    return completion.result

def get_answer(question, template, answer_type):
    """
    question:   ... (str)
    template:   prompt template (str)
    answer_type:       The type of the answer that should be extracted. (str)
                Choose between "integer", "float" and "multiple choice"
                The answer extraction depends on this argiment. 
    """
    
    
    
    prompt = f"""
    Q: {question}
    A: {template}
    """

    solution = palm_completion(prompt)
    if not solution:
        return None
    # Extract answer
    prompt = prompt + solution + answer_extraction_prompt[answer_type]
    answer_text = palm_completion(prompt)

    if answer_type == "integer":
        result = re.search(r'\b\d+\b', answer_text)
        if result is None:
            return None
        return int(result.group(0))
    elif answer_type == "float":
        result = re.search(r'\b\d+\.\d+\b', answer_text)
        if result is None:
            return None
        return float(result.group(0))
    elif answer_type == "multiple choice":
        if answer_text is None:
            return None
        return answer_text.strip()
    

default_prompt = '''
Initiating with a deep understanding of the problem, formulate and execute a well-considered strategy.
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



def fitness(prompt):
    json_file_path = "datasets/gsm8k_90.json"
    correct = 0
    tnumber = 0

    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    
    gsm8k_samples = data["gsm8k"]

    for sample in gsm8k_samples:
        question = sample["question"]
        answer = sample["answer"]
        output = get_answer(question, default_prompt, 'integer')
        if answer == str(output):
            correct += 1
        tnumber += 1

        print("correct: ", correct)
        print(output, answer)
    

    return (correct/tnumber)*100



print(fitness(default_prompt))

# fitness_testcase_generation('correct_1', [[1,2]])