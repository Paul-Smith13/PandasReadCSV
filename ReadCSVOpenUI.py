'''
1. To create a user interface (UI) for the user.
2. This UI will have a button to open the file explorer.
3. File explorer will open the current directory.
4. The user will then select a file they want to open.
5. If it is a CSV file, then the user will be able to open it.
6.

'''

from tkinter import *
import tkinter.filedialog as tkfd
import os
from plot_CSV_series import *

def openFileExplorer():
    import tkinter
    print("Opening file explorer...")
    cwd = os.getcwd()
    filetypes = ('all files', '.*'), ('text files', '.txt')
    file_chosen = tkfd.askopenfilename(filetypes = filetypes,
                        initialdir = cwd)
    graph_title_name = graph_title_name_entry_box.get(1.0, END)
    left_Y_axis_name = left_Y_axis_name_entry_box.get(1.0, END)                    
    plot_series_and_change(file_chosen, graph_title_name, left_Y_axis_name)

window = Tk()

button = Button(window,
                text = "Open File",
                command = openFileExplorer,
                activebackground = "blue",
                activeforeground = "white"
                )

button.pack(padx=5, pady = 5)

graph_title_name_entry_box = Text(window, height = 3, width = 15)
left_Y_axis_name_entry_box = Text(window, height = 2, width = 15)

graph_title_name_entry_box.insert(END, "Enter figure title here")
left_Y_axis_name_entry_box.insert(END, "Enter Left Y Axis title here")


graph_title_name_entry_box.pack(padx = 15, pady = 15)
left_Y_axis_name_entry_box.pack(padx = 10, pady = 10)


window.configure(bg = "black")
window.title('Python Grapher')
window.geometry("600x200+10+20")
window.mainloop()


