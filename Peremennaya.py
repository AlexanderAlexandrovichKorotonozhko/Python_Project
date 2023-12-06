from transliterate import translit


def permennaya(ru_text):
    text = translit(ru_text, language_code='ru', reversed=True)
    text = text.split()
    per = '_'.join(text)
    print(per)


permennaya(input("Ввод русcкого текста>>> "))
