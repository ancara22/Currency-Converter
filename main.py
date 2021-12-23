from tkinter import *  # import whole module


class CurrencyConverter:                    # Create class
    def __init__(self):                     # Spe ial method in Python class
        window = Tk()                       # Create application window
        window.title("Currency Converter")  # Add title to application window
        window.configure(bg="gray")        # Add background color to application window

        # Adding Label widgets to application window
        Label(window, font="Helvetica 12 bold", bg="gray", text="Amount to convert")\
            .grid(row=1, column=1, padx=25, pady=10,  sticky=W)
        Label(window, font="Helvetica 12 bold", bg="gray", text="Conversion Rate")\
            .grid(row=2, column=1, padx=25, pady=10, sticky=W)
        Label(window, font="Helvetica 12 bold", bg="gray", text="Converted Amount")\
            .grid(row=3, column=1, padx=25, pady=10, sticky=W)

        # Create object and add entry functions
        self.amountToConvertVar = StringVar()
        Entry(window, textvariable=self.amountToConvertVar, justify=RIGHT).grid(row=1, column=2)
        self.amountToRateVar = StringVar()
        Entry(window, textvariable=self.amountToRateVar, justify=RIGHT).grid(row=2, column=2)
        self.convertedAmountVar = StringVar()
        Label(window, font="Helvetica 12 bold", bg="gray", textvariable=self.convertedAmountVar)\
            .grid(row=3, column=2, sticky=E)

        # Create convert and clear buttons. When clicked they will call their respective functions.
        Button(window, text="Convert", font="Helvetica 12 bold", bg="blue", fg="black", command=self.converted_amount)\
            .grid(row=4, column=2, sticky=E)
        Button(window, text="Clear", font="Helvetica 12 bold", bg="red", fg="gray", command=self.delete_all)\
            .grid(row=4, column=6, padx=25, pady=25, sticky=E)

        window.mainloop()

    def converted_amount(self):
        amt = float(self.amountToRateVar.get())
        convertedAmountVar = float(self.amountToConvertVar.get()) * amt
        self.convertedAmountVar.set(format(convertedAmountVar, "10.2f"))

    def delete_all(self):
        self.convertedAmountVar.set("")
        self.amountToConvertVar.set("")
        self.amountToRateVar.set("")


CurrencyConverter()

