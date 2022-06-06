from tkinter import *


def imc1():
    tex6['text'] = 'Seu IMC é: '
    if entrada1.get().replace('.', '', 1).isnumeric() and entrada2.get().replace('.', '', 1).isnumeric():
        tex2['text'] = round(float(entrada1.get()) / float(entrada2.get()) ** 2, 1)
        if tex2['text'] < 18.5:
            tex7['text'] = 'Classificação:'
            tex3['text'] = 'Abaixo do peso.'
            tex3['bg'] = '#ffad33'
        elif 18.5 < tex2['text'] < 25:
            tex7['text'] = 'Classificação:'
            tex3['text'] = 'Peso ideal.'
            tex3['bg'] = '#66b3ff'
        elif 25 < tex2['text'] < 30:
            tex7['text'] = 'Classificação:'
            tex3['text'] = 'Acima do peso.'
            tex3['bg'] = '#5cd65c'
        elif 30 < tex2['text'] < 35:
            tex7['text'] = 'Classificação:'
            tex3['text'] = 'Obesidade Grau I.'
            tex3['bg'] = '#d9d926'
        elif 35 < tex2['text'] < 40:
            tex7['text'] = 'Classificação:'
            tex3['text'] = 'Obesidade Grau II.'
            tex3['bg'] = '#ff8533'
        elif tex2['text'] >= 40:
            tex7['text'] = 'Classificação:'
            tex3['text'] = 'Obesidade Grau III.'
            tex3['bg'] = '#ff4d4d'
        else:
            pass
    else:
        tex3['text'] = 'Valor invalido!'


imc = Tk()
imc.geometry('300x200+800+260')
imc.config(background='#e6ccff')
imc.bind('<Return>', lambda event: imc1())

fr1 = Frame(imc, bg='#e6ccff')
fr2 = Frame(imc, bg='#e6ccff', pady=10)
fr3 = Frame(imc, bg='#e6ccff')
entrada1 = Entry(fr2)
entrada2 = Entry(fr2)
bot = Button(fr3, text='Calcular', font='Arial 11', command=imc1, bg='#ffccdd')
tex1 = Label(fr1, text='Calculando IMC', font='Arial 11', bg='#e6ccff')
tex2 = Label(fr3, text='', font='Arial 11', bg='#e6ccff')
tex3 = Label(fr3, text='', font='Arial 11', bg='#e6ccff')
tex4 = Label(fr2, text='Peso:', font='Arial 11', bg='#e6ccff')
tex5 = Label(fr2, text='Altura:', font='Arial 11', bg='#e6ccff')
tex6 = Label(fr3, text='', font='Arial 11', bg='#e6ccff')
tex7 = Label(fr3, text='', font='Arial 11', bg='#e6ccff')

fr1.pack()
fr2.pack()
fr3.pack()

tex1.grid(row=0, column=0, columnspan=3)
tex4.grid(row=0, column=0)
tex5.grid(row=2, column=0)
entrada1.grid(row=0, column=2)
entrada2.grid(row=2, column=2)
bot.grid(row=0, column=0, columnspan=3)
tex6.grid(row=3, column=1)
tex2.grid(row=6, column=1)
tex7.grid(row=3, column=2)
tex3.grid(row=6, column=2)


imc.mainloop()
