import tkinter as tk
from tkinter import filedialog
from tkinter import *
from predict import predict_cell


class MainWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.source_directory = StringVar()
        self.labelText = StringVar()

        # define gui elements
        text_header = tk.Label(self, text="Select a picture to classify",
                               fg="black", font="Arial 12 bold")

        dir_box = tk.Entry(self, textvariable=self.source_directory, text=self.source_directory,
                           width=40)
        button_browser_source = tk.Button(self, text="Browse",
                                          command=lambda: self.askFileDialog(self.source_directory))

        self.text_classification = tk.Label(self, text=self.labelText,
                                            fg="BLACK", font="Arial 12 bold")

        text_header.pack(anchor=N, pady=2)
        dir_box.pack(anchor=S, padx=3)
        button_browser_source.pack(anchor=S, padx=3)
        self.text_classification.pack(anchor=S, pady=2)

    def askFileDialog(self, dir):
        filename = tk.filedialog.askopenfile(parent=self, mode='rb', title='Choose a file').name
        dir.set(filename)
        if filename.endswith(".png"):
            self.labelText.set("Infected")
            predicted = predict_cell(filename)
            self.text_classification['text'] = predicted
            if predicted == "Parasitized":
                self.text_classification['fg'] = "RED"
            elif predicted == "Uninfected":
                self.text_classification['fg'] = "GREEN"

    def mainWindow(self):
        self.controller.show_frame("MainWindow")
