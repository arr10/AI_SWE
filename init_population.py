def get_initial_popularion(type='reasoning'):
    if type == 'reasoning':
        return reasoning_initial_population()
    elif type == 'testcase':
        return testcase_initial_population()
    elif type == 'bugfix':
        return bugfix_initial_population()


def reasoning_initial_population():
        return [
            "Let's think step by step.",
            'First,',
            "Let's think about this logically.",
            "Let's solve this problem by splitting it into steps.",
            "Let's be realistic and think step by step.", 
            "Let's think like a detective step by step.",
            'First, let’s think about it step by step.', 
            'Let’s use logical thinking to solve this problem step by step.', 
            'Logically speaking, we can solve this problem in the following steps.', 
            "Let's use step-by-step thinking", 
            "Let's break down the problem and tackle it one step at a time.",
            "To approach this systematically, let's consider each step individually.",
            'Let’s dissect this issue methodically, step by step.', 
            "Let's methodically work through each part of this problem.",
            "Step by step, let's analyze the components of this issue.", 
            'We can solve this by carefully addressing each aspect, one step at a time.',
            "To find a solution, let's sequentially examine every element of the problem.", 
            "Let's sequentially think through the steps to resolve this.",
            'By thinking in stages, we can methodically solve this problem.', 
            "Let's take a structured approach and address this step by step.",
            "Let's first understand the problem, extract relevant variables and their corresponding numerals, and devise a plan. Then, let's carry out the plan, calculate intermediate variables (pay attention to correct numeral calculation and commonsense), solve the problem step by step, and show the answer.", 
            "Let's first understand the problem and devise a plan to solve the problem. Then, let's carry out the plan to solve the problem step by step.", 
            "Let's devise a plan and solve the problem step by step.",
            "Let's first understand the problem, extract relevant variables and their corresponding numerals, and devise a complete plan. Then, let's carry out the plan, calculate intermediate variables (pay attention to correct numerical calculation and commonsense), solve the problem step by step, and show the answer.", 
            "Let's first understand the problem, extract relevant variables and their corresponding numerals, and make a complete plan. Then, let's carry out the plan, calculate intermediate variables (pay attention to correct numerical calculation and commonsense), solve the problem step by step, and show the answer."
            ]

def testcase_initial_population():
    return [
         "Given the following docstring, identify the primary purpose and functionality of the function. Then, create three distinct test cases that validate different aspects of this functionality in Python.",
         "Read the provided docstring and list all the parameters the function takes. For each parameter, create a test case in Python that specifically tests different values, including edge cases.",
         "Examine the docstring to understand the expected output of the function. Write two Python test cases that validate the function's output against expected results.",
         "Based on the function's docstring, identify potential errors or exceptions the function might encounter. Write Python test cases to ensure that the function handles these errors gracefully.",
         "From the docstring, determine the boundary conditions for this function. Create Python test cases to test these boundary conditions.",
         "Considering the function's description in the docstring, develop a Python test case that measures and evaluates the function's performance, especially under heavy load or large inputs.",
         "Generate Python test cases to check the compatibility of the function with different environments or Python versions, as inferred from the docstring.",
         "Create Python test cases that can be used for regression testing, ensuring that the new changes in the function do not break its existing functionality as described in the docstring.",
         "From the docstring, infer how this function interacts with other components. Write a Python test case that tests these interactions and integration points.",
         "Using the docstring, identify a real-world scenario where this function might be used. Write a Python test case that simulates this user scenario.",
         "Analyze the data types the function handles as per the docstring. Develop Python test cases to check the function's handling of different data types.",
         "If the function has default parameters as mentioned in the docstring, write Python test cases to test the function with and without these default values.",
         "Based on the docstring, create a Python test case that stress tests the function, pushing it to its operational limits.",
         "Construct a series of Python test cases that test the function in a sequence, each dependent on the outcome of the previous test, as guided by the docstring.",
         "Create Python test cases with randomized inputs to test the robustness of the function as described in the docstring.",
         "If applicable from the docstring, write Python test cases that assess the security aspects of the function, such as input validation and sanitization.",
         "Develop a Python test case to monitor and assess the resource utilization of the function (like memory and CPU usage), as suggested by the docstring.",
         "If the function is intended to be used in a concurrent environment as per the docstring, create Python test cases to test its behavior under concurrent execution.",
         "Create Python test cases focusing on input validation for the function, ensuring it handles invalid or unexpected inputs as described in the docstring.",
         "Construct a comprehensive Python test case that covers an end-to-end workflow involving the function, as per the use cases described in the docstring.",
         "Analyze the provided docstring to understand the comprehensive functionality of the function. Develop at least three Python test cases that collectively ensure the function performs as described, focusing on its key features and intended use.",
         "Examine the function's docstring and identify all input parameters. For each parameter, generate Python test cases that explore a range of valid, invalid, and edge case values to thoroughly test the function's handling of these inputs.",
         "Using the information in the docstring, determine the expected results of the function for various inputs. Craft Python test cases that compare the actual output of the function with these expected results under different scenarios.",
         "From the docstring, identify the limits and extremes within which the function is expected to operate. Write Python test cases that specifically test the function at these limits, ensuring it behaves correctly at its boundaries.",
         "Carefully analyze the docstring to understand the core purpose and functionality of the function. Develop a set of Python test cases that not only test the function's basic operations but also simulate real-world scenarios where the function would be applicable. Ensure these test cases cover a wide range of use cases as suggested by the function's intended purpose."
    ]

def bugfix_initial_population():
     return [
        "You are presented with a function which is not behaving as expected according to its docstring. Identify the bug and provide the corrected version of the function.",
        "Examine the given function and its docstring. The function contains an error. Find and fix the error to align the function's behavior with the docstring's description.",
        "Analyze the provided function which is currently not working as described in the docstring. Determine the cause of the discrepancy and correct the function.",
        "You are given a function that has a bug. Use the docstring as a guide to what the function should do and modify the function to fix the bug.",
        "The behavior of the given function does not match its docstring. Identify where it deviates and adjust the function to match the intended behavior.",
        "Inspect the provided function for errors. Cross-reference with its docstring to ensure it performs as documented, and rectify any inconsistencies found.",
        "A function and its docstring are provided. The function currently has a bug. Modify the function so that it aligns with the docstring's specifications.",
        "You're faced with a function that isn't working as per its docstring. Identify the problem in the function and correct it accordingly.",
        "The given function has a discrepancy with its docstring. Examine the function, find the bug, and correct it to match the docstring's description.",
        "Review the provided function and its docstring. There's a bug in the function. Correct it so that the function's output matches the docstring's intended behavior.",
        "Analyze the given function which is not performing as its docstring describes. Find the bug and adjust the function accordingly.",
        "A function with a bug is given alongside its docstring. Your task is to align the function's actual behavior with that described in the docstring.",
        "Identify the bug in the given function that causes it to deviate from its docstring description. Correct the function to match the docstring.",
        "You have a function that isn't behaving as described in its docstring. Find the error and modify the function to correct it.",
        "There is a discrepancy between the provided function's behavior and its docstring. Find and fix the error in the function.",
        "Examine the given function and its accompanying docstring. The function has a bug. Correct it to ensure it works as described in the docstring.",
        "You're given a function with a bug that makes it inconsistent with its docstring. Identify and rectify this bug.",
        "Inspect the given function and compare it to its docstring. The function contains an error. Fix this error to align the function with the docstring.",
        "A function is provided with a bug that contradicts its docstring. Your task is to identify and fix this bug.",
        "Align the provided function's actual behavior with its intended behavior as described in the docstring by identifying and fixing the existing bug.",
        "Review the provided function against its docstring. There's an inconsistency in its current operation. Diagnose and resolve the issue to make the function conform to the docstring's description.",
        "You are presented with a function that doesn't operate as outlined in its docstring. Examine the function, identify the flaw, and rework it to match the intended behavior as per the docstring.",
        "A function is given with its docstring, but the function contains a bug. Analyze the function, pinpoint the error, and refine the code to ensure it fulfills the docstring's criteria.",
        "Evaluate the given function, which is not aligning with its accompanying docstring. Identify the error in the function and modify it to accurately reflect the docstring's intended functionality.",
        "Given a function and its docstring, there is a misalignment in the function's actual performance versus what is described in the docstring. Your task is to diagnose the error within the function and rectify it to ensure it adheres to the docstring's guidelines."
    ]