from PySimpleGUI import *
    # Demo - Class wrapper
    #
    # Using a class to encapsulate PySimpleGUI Window creation & event loop
    #
    # This is NOT a recommended design pattern.  It mimics the object oriented design that many OO-based
    # GUI frameworks use, but there is no advantage to structuring you code in his manner.  It adds
    # confusion, not clarity.
    #
    # The class version is 18 lines of code.  The plain version is 13 lines of code.
    #
    # Two things about the class wrapper jump out as adding confusion:
    # 1. Unneccessary fragmentation of the event loop - the button click code is pulled out of the loop entirely
    # 2. "self" clutters the code without adding value
    #
    #
    # Copyright 2022, 2023 PySimpleGUI


class SampleGUI():

    def __init__(self):
        self.layout = [[Text('My layout')],
                       [Input(key='-IN-')],
                       [Button('Go'), Button('Exit')]]

        self.window = Window('My new window', self.layout)

    def run(self):
        while True:  # Event Loop
            self.event, self.values = self.window.read()
            if self.event in (WIN_CLOSED, 'Exit'):
                break

            if self.event == 'Go':
                self.button_go()

        self.window.close()

    def button_go(self):
        popup('Go button clicked', 'Input value:', self.values['-IN-'])


# Create the class
my_gui = SampleGUI()
# run the event loop
my_gui.run()

def gui_function():
    layout = [[Text('My layout')],
              [Input(key='-IN-')],
              [Button('Go'), Button('Exit')]]

    window = Window('My new window', layout)

    while True:  # Event Loop
        event, values = window.read()
        if event in (WIN_CLOSED, 'Exit'):
            break

        if event == 'Go':
            popup('Go button clicked', 'Input value:', values['-IN-'])

    window.close()


gui_function()