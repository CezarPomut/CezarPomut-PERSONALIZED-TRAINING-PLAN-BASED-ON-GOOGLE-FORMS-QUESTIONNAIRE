# Python program to create
# a file explorer in Tkinter
import os

# import all components
# from the tkinter library
from tkinter import *

# import filedialog module
from tkinter import filedialog
from read_excel_data import *

# Function for opening the
# file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("all files",
                                                      "*.*")))

    filepath = os.path.abspath(filename)
    print(filepath)
    print(type(filepath))
    text_file_explorer.insert('1.0',filepath)

def run():
    file_path=text_file_explorer.get('1.0', END)
    print(file_path)
    run_main(file_path)


# Create the root window
window = Tk()

# Set window title
window.title('File Explorer')

# Set window size
window.geometry("500x500")

# Set window background color
window.config(background="white")

# Create a File Explorer label
text_file_explorer = Text(window,
                            fg="black",borderwidth=10,relief=RIDGE, height=1,width=40,padx=10,pady=5)

button_explore = Button(window,
                        text="Browse Files",
                        command=browseFiles)

button_exit = Button(window,
                     text="Exit",
                     command=exit)

button_run= Button(text="Run",command=run)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
text_file_explorer.place(x=75,y=100)

button_explore.place(x=200,y=170)

button_exit.place(x=240,y=200)

button_run.place(x=200,y=200)

# Let the window wait for any events
window.mainloop()
