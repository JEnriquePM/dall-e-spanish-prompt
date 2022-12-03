from googletrans import Translator


def translate_input(input_str):
    if len(input_str) > 0:
        translator = Translator()
        translation = translator.translate(input_str, dest="en")
        return translation.text
