import random
import openai

def crossover(parent1, parent2, rate):
    
    openai.api_key = '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'
    if random.random() < rate:
        messages = [
        {"role": "user", "content": "Crossover following sentences and return two sentences: " + parent1 + ", " + parent2}
        ]
        chat = openai.Completion.create(
            model="gpt-3.5-turbo", messages= messages
        )

        ans = chat.choices[0].message.content.lower()
        off1 = ans
        off2 = ans
    else:
        off1 = parent1
        off2 = parent2
    return off1, off2

print(crossover("Let's think step by step", "Before we dive into the answer", 1))