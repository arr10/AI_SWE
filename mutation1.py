import requests
import nltk
import random
import string
# import ssl
from nltk.corpus import wordnet
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize


# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context

# nltk.download()


changeable_pos_tags = ['JJ', 'JJR', 'JJS', 'NN', 'NNS', 'PDT', 'RB', 'RBR', 'RBS', 'RP', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']



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



def mutate_word_level(text):
    words = word_tokenize(text)

    # Mutate words with synonyms based on their part of speech
    mutated_text = []
    for word in words:
          pos = get_part_of_speech(word)
          if pos in changeable_pos_tags:
            synonyms = get_synonyms(word)
            if synonyms:
                mutated_text.append(synonyms[random.randrange(0, len(synonyms))])
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




if(__name__ == '__main__'):
    original_text = "What a beautiful day it is. I wish to jump over the fences, go prancing across the meadow"
    mutated_text = mutate_word_level(original_text)
    print("Original Text:", original_text)
    print("Mutated Text:", mutated_text)



# api_key = 'ADD IT'

# word = 'asking'
# api_url = 'https://api.api-ninjas.com/v1/thesaurus?word={}'.format(word)
# response = requests.get(api_url, headers={'X-Api-Key': api_key})
# if response.status_code == requests.codes.ok:
#     print(response.text)
# else:
#     print("Error:", response.status_code, response.text)
