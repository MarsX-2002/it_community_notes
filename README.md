# Notes from the Opening Ceremony of an IT Community of Uzbekistan (ICU)

# Introduction
This is a simple Python script that allows users to input notes and output them in a formatted manner.

# Usage
To use this script, simply run it in a Python environment. You will be prompted to input notes, and you can type "exit" at any time to stop inputting notes and see the notes you have inputted.

# Functions
inputNote()
This function prompts the user to input notes, which are stored in a list. If the user inputs "exit", the function returns the list.

outputNote()
This function takes a list of notes as input and outputs them in a formatted manner, with each note numbered.

noteStored()
This function contains a list of notes as an example of how the outputNote() function can be used.

# Example
python code
```from note_taker import inputNote, outputNote

notes = inputNote()
outputNote(notes)```

# Credits
This script was created by `https://www.linkedin.com/in/mirjalol-shavkatov/` as part of a note-taking exercise.
