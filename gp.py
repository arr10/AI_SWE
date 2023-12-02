import requests
import random
import os

TRANSLATION_API_KEY = os.environ.get('TRANSLATION_API_KEY')

def get_translation(query, source, target):
    url = 'https://translation.googleapis.com/language/translate/v2'
    params = {
        'q': query,
        'source': source,
        'target': target,
        'key': 'AIzaSyD5flu_ECUNVLbWvzH1S7643ljsGN0ciGg'
    }
    response = requests.get(url, params=params)
    return response.json()['data']['translations'][0]['translatedText']

def backtranslation(prompt):
    languages = ['af', 'sq', 'am', 'ar', 'hy', 'as', 'ay', 'az', 'bm', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'or', 'zh', 'co', 'hr', 'cs', 'da', 'dv', 'nl', 'en', 'eo', 'et', 'ee', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gn', 'gu', 'ht', 'ha', 'he', 'or', 'iw', 'hi', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jv', 'or', 'jw', 'kn', 'kk', 'km', 'rw', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'ln', 'lt', 'lg', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'ny', 'or', 'om', 'ps', 'fa', 'pl', 'pt', 'pa', 'qu', 'ro', 'ru', 'sm', 'sa', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tl', 'tg', 'ta', 'tt', 'te', 'th', 'ti', 'ts', 'tr', 'tk', 'ak', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu']
    source = 'en'
    for language in random.sample(languages, 4):
        prompt = get_translation(prompt, source, language)
        source = language
    prompt = get_translation(prompt, source, 'en')
    return prompt

def get_initial_popularion():
        return ["Let's think step by step.",
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
        "Let's first understand the problem, extract relevant variables and their corresponding numerals, and make a complete plan. Then, let's carry out the plan, calculate intermediate variables (pay attention to correct numerical calculation and commonsense), solve the problem step by step, and show the answer."]

if(__name__ == '__main__'):
    print(backtranslation('Lets think like a detective, step by step.'))