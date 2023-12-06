import requests
import nltk
import random
import string
import os
from nltk.corpus import wordnet
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
import stanza
from nltk import Tree
from dotenv import load_dotenv
import google.generativeai as palm

try:
    stanza.download('en', processors='tokenize,pos,lemma,parse,depparse')
except Exception as e:
    stanza.install_corenlp()

from stanza.server import CoreNLPClient

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context

# nltk.download()


changeable_pos_tags = ['JJ', 'JJR', 'JJS', 'NN', 'NNS', 'PDT', 'RB',
                       'RBR', 'RBS', 'RP', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']

load_dotenv()

api_key = os.getenv('PALM2_API_KEY')
palm.configure(api_key=api_key)
model = 'models/text-bison-001'

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

TRANSLATION_API_KEY = os.environ.get('TRANSLATION_API_KEY')


# Get the part of speech for a given word
def get_part_of_speech(word):
    pos_tagged = pos_tag([word])
    return pos_tagged[0][1]


def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return synonyms


def mutation_word_level(text):
    words = word_tokenize(text)

    # Mutate words with synonyms based on their part of speech
    mutated_text = []
    for word in words:
        pos = get_part_of_speech(word)
        if pos in changeable_pos_tags:
            synonyms = get_synonyms(word)
            if synonyms:
                mutated_text.append(
                    synonyms[random.randrange(0, len(synonyms))])
            else:
                mutated_text.append(word)
        else:
            mutated_text.append(word)

    # result = ' '.join(mutated_text)
    result = ''
    for w in mutated_text:
        if w in string.punctuation:
            result += w
        else:
            result += ' ' + w
    return result


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
        if subtree.label() == "S" or subtree.label() == "SBAR":
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

# simply pass the text based prompt as a string, it will return mutated output
# it works by removing a phrase from a sentence and asking PALM2 to complete it


def mutation_sent_comp(prompt):
    phrases_list = split_phrase(prompt)
    w_blank = make_input(phrases_list)
    input_prompt = global_prompt.format(variable_string=w_blank)
    output = palm_completion(input_prompt)
    return output


def get_translation(query, source, target):
    url = 'https://translation.googleapis.com/language/translate/v2'
    params = {
        'q': query,
        'source': source,
        'target': target,
        'key': TRANSLATION_API_KEY
    }
    response = requests.get(url, params=params)
    return response.json()['data']['translations'][0]['translatedText']


def mutation_backtranslation(prompt):
    '''Input: prompt (string), Output: backtranslated promtp (string)'''
    languages = ['af', 'sq', 'am', 'ar', 'hy', 'as', 'ay', 'az', 'bm', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'or', 'zh', 'co', 'hr', 'cs', 'da', 'dv', 'nl', 'en', 'eo', 'et', 'ee', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gn', 'gu', 'ht', 'ha', 'he', 'or', 'iw', 'hi', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jv', 'or', 'jw', 'kn', 'kk', 'km', 'rw', 'ko', 'ku', 'ky', 'lo', 'la',
                 'lv', 'ln', 'lt', 'lg', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'ny', 'or', 'om', 'ps', 'fa', 'pl', 'pt', 'pa', 'qu', 'ro', 'ru', 'sm', 'sa', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tl', 'tg', 'ta', 'tt', 'te', 'th', 'ti', 'ts', 'tr', 'tk', 'ak', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu']
    source = 'en'
    for language in random.sample(languages, 4):
        prompt = get_translation(prompt, source, language)
        source = language
    prompt = get_translation(prompt, source, 'en')
    return prompt


def mutate(prompt):
    r = random.randint(1, 3)
    r = 2
    match r:
        case 1:
            return mutation_backtranslation(prompt)
        case 2:
            return mutation_sent_comp(prompt)
        case 3:
            return mutation_word_level(prompt)


if (__name__ == '__main__'):
    original_text = "Please follow the prompt as accurately as possible, wihtout any sort of swear words"
    mutated_text = mutate(original_text)
    print("Original Text:", original_text)
    print("Mutated Text:", mutated_text)