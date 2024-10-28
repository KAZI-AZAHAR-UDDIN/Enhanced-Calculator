from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Enhanced Calculator")
        master.geometry('357x490+0+0')  # Adjusted height for better layout
        master.config(bg='#222')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''

        # Entry field with improved styling
        Entry(master, width=17, font=('Arial', 24), textvariable=self.equation, bg='#fff', bd=10, relief='flat', justify='right').place(x=10, y=10)

        # Define button configurations with consistent size and layout
        buttons = [
            ('(', 10, 80), (')', 95, 80), ('%', 180, 80), ('/', 265, 80),
            ('7', 10, 160), ('8', 95, 160), ('9', 180, 160), ('x', 265, 160),
            ('4', 10, 240), ('5', 95, 240), ('6', 180, 240), ('-', 265, 240),
            ('1', 10, 320), ('2', 95, 320), ('3', 180, 320), ('+', 265, 320),
            ('C', 10, 400), ('0', 95, 400), ('.', 180, 400), ('=', 265, 400),
        ]

        # Create buttons with updated style
        for (text, x, y) in buttons:
            if text == '=':
                Button(master, text=text, width=8, height=3, bg='#4CAF50', fg='white', font=('Arial', 12, 'bold'),
                       command=self.solve).place(x=x, y=y)
            elif text == 'C':
                Button(master, text=text, width=8, height=3, bg='#f44336', fg='white', font=('Arial', 12, 'bold'),
                       command=self.clear).place(x=x, y=y)
            else:
                Button(master, text=text, width=8, height=3, bg='#333', fg='white', font=('Arial', 12, 'bold'),
                       command=lambda txt=text: self.show(txt)).place(x=x, y=y)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value.replace('x', '*'))
            self.equation.set(result)
            self.entry_value = str(result)
        except:
            self.equation.set("Error")
            self.entry_value = ''

root = Tk()
Calculator(root)
root.mainloop()
