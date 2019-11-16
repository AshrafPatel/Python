from translate import Translator

my_file = open("english.txt", mode="r")
translator = Translator(to_lang="zh")
translator2 = Translator(to_lang="es")

with open("translate.txt", mode="w", encoding="utf-8") as translate_file:
    text = my_file.read();
    translate_file.write(translator.translate(text) + "\n")
    translate_file.write(translator2.translate(text) + "\n")

my_file.close()