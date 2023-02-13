from google.transliteration import transliterate_word

def transliterate(text):
    result = transliterate_word('''Phir le aaya dil majboor kya keeje
Raas na aaya rehna door kya keeje
Dil keh raha use maqammal kar bhi aao
Wo jo adhoori si baat baaki hai
Wo jo adhoori si yaad baaki hai
Wo jo adhoori si yaad baaki hai''', lang_code='hi')
    return result


