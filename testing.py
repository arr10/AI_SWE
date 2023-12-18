import google.generativeai as palm
import json
import re
import time
import random
import os
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)
from dotenv import load_dotenv
import asyncio
load_dotenv()

api_key = os.getenv('PALM2_API_KEY')
model = 'models/text-bison-001'

palm.configure(api_key=api_key)

answer_extraction_prompt = {
    "integer": "\n\n--------------------------------------\n\nReturn the answer in integer. Only the answer. No explanation. No extra words. Just one integer.",
    "float":   "\n\n--------------------------------------\n\nReturn the answer in floating point number. Only the answer. No explanation. No extra words. Just one number.",
    "multiple choice": "\n\n--------------------------------------\n\nReturn the answer in one of A, B, C, D, E. Only the answer. No explanation. No extra words. Just one letter."
}

file = open("datasets/gsm8k_90.json", mode="r")
gsm8k_dataset = json.load(file)
file.close()


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
    

def fitness_reasoning(template, dataset='gsm8k_90'):
    count = 0
    total = 0
    file = open(f"datasets/{dataset}.json", mode="r")
    datasets = json.load(file)
    file.close()
    for dataset in datasets:
        answer_type = 'integer'
        if dataset in ['aqua', 'date_understanding', 'tracking_shuffled_objects', 'commonsense_qa']:
            answer_type = 'multiple choice'
        questions = datasets[dataset]
        for q in questions:
            if '.' in q['answer']:
                answer_type = 'float'
            ans = get_answer(q['question'], template, answer_type)
            if not ans:
                continue
            
            count += 1
            if str(ans)==str(q["answer"]):
                total += 1
            print(ans, q["answer"], count, total)
    if count == 0:
        return 0
    return total / count
# def fitness(template, questions):
def fitness(template):
    
    """
    """
    
    return fitness_reasoning(template)

######## TEST ##########

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog='testing',
        description='test the given prompt on a given dataset')
    parser.add_argument('-d', '--dataset', type=str)
    parser.add_argument('-p', '--prompt', type=str)
    args = parser.parse_args()

    t = time.time()
    dataset = args.dataset
    prompt = args.prompt
    fit = fitness_reasoning(prompt, dataset)
    print(fit)
    print(time.time() - t)

        
        
        
            
        
    
    
    

