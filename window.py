import tkinter as tk
from tkinter import END

import hashes as hs


class Window(object):

    def __init__(self):
        self.window = None

        self.hashInputEntryLabel = None
        self.hashInputEntry = None
        self.findHashButton = None

        self.textBox = None

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

    def _find_hash_button_handler(self):
        self.textBox.delete('1.0', END)
        input_hash = self.hashInputEntry.get()
        algorithm_list = hs.compare_algorithms(input_hash)
        self.textBox.insert('end', "Possible hashes: \n")
        for algo in algorithm_list:
            self.textBox.insert('end', "[+]" + algo + "\n")
        hs.clear_algo_list()
