import random
from openai import OpenAI

client = OpenAI(api_key = 'your-key')


def crossover(parent1, parent2, rate):
        
    if random.random() < rate:
        
        prompt = f"Crossover the following sentences and return a new sentence: {parent1}, {parent2}"
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=2
        )

        generated_sentence = response.choices[0].message.content

        print(generated_sentence)#chat.choices[0].message.content.lower()
        off1 = generated_sentence
        off2 = generated_sentence
    else:
        off1 = parent1
        off2 = parent2
    return off1, off2

print(crossover("Let's think step by step", "Before we dive into the answer", 1))