import tkinter as tk


class AboutWindow(object):

    def __init__(self):
        self.aboutwindow = None

        self.aboutTextBox = None

        self.closeButton = None

    def show(self):
        self._create_window()
        self._create_widgets()
        self.aboutwindow.mainloop()

    def _create_window(self):
        self.aboutwindow = tk.Tk()
        self.aboutwindow.title("About")
        self.aboutwindow.iconbitmap("logo.ico")
        self.aboutwindow.geometry('350x380')

    def _create_widgets(self):
        self.aboutTextBox = tk.Text(self.aboutwindow, height=20, width=20)
        self.aboutTextBox.insert('end',"Kaan KULAK\nGTPC10\nGUI Hash Identifier")
        self.aboutTextBox.config(state=tk.DISABLED)
        self.aboutTextBox.pack()

        self.closeButton = tk.Button(self.aboutwindow)
        self.closeButton["text"] = "Close"
        self.closeButton["command"] = self._exit_about_menu
        self.closeButton.pack()

    def _exit_about_menu(self):
        self.aboutwindow.destroy()
