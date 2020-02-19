# This Python file uses the following encoding: utf-8

# if__name__ == "__main__":
#     pass

import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import Slot
'''
NOTE: The @Slot() is a decorator that identifies a function as a slot.
Always use to avoid unexpected behavior

'''

# Greetings
@Slot()
def say_hello():
    print("Button clicked, Hello!")


# Create the Qt application
app = QApplication(sys.argv)

# Create a Button
button = QPushButton("Click me")
# Connect the button to the function
button.clicked.connect(say_hello)
# Show the button
button.show()

# Run the main Qt loop
app.exec_()
