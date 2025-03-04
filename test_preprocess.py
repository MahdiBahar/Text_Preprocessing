from preprocessing_main import preprocess



# text = "سلاااااممممم..... چطوری؟؟ اگه حالت خوبه..، یک ۱ برام می فرستی؟"
text = "سلاااااممممم..... چطوری؟؟ اگه (حالت) خوبه..، یک ۱ برام می فرستی؟"

preprocessed_text = preprocess(text,
               convert_farsi_numbers = False,
               convert_english_numbers = False,
               convert_arabic_characters = True,
               remove_diacritic = True,
               convert_emojis = False,
               remove_halfspace = True,
               remove_removelist = False,
               remove_extra_characters = True,
               remove_numbers = False,
               remove_punctuations = False,
               remove_punctuation_exception=True,
               replace_multiple_spaces = True,
               handle_prefix = True,
               map_number_to_text = True
               
               )

print(preprocessed_text)
