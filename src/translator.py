from translations import english_to_genz, genz_to_english
import re

# print(genz_to_english)

# print(translations_dict.get('win'))

def translate(message, to_genz=False):
    
    if to_genz:
        translation_dict=english_to_genz
    else:
        translation_dict=genz_to_english

    message=message.lower()
    output = []
    exp = "[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+" #finds characters, removes punctuation

    for word in re.findall(exp, message):

        translated_word=translation_dict.get(word, word)
        # print(translated_word)
        if type(translated_word) == list:
            output.append('/'.join(translated_word))
        else:
            output.append(translated_word)

    return " ".join(output)



