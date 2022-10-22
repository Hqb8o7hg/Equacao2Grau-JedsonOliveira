import tkinter

janela = tkinter.Tk()
janela.title('Calcula Equação do segundo grau')
janela.geometry('500x100-500-500')


def equacao_2_grau(A, B, C):
    delta = float((B ** 2) - 4 * A * C)

    if A > 0:
        if delta > 0:
            x1 = float((-B + delta ** (1 / 2)) / (2 * A))
            x2 = float((-B - delta ** (1 / 2)) / (2 * A))

            return mostra_resultado(f'Para X1 = {x1} \n\n||\n\n Para X2 = {x2}')
        elif delta == 0:
            x3 = float((-B + delta ** (1 / 2)) / (2 * A))
            return mostra_resultado(f'A equação possui \napenas uma raiz que eh: \n{x3}')
        else:
            return mostra_resultado(f'Para Delta: {delta}, \nnão há raizes reais.')
    else:
        return mostra_resultado(f'O valor do coeficiente "A" \ndeve ser positivo.')


def mostra_resultado(mensagem):
    janela_msg = tkinter.Toplevel()
    janela_msg.title('Resultado')
    janela_msg.geometry('400x300')

    tkinter.Label(janela_msg, text=mensagem, font='arial 12 bold', pady=30).pack()

    tkinter.Button(janela_msg, text='OK', command=janela_msg.destroy).pack()


quadro = tkinter.Frame(janela, bd=35)
quadro.pack()

coeficiente_a_texto = tkinter.Label(quadro, text='Insira os Coeficientes    >>>    a: ', font='arial 12 bold')
coeficiente_a_texto.pack(side='left')
coeficiente_a_quadro = tkinter.Entry(quadro, font='arial 12', width=3)
coeficiente_a_quadro.pack(side='left')

coeficiente_b_texto = tkinter.Label(quadro, text='b: ', font='arial 12 bold')
coeficiente_b_texto.pack(side='left')
coeficiente_b_quadro = tkinter.Entry(quadro, font='arial 12', width=3)
coeficiente_b_quadro.pack(side='left')

coeficiente_c_texto = tkinter.Label(quadro, text='c: ', font='arial 12 bold')
coeficiente_c_texto.pack(side='left')
coeficiente_c_quadro = tkinter.Entry(quadro, font='arial 12', width=3)
coeficiente_c_quadro.pack(side='left')

tkinter.Button(quadro, bg='red', text='>>>', bd=3, width=3, height=2,
               command=lambda: equacao_2_grau(float(coeficiente_a_quadro.get()), float(coeficiente_b_quadro.get()),
                                              float(coeficiente_c_quadro.get()))).pack(side='left')

janela.mainloop()
