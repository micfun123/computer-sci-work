from tkinter import *

class Exchange(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.makeWidgets()

    def makeWidgets(self):
        Label(self, text="Enter amount in GBP:").pack(side=LEFT)
        self.gbp = Entry(self)
        self.gbp.pack(side=LEFT)
        Button(self, text="Convert", command=self.onPress).pack(side=LEFT)
        self.result = Label(self, text="Result")
        self.result.pack(side=LEFT)

    def onPress(self):
        gbp = float(self.gbp.get())
        eur = gbp * 1.17
        self.result.config(text="%.2f" % eur + " EUR")


if __name__ == '__main__': Exchange().mainloop()