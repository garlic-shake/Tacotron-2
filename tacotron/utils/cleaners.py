'''
Cleaners are transformations that run over the input text at both training and eval time.

Cleaners can be selected by passing a comma-delimited list of cleaner names as the "cleaners"
hyperparameter. Some cleaners are English-specific. You'll typically want to use:
  1. "english_cleaners" for English text
  2. "transliteration_cleaners" for non-English text that can be transliterated to ASCII using
     the Unidecode library (https://pypi.python.org/pypi/Unidecode)
  3. "basic_cleaners" if you do not want to transliterate (in this case, you should also update
     the symbols in symbols.py to match your data).
'''

import re

from unidecode import unidecode

from .numbers import normalize_numbers
from tacotron.utils.num2t4ru import num2text
from .symbols import _stress_vowels, _stress_vowels_inv

# Regular expression matching whitespace:
_whitespace_re = re.compile(r'\s+')

# List of (regular expression, replacement) pairs for abbreviations:
_abbreviations = [(re.compile('\\b%s\\.' % x[0], re.IGNORECASE), x[1]) for x in [
  ('mrs', 'misess'),
  ('mr', 'mister'),
  ('dr', 'doctor'),
  ('st', 'saint'),
  ('co', 'company'),
  ('jr', 'junior'),
  ('maj', 'major'),
  ('gen', 'general'),
  ('drs', 'doctors'),
  ('rev', 'reverend'),
  ('lt', 'lieutenant'),
  ('hon', 'honorable'),
  ('sgt', 'sergeant'),
  ('capt', 'captain'),
  ('esq', 'esquire'),
  ('ltd', 'limited'),
  ('col', 'colonel'),
  ('ft', 'fort'),
]]


def expand_abbreviations(text):
  for regex, replacement in _abbreviations:
    text = re.sub(regex, replacement, text)
  return text


def expand_numbers(text):
  return normalize_numbers(text)


def lowercase(text):
  '''lowercase input tokens.
  '''
  return text.lower()


def collapse_whitespace(text):
  return re.sub(_whitespace_re, ' ', text)


def convert_to_ascii(text):
  return unidecode(text)


def basic_cleaners(text):
  '''Basic pipeline that lowercases and collapses whitespace without transliteration.'''
  text = lowercase(text)
  text = collapse_whitespace(text)
  return text


def transliteration_cleaners(text):
  '''Pipeline for non-English text that transliterates to ASCII.'''
  text = convert_to_ascii(text)
  text = lowercase(text)
  text = collapse_whitespace(text)
  return text


def english_cleaners(text):
  '''Pipeline for English text, including number and abbreviation expansion.'''
  text = convert_to_ascii(text)
  # text = lowercase(text)
  text = expand_numbers(text)
  text = expand_abbreviations(text)
  text = collapse_whitespace(text)
  return text

p_num = re.compile(r'[0-9]+')
def expand_numbers_ru(text):
    text = text.replace('%', ' процент')
    text = text.replace('$', ' доллар')
    shift = 0
    for m in p_num.finditer(text):
        num_text = num2text(int(m.group(0)))
        text = text[:m.start()+shift] + num_text + text[m.end()+shift:]
        shift += len(num_text) + m.start() - m.end()
    return text

from russ.stress.model import StressModel

model = StressModel.load()
p = re.compile('[а-яё' + ''.join(_stress_vowels) + '-]+')
stress_fix = {'она': 2, 'семье': 4, 'прямо': 2, 'чудеса': 5, 'если': 0, 'его': 2, 'ужас': 0, 'было': 1, 'дому': 3, 'шаги': 3, 'либо': 1, 'тому': 3,
              'они': 2, 'мои': 2, 'себе': 3, 'имя': 0, 'тебе': 3, 'после': 1,
              'дано': 3, 'дела': 3, 'никто': 4, 'тебя': 3, 'зачем': 3, 'сама': 3, 'этот': 0, 'куда': 3, 'весы': 3, 'хуже': 1,
              'саблин': 1, 'саблину': 1, 'саблиным': 1, 'саблина': 1, 'осипу': 0, 'осипа': 0, 'осипом': 0, 'софья': 1, 'карловна': 1, 'борис': 3, 'яшу': 0,
              'фомину': 5, 'пухова': 1, 'елен': 2,
              'что-нибудь': 2, 'кто-нибудь': 2, 'где-нибудь': 2, 'когда-нибудь': 4, 'каким-то': 3, 'кому-то': 3,
              'новгороде': 1, 'новгород': 1, 'казани': 3,
              'ежели': 0, 'помощницу': 3, 'площади': 2, 'сторону': 2, 'плохи': 2, 'мести': 1, 'нехотя': 5, 'худобу': 5, 'очереди': 0, 'деньгах': 5,
              'господь': 4, 'лекарств': 3, 'слева': 2, 'память': 1, 'поздно': 1, 'несколько': 1, 'должна': 5, 'вывозят': 3,
              'голосом': 1, 'поезде': 1, 'тортийю': 4, 'развит': 1, 'губам': 3, 'наяву': 4, 'крупу': 4, 'пополам': 5, 'труднее': 5,
              'власти': 2, 'купе': 3, 'мире': 1,
              'четырнадцать': 3,}


def stress_cleaners(text):
    words = [x for x in p.findall(text) if not 'ё' in x and not any(s in x for s in _stress_vowels)]
    st_dict = model.predict_words_stresses(words)

    new_text = ''
    for w in words:
        if w in st_dict and len(st_dict[w]) > 0 and len(w) > 1:
            pos = st_dict[w][0]
            if w in stress_fix:
                pos = stress_fix[w]
            m = re.search(r'([^а-яёА-ЯЁ́]|^)(' + w + r')([^а-яёА-ЯЁ́]|$)', text)
            if m is None:
                print(text, w)
            text = text[:m.start(2)] + w[:pos] + _stress_vowels_inv[w[pos]] + w[pos+1:] + text[m.end(2):]
            #text = text.replace(w, w[:pos] + _stress_vowels_inv[w[pos]] + w[pos+1:])

    return text

def russian_cleaners(text):
    text = basic_cleaners(text)
    text = expand_numbers_ru(text)
    text = stress_cleaners(text)
    return text