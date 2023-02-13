from google.transliteration import transliterate_word

def transliterate(text):
    result = transliterate_word(text, lang_code='hi')
    return result[0]


