
from preprocessing_func import convert_fa_numbers, convert_ar_characters, convert_emojis_to_persian, convert_en_numbers
from preprocessing_func import  remove_diacritics, map_num_to_text, merge_mi_prefix

import re



def preprocess(text,
               convert_farsi_numbers = False,
               convert_english_numbers = False,
               convert_arabic_characters = False,
               remove_diacritic = False,
               convert_emojis = False,
               remove_half_space = False,
               remove_removelist = False,
               remove_extra_characters = False,
               remove_numbers = False,
               remove_punctuation = False,
               replace_multiple_space = False,
               handle_prefix = False,
               map_number_to_text = False
               
               ):
    
    text = text.strip()

    if convert_farsi_numbers:
        text = convert_fa_numbers(text)

    if convert_arabic_characters:
# convert arabic characters to persian
        text = convert_ar_characters(text)

    if remove_diacritic:
        text = remove_diacritics(text)

    if convert_emojis:
# convert Emojis
        text = convert_emojis_to_persian(text)
    
    if remove_removelist:
        removelist = "<>"
        # text = re.sub(r'[^\w'+removelist+']', ' ', text)
        # text = re.sub(r'[^\w]', ' ', text)
        # text = re.sub(r'((#)[\w]*)','#',text)
    
    if remove_half_space:
# remove half space
        text = text.replace('\u200c', '')
    
    if remove_extra_characters:
        text = re.sub(r'(\w)\1{2,}', r'\1\1',text)

    if map_number_to_text:
        text = map_num_to_text(text)

# remove numbers
    if remove_numbers:
        text = re.sub(r' [\d+]', ' ',text)

# convert english numbers to persian
    if convert_english_numbers:
        text = convert_en_numbers(text)
    
# remove punctuations
    if remove_punctuation:
        text= re.sub(r'[^\w\[\]]', ' ', text)

# replace multiple spaces with one space
    if replace_multiple_space:
        text = re.sub(r'[\s]{2,}', ' ', text)

# prefix
    if handle_prefix:
        text = merge_mi_prefix(text)
   
    
    return(text)