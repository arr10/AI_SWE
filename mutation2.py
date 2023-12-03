# install stanza, nltk
# install google.generativeai

import stanza
from nltk import Tree
import random
import os
from dotenv import load_dotenv
import google.generativeai as palm

try:
    stanza.download('en', processors='tokenize,pos,lemma,parse,depparse')
except Exception as e:
    stanza.install_corenlp()

from stanza.server import CoreNLPClient

load_dotenv()

api_key=os.getenv('PALM2_API_KEY')
palm.configure(api_key=api_key)
model = 'models/text-bison-001'



def split_phrase(text):
    with CoreNLPClient(
            annotators=['tokenize', 'pos', 'lemma', 'parse', 'depparse'],
            output_format="json",
            timeout=30000,
            memory='16G') as client:
        output = client.annotate(text)
        parse_tree = output['sentences'][0]['parse']
        parse_tree = ' '.join(parse_tree.split())

    t = Tree.fromstring(parse_tree)

    subtexts = []
    for subtree in t.subtrees():
        if subtree.label()=="S" or subtree.label()=="SBAR":
            subtexts.append(' '.join(subtree.leaves()))

    presubtexts = subtexts[:]

    for i in reversed(range(len(subtexts)-1)):
        subtexts[i] = subtexts[i][0:subtexts[i].index(subtexts[i+1])]
    return subtexts



def make_input(phrase_list):
    filtered_parts = [part for part in phrase_list if len(part.split()) > 1]

    if filtered_parts:
        selected_part = random.choice(filtered_parts)
        phrase_list[phrase_list.index(selected_part)] = '[BLANK] '
        return ''.join(phrase_list)
    
    else:
        selected_part = random.choice(phrase_list)
        phrase_list[phrase_list.index(selected_part)] = '[BLANK] '
        return ''.join(phrase_list)



def palm_completion(prompt):
    completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0.8,
    max_output_tokens=800,
    )
    return completion.result



global_prompt = """
Fill the sentence with a suitable phrase where it is tagged [BLANK]. Please output the whole sentence.
Follow the examples given.

Text : "Yesterday when I was [BLANK] I saw a duck"
"Yesterday when I was walking beside the pond I saw a duck"

-----------------------------------------------------------------
Text: "I turned on my computer and [BLANK] but did not like it"
"I turned on my computer and surfed the net but did not like it"

-----------------------------------------------------------------
Text: {variable_string}
"""


# simply pass the text based prompt as a string, it will return mutated output
# it works by removing a phrase from a sentence and asking PALM2 to complete it

def mutation_sent_comp(prompt):
    phrases_list = split_phrase(prompt)
    w_blank = make_input(phrases_list)
    input_prompt = global_prompt.format(variable_string=w_blank)
    output = palm_completion(input_prompt)
    return output



text = "Please follow the prompt as accurately as possible, wihtout any sort of swear words"
print(mutation_sent_comp(text))
