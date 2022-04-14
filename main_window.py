import tkinter as tk
from tkinter import END

import hashes as hs
import about_window
import writeoutput


class Window(object):

    def __init__(self):
        self.window = None

        self.hashInputEntryLabel = None
        self.hashInputEntry = None
        self.findHashButton = None

        self.menu = None

        self.textBox = None

        self.var = None
        self.writeoutput = None

    def show(self):
        self._create_window()
        self._create_widgets()
        self.window.mainloop()

    def _create_window(self):
        self.window = tk.Tk()
        self.window.title("Kaan's Hash Identifier")
        self.window.geometry('350x380')

    def _create_widgets(self):
        self.hashInputEntryLabel = tk.Label(self.window, text="Hash : ")
        self.hashInputEntry = tk.Entry(self.window, bd=5)

        self.hashInputEntryLabel.grid(column=0, row=0)
        self.hashInputEntry.grid(column=1, row=0)

        self.findHashButton = tk.Button(self.window)
        self.findHashButton["text"] = "Find hash!"
        self.findHashButton["command"] = self._find_hash_button_handler
        self.findHashButton.grid(column=3, row=0)

        self.textBox = tk.Text(self.window, height=20, width=30)
        self.textBox.grid(column=1, row=1)

        self.menu = tk.Menu(self.window)
        self.window.config(menu=self.menu)

        optionsMenu = tk.Menu(self.menu, tearoff=0)
        self.var = tk.IntVar()
        self.var.set(0)
        self.writeoutput = optionsMenu.add_checkbutton(label="Write output to file",variable=self.var,onvalue=1,offvalue=0)
        self.menu.add_cascade(label="Options", menu=optionsMenu)

        aboutMenu = tk.Menu(self.menu, tearoff=0)
        aboutMenu.add_command(label="Info", command=self.about_window)
        self.menu.add_cascade(label="About", menu=aboutMenu)

        self.menu.add_cascade(label="Exit", command=self.exit_program)

    def _find_hash_button_handler(self):
        self.textBox.delete('1.0', END)
        input_hash = self.hashInputEntry.get()
        algorithm_list = hs.compare_algorithms(input_hash)
        self.textBox.insert('end', "Given hash: " + f"${input_hash}" + "\n")
        self.textBox.insert('end', "\nPossible hashes: \n")
        for algo in algorithm_list:
            self.textBox.insert('end', "[+]" + algo + "\n")
        if self.var.get() == 1:
            writeoutput.writefile(data=self.textBox.get('1.0','end'))

        hs.clear_algo_list()

    def about_window(self):
        aboutwindow = about_window.AboutWindow()
        aboutwindow.show()

    def exit_program(self):
        exit(0)
