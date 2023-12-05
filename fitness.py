import google.generativeai as palm
import json
import re
import time
import random
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)

palm.configure(api_key='AIzaSyAQ8QUkbrX9DXCGDXbXv81Y4kGUhQXVvwY')
model = 'models/text-bison-001'


answer_extraction_prompt = {
    "integer": "\n\n--------------------------------------\n\nReturn the answer in integer. Only the answer. No explanation. No extra words. Just one integer.",
    "float":   "\n\n--------------------------------------\n\nReturn the answer in floating point number. Only the answer. No explanation. No extra words. Just one number.",
    "multiple choice": "\n\n--------------------------------------\n\nReturn the answer in one of A, B, C, D, E. Only the answer. No explanation. No extra words. Just one letter."
}



@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(2))
def palm_completion(prompt):
    completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # The maximum length of the response
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
        return int(result.group(0))
    elif answer_type == "float":
        result = re.search(r'\b\d+\.\d+\b', answer_text)
        return float(result.group(0))
    elif answer_type == "multiple choice":
        return answer_text.strip()
    

def fitness(template, questions):
    
    """
    DEPENDS ON WHICH DATASET WE CHOOSE. IF MULTIPLE DATASETS, DATASET SHOULD BE PASSED AS AN ARGUMENT
    """
    
    count = 0
    total = 0
    for q in questions:
        options = "\n".join(q["options"])
        problem = f"""
        {q["question"]}\n{options} 
        """
        ans = get_answer(problem, template=template, answer_type="multiple choice")
        
        if not ans:
            continue
        print(q["question"], ans, q["correct"])
        
        count += 1
        if ans==q["correct"]:
            total += 1
    
    return total / count


######## TEST ##########

with open("datasets/AQUA-RAT.json", mode="r") as file:
    questions = [json.loads(line.strip()) for line in file]

fit = fitness("Firstly, ", questions[:5])
print(fit)

        
        
        
            
        
    
    
    

