'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run
through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details.
'''
from . import cmudict

_pad        = '_'
_eos        = '~'
_punctuation = '!\'(),.:;?- '
#_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!\'\"(),-.:;? '
_characters_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
_svowels_ru = ['а́', 'и́', 'у́', 'э́', 'о́', 'ю́', 'я́', 'ы́', 'е́']
_stress_vowels = {'á': 'а', 'ó': 'о', 'é': 'е', 'ý': 'у',
                  'а́': 'а', 'и́': 'и', 'у́': 'у', 'э́': 'э', 'о́': 'о', 'ю́': 'ю', 'я́': 'я', 'ы́': 'ы', 'е́': 'е'}
_stress_vowels_inv = {v: k for k, v in _stress_vowels.items()}
# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
#_arpabet = ['@' + s for s in cmudict.valid_symbols]

# Export all symbols:
# symbols = [_pad, _eos] + list(_characters) #+ _arpabet
ru_symbols = [_pad, _eos] + list(_punctuation) + list(_characters_ru) + _svowels_ru
symbols = ru_symbols