from tkinter import Frame, Tk, BOTH, Text, Menu, END
from tkinter import filedialog
from tkinter import messagebox as mbox

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("File dialog")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menubar.add_cascade(label="File", menu=fileMenu)

    def onOpen(self):
        ftypes = [('Image', '*.png'), ('All files', '*')]
        dlg = filedialog.Open(self, filetypes=ftypes)
        fl = dlg.show()
        c, s = predict_cell(fl)
        root = Tk()
        T = Text(root, height=4, width=70)
        T.pack()
        T.insert(END, s)


def main():
    root = Tk()
    ex = Example()
    root.geometry("100x50+100+100")
    root.mainloop()


if __name__ == '__main__':
    main()