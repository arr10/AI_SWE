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
import ssl

# try:
#     stanza.download('en', processors='tokenize,pos,lemma,parse,depparse')
# except Exception as e:
#     stanza.install_corenlp()

# from stanza.server import CoreNLPClient

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
            # start_server=StartServer.TRY_START,
            annotators=['tokenize', 'pos', 'lemma', 'parse', 'depparse'],
            output_format="json",
            timeout=30000,
            memory='16G') as client:
        output = client.annotate(text)
        parse_tree_list = []
        for p_t in output['sentences']:
            parse_tree_list.append(' '.join(p_t['parse'].split()))

    sentences = []
    for parse_tree in parse_tree_list:
        t = Tree.fromstring(parse_tree)

        subtexts = []
        for subtree in t.subtrees():
            if subtree.label()=="S" or subtree.label()=="SBAR" or subtree.label() == "FRAG":
                subtexts.append(' '.join(subtree.leaves()))
        
        for i in reversed(range(len(subtexts)-1)):
            if subtexts[i+1] in subtexts[i]:
                subtexts[i] = subtexts[i][0:subtexts[i].index(subtexts[i+1])]
            else:
                subtexts[i] = subtexts[i]
        sentences.append(subtexts)
    
    merged = []
    for sent in sentences:
        sent[-1] += ". "
        for s in sent:
            merged.append(s)

    return merged


def sentence_splitter(sentence):
    words = sentence.split()
    min_words_per_phrase = 3
    max_words_per_phrase = len(words) // 2
    words_per_phrase = random.randint(min_words_per_phrase, max_words_per_phrase)
    phrases = [words[i:i + words_per_phrase] for i in range(0, len(words), words_per_phrase)]
    result_sentences = [' '.join(phrase) for phrase in phrases]

    return result_sentences


def make_input(phrase_list):
    filtered_parts = [part for part in phrase_list if len(part.split()) > 1]

    if filtered_parts:
        selected_part = random.choice(filtered_parts)
        phrase_list[phrase_list.index(selected_part)] = '[BLANK] '
        return ' '.join(phrase_list)

    else:
        selected_part = random.choice(phrase_list)
        phrase_list[phrase_list.index(selected_part)] = '[BLANK] '
        return ' '.join(phrase_list)


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
    phrases_list = sentence_splitter(prompt)
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
    translated_text = ""
    try:
        translated_text = response.json()['data']['translations'][0]['translatedText']
    except Exception as e:
        translated_text = query
        print("problems with backtranslation")
        print(response.json()['error']['message'])
    return translated_text


def mutation_backtranslation(prompt):
    '''Input: prompt (string), Output: backtranslated promtp (string)'''
    languages = ['af', 'sq', 'am', 'ar', 'hy', 'as', 'ay', 'az', 'bm', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'or', 'zh', 'co', 'hr', 'cs', 'da', 'dv', 'nl', 'eo', 'et', 'ee', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gn', 'gu', 'ht', 'ha', 'he', 'or', 'iw', 'hi', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jv', 'or', 'jw', 'kn', 'kk', 'km', 'rw', 'ko', 'ku', 'ky', 'lo', 'la',
                 'lv', 'ln', 'lt', 'lg', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'ny', 'or', 'om', 'ps', 'fa', 'pl', 'pt', 'pa', 'qu', 'ro', 'ru', 'sm', 'sa', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tl', 'tg', 'ta', 'tt', 'te', 'th', 'ti', 'ts', 'tr', 'tk', 'ak', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu']
    source = 'en'
    temp = prompt
    for language in random.sample(languages, 4):
        
        new_prompt = get_translation(prompt, source, language)
        if prompt != new_prompt: 
            prompt = new_prompt
            source = language
        # in case tranlsation fails do nothing

    new_prompt = get_translation(prompt, source, 'en')
    # To ensure return is always in english
    if prompt == new_prompt:
        prompt = temp
    else:
        prompt = new_prompt
    return prompt


def mutate(prompt, rate=1):
    '''randomly select a mutation method and apply it to the prompt. Mutation is applied with chance of rate'''
    p = random.random()
    if p > rate:
        return prompt
    r = random.randint(1, 3)
    match r:
        case 1:
            return mutation_backtranslation(prompt)
        case 2:
            return mutation_word_level(prompt)
        case 3:
            return mutation_sent_comp(prompt)


if (__name__ == '__main__'):
    original_text = "Please follow the prompt as accurately as possible, wihtout any sort of swear words"
    mutated_text = mutate(original_text)
    print("Original Text:", original_text)
    print("Mutated Text:", mutated_text)