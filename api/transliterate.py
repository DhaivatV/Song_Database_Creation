from google.transliteration import transliterate_word

def Transliterate(text):
    result = transliterate_word(text, lang_code='hi')
    return result[0]


# print(Transliterate("I found a love, for me Darling, just dive right in and follow my lead  Well, I found a girl, beautiful and sweet Oh, I never knew you were the someone waiting for me"))