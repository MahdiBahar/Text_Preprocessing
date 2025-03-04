import re
import emoji


def _multiple_replace(mapping, text):
    pattern = "|".join(map(re.escape, mapping.keys()))
    return re.sub(pattern, lambda m: mapping[m.group()], str(text))

def convert_fa_numbers(input_str):
    mapping = {
        '۰': '0',
        '۱': '1',
        '۲': '2',
        '۳': '3',
        '۴': '4',
        '۵': '5',
        '۶': '6',
        '۷': '7',
        '۸': '8',
        '۹': '9',
        '.': '.',
    }
    return _multiple_replace(mapping, input_str)

def convert_en_numbers(input_str):
    mapping = {
         '0': '۰',
         '1' : '۱',
         '2' :'۲',
        '3'  :'۳',
        '4'  :'۴',
        '5' :'۵',
        '6' :'۶',
        '7' :'۷',
        '8' :'۸',
        '9' :'۹',
        '.' :'.'
    }
    return _multiple_replace(mapping, input_str)

def convert_ar_characters(input_str):
    """
    Converts Arabic chars to related Persian unicode char
    """
    mapping = {
        'ك': 'ک',
        'ى': 'ی',
        'ي': 'ی',
        'ئ':'ی',
        'إ':'ا',
        'أ':'ا',
        'ة':'ه',
        'ؤ':'و'
    }
    return _multiple_replace(mapping, input_str)

#-------------------------------------------------------------------------------------------


def convert_emojis_to_persian(text):
    # First, convert emojis to English descriptive labels.
    # This will convert "😊" into something like ":smiling_face_with_smiling_eyes:".
    demojized_text = emoji.demojize(text)
    
    # Define a dictionary mapping some common English emoji labels to Persian words.
    persian_emoji_map = {
        ":smiling_face_with_smiling_eyes:": "خندان",
        ":grinning_face:": "با لبخند",
        ":face_with_tears_of_joy:": "با اشک شوق",
        ":red_heart:": "عشق",
        ":thumbs_up:": "پسندیده",
        ":thumbs_down:" : "نپسندیده" , # 👎
        ":OK_hand:" : "خوب", # 👌
        "folded_hands": "تشکر"  ,
        "rose" : "مرسی" , 
        "cherry_blossom" : "سپاس" ,
        "face_with_symbols_on_mouth" : "خیلی عصبانی" , 
        ":face_vomiting:" : "مزخرف" , #  🤮
        ":angry_face:" : "عصبانی", # 😠
        ":broken_heart:" : "قلب شکسته", # 💔
        ":clapping_hands:" : "عالی" , # 👏 
        ":confused_face:" : "گیج شدم" , # 😕 
        ":crying_face:" : "گریه میکنم" , # 😢 
        ":disappointed_face:" : "ناامید", # 😞 
        ":enraged_face:" : "عصبانی" , # 😡
        ":expressionless_face:" : "خنثی" , # 😑
        ":sparkling_heart:" : "دوستداشتنی" , # 💖
        ":smiling_face_with_heart-eyes:" : "دوستداشتنی", # 😍
    
    
    }
    # Replace known emojis with Persian equivalents
    for eng_label, pers_label in persian_emoji_map.items():
        persian_formatted = f"[{pers_label}]"  # Wrap in brackets
        demojized_text = re.sub(re.escape(eng_label), persian_formatted, demojized_text)

    # Replace any remaining :emoji_name: patterns (unmapped emojis) with a space
    demojized_text = re.sub(r':[a-zA-Z0-9_]+:', ' ', demojized_text)
    
    return demojized_text

#--------------------------------------------------------------------------------------------------------


def merge_mi_prefix(text):

    return re.sub(r'\b(ن?می)\s+(\S+)', r'\1\2', text)

def remove_diacritics(text):
    # Define regex for Persian diacritics (Unicode range: \u064B-\u0652)
    diacritics_pattern = re.compile(r'[\u064B-\u0652]')
    return re.sub(diacritics_pattern, '', text)


def convert_number_to_text(text):
    
    return re.sub(r'(\d)\d*', r'\1', text)

def remove_half_space(text):

    text = text.replace('\u200c', '')
    return text

def remove_extra_charecter(text):

    return re.sub(r'(\w)\1{2,}', r'\1\1',text)

def remove_number(text):

    return re.sub(r' [\d+]', ' ',text)

def remove_punctuation(text):

    return re.sub(r'[^\w\[\]]', ' ', text)

def replace_multiple_space(text):

    return re.sub(r'[\s]{2,}', ' ', text)


def map_num_to_text(text):

    # Check if the text is exactly '1', '2', or '3' (nothing else)
    mapping = {'1': 'خیلی بد', '2': 'بد', '3': 'متوسط' , '4': 'خوب' , '5': 'عالی'}
    
    if text in mapping:
        return mapping[text]  
    
    return text 
#--------------------------------------------------------------------------------------------------------

