from PySimpleGUI import *
from random import *

theme('Black')
# обрабатываем нажатие на кнопку
def update():
    # получаем новое случайное число
    r = randint(1,100)
    # получаем доступ к текстовому элементу
    text_elem = window['-text-']
    # выводим в него текст с новым числом
    text_elem.update("Результат: {}".format(r))

# что будет внутри окна
# первым описываем кнопку и сразу указываем размер шрифта
layout = [[Button('Генерировать число', enable_events=True, key='-FUNCTION-', font='Any 10')], # Arial Any Helvetica
        # затем делаем текст
        [Text('Результат:',  key='-text-', font='Helvetica 10')]]
# size=(250, 100),
# рисуем окно
window = Window('Генератор случайных чисел', layout, size=(350,100))

# запускаем основной бесконечный цикл
while True:
    # получаем события, произошедшие в окне
    event, values = window.read()
    # если нажали на крестик
    if event in (WIN_CLOSED, 'Exit'):
        # выходим из цикла
        break
    # если нажали на кнопку
    if event == '-FUNCTION-':
        # запускаем связанную функцию
        update()

# закрываем окно и освобождаем используемые ресурсы
window.close()