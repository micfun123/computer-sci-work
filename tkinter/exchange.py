from tkinter import *
import requests

current_exchange_rate= {
    'EUR' : 1.17,
    'USD' : 1.31,
    'JPY' : 132.53,
    'AED' : 4.754,
    'AUD' : 1.77,
    'BGN' : 2.11,
}

url = "https://api.exchangerate.host/latest"
response = requests.get(url)
data = response.json()
Currecy = data["rates"]

class Exchange(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.makeWidgets()

        # Change the label text
    def show_drop(self):
        self.result.config(text=self.to_currency.get())
               


    def makeWidgets(self):
        Label(self, text="Enter amount in GBP:").pack(side=LEFT)
        self.gbp = Entry(self)
        self.to_currency = Entry(self)
        self.gbp.pack(side=LEFT)
        #show dropdown
        self.to_currency.pack(side=LEFT)
        self.to_currency.bind("<<ComboboxSelected>>", self.show_drop)
        Button(self, text="Convert", command=self.onPress).pack(side=LEFT)
        self.result = Label(self, text="Result")
        self.result.pack(side=LEFT)

    def onPress(self):
        gbp = float(self.gbp.get())
        result = gbp * Currecy[self.to_currency.get()]
        self.result.config(text="%.2f" % result + " "+  self.to_currency.get())


if __name__ == '__main__': Exchange().mainloop()