from google.transliteration import transliterate_word

def Transliterate(text):
    result = transliterate_word(text, lang_code='hi')
    return result[0]


