from transliterate import translit
from translate import Translator


# версия 1.3
def permennaya(ru_text):
    text = translit(ru_text, language_code='ru', reversed=True)
    text = text.split()
    per = '_'.join(text)
    # print(per)
    return per


# print(permennaya(input("Ввод русcкого текста>>> ")))
def dob_test(peremennaya):
    text = 'test_' + permennaya(peremennaya)
    # print(text)
    return text
print(dob_test(input('test+ ')))
# text = input()
# trans = Translator(from_lang="russian",to_lang="English")
# text_t = trans.translate(text)
# print(text_t)

# версия 2.0
# def permennaya(ru_text):
#     trans = Translator(from_lang="russian", to_lang="English")
#     text_t = trans.translate(ru_text)
#     # print(text_t)
#     text = text_t.split()
#     per = '_'.join(text)
#     print(per)
#
#
# permennaya(input("Ввод русcкого текста>>> "))
