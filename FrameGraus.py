from tkinter import *


def transfor():
    if entrada1.get().replace('.', '', 1).isnumeric():
        tex4['text'] = float(entrada1.get()) * 1.8 + 32


graus = Tk()
graus.geometry('300x200+800+260')
graus.config(background='#ccffe6')
graus.bind('<Return>', lambda event: transfor())

fr1 = Frame(graus, bg='#ccffe6')
fr2 = Frame(graus, bg='#ccffe6', pady=20)
fr3 = Frame(graus, bg='#ccffe6')

entrada1 = Entry(fr2)
bot = Button(fr3, text='Converter', font='Arial 11', command=transfor)
tex1 = Label(fr1, text='Convertendo Valores', font='Arial 11', bg='#ccffe6')
tex2 = Label(fr2, text='Graus Celsius: ', font='Arial 11', bg='#ccffe6')
tex3 = Label(fr2, text='Graus Fahrenheit: ', font='Arial 11', bg='#ccffe6')
tex4 = Label(fr2, text='', font='Arial 11', bg='#ccffe6')

fr1.pack()
fr2.pack()
fr3.pack()

tex1.grid(row=0, column=0, columnspan=3)
tex2.grid(row=0, column=0)
entrada1.grid(row=0, column=2)
tex3.grid(row=2, column=0)
tex4.grid(row=2, column=2)
bot.grid(row=0, column=0, columnspan=3)

graus.mainloop()
