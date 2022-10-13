#Feito por Joao Gabriel

from tkinter import Button
import tkinter as tk
from random import randint
from threading import Timer

root = tk.Tk()
root.geometry('500x300')
root.resizable(False, False)
root.title('Jogo Da Velha')

ptsx = 0
ptso = 0
vencedor = ''

v = randint(1, 2)
if v == 1:
    vez = 'X'
else:
    vez = 'O'

def ab():
    inf = tk.Tk()
    inf.title('About')
    inf.geometry('250x300')
    madeby = tk.Label(inf, text= 'Feito por: Joao Gabriel\n(JoNeoX)', font= ('Arial', 15))
    madeby.place(x= 10, y= 10)
    madew = tk.Label(inf, text= 'Feito com Python e Tkinter', font= ('Arial', 13))
    madew.place(x= 20, y=230)
    version = tk.Label(inf, text= 'Versão: 1.0')
    version.place(x= 180, y= 270)
    closebutton = Button(inf, bd= 3, text= 'Fechar', command= lambda: inf.destroy(), font=('Arial', 10))
    closebutton.place(x= 90, y= 260)

def aguarda():
    switch()
    def timeout():
        switch()
        restartgame()
    t = Timer(2, timeout)
    t.start()

def switch():
    global botao1, botao2, botao3, botao4, botao5, botao6, botao7, botao8, botao9

    if botao1['state'] == 'normal':
        botao1['state'] = 'disable'
    else:
        botao1['state'] = 'normal'

    if botao2['state'] == 'normal':
        botao2['state'] = 'disable'
    else:
        botao2['state'] = 'normal'

    if botao3['state'] == 'normal':
        botao3['state'] = 'disable'
    else:
        botao3['state'] = 'normal'

    if botao4['state'] == 'normal':
        botao4['state'] = 'disable'
    else:
        botao4['state'] = 'normal'

    if botao5['state'] == 'normal':
        botao5['state'] = 'disable'
    else:
        botao5['state'] = 'normal'

    if botao6['state'] == 'normal':
        botao6['state'] = 'disable'
    else:
        botao6['state'] = 'normal'

    if botao7['state'] == 'normal':
        botao7['state'] = 'disable'
    else:
        botao7['state'] = 'normal'

    if botao8['state'] == 'normal':
        botao8['state'] = 'disable'
    else:
        botao8['state'] = 'normal'

    if botao9['state'] == 'normal':
        botao9['state'] = 'disable'
    else:
        botao9['state'] = 'normal'



def restartpts():
    global ptsx, ptso
    ptsx = 0
    ptso = 0
    mostrax.config(text= f'Pontos X: {ptsx}')
    mostrao.config(text= f'Pontos O: {ptso}')

def restartgame():
    global vez, vencedor, linha1, linha2, linha3
    vencedor = ''
    v = randint(1, 2)
    if v == 1:
        vez = 'X'
    else:
        vez = 'O'
    linha1 = [' ', ' ', ' ']
    linha2 = [' ', ' ', ' ']
    linha3 = [' ', ' ', ' ']

    botao1.config(text = linha1[0])
    botao2.config(text = linha1[1])
    botao3.config(text = linha1[2])
    botao4.config(text = linha2[0])
    botao5.config(text = linha2[1])
    botao6.config(text = linha2[2])
    botao7.config(text = linha3[0])
    botao8.config(text = linha3[1])
    botao9.config(text = linha3[2])
    mostravencedor.config(text = f'Vencedor: {vencedor}')
    mostravez.config(text = vez)
    

def quemganhou():
    # X
    global vencedor, ptso, ptsx
    # Horizontais
    if linha1[0] == 'X' and linha1[1] == 'X' and linha1[2] == 'X':

        mostrax.config(text= f'Pontos X: {ptsx}')
        return 'X'
    elif linha2[0] == 'X' and linha2[1] == 'X' and linha2[2] == 'X':
        
        mostrax.config(text= f'Pontos X: {ptsx}')
        return 'X'
    elif linha3[0] == 'X' and linha3[1] == 'X' and linha3[2] == 'X':
        
        mostrax.config(text= f'Pontos X: {ptsx}')
        return 'X'

    #Verticais
    elif linha1[0] == 'X' and linha2[0] == 'X' and linha3[0] == 'X':
        
        mostrax.config(text= f'Pontos X: {ptsx}')
        return 'X'
    elif linha1[1] == 'X' and linha2[1] == 'X' and linha3[1] == 'X':
        
        mostrax.config(text= f'Pontos X: {ptsx}')
        return 'X'
    elif linha1[2] == 'X' and linha2[2] == 'X' and linha3[2] == 'X':
        
        mostrax.config(text= f'Pontos X: {ptsx}')
        return 'X'
    
    #Diagonais
    elif linha1[0] == 'X' and linha2[1] == 'X' and linha3[2] == 'X':
        
        mostrax.config(text= f'Pontos X: {ptsx}')
        return 'X'
    elif linha3[0] == 'X' and linha2[1] == 'X' and linha1[2] == 'X':
        
        mostrax.config(text= f'Pontos X: {ptsx}')
        return 'X'
    
   # O
   # Horizontais
    elif linha1[0] == 'O' and linha1[1] == 'O' and linha1[2] == 'O':
        
        mostrao.config(text= f'Pontos O: {ptso}')
        return 'O'
    elif linha2[0] == 'O' and linha2[1] == 'O' and linha2[2] == 'O':
        
        mostrao.config(text= f'Pontos O: {ptso}')
        return 'O'
    elif linha3[0] == 'O' and linha3[1] == 'O' and linha3[2] == 'O':
        
        mostrao.config(text= f'Pontos O: {ptso}')
        return 'O'

    #Verticais
    elif linha1[0] == 'O' and linha2[0] == 'O' and linha3[0] == 'O':
        
        mostrao.config(text= f'Pontos O: {ptso}')
        return 'O'
    elif linha1[1] == 'O' and linha2[1] == 'O' and linha3[1] == 'O':
        
        mostrao.config(text= f'Pontos O: {ptso}')
        return 'O'
    elif linha1[2] == 'O' and linha2[2] == 'O' and linha3[2] == 'O':
        
        mostrao.config(text= f'Pontos O: {ptso}')
        return 'O'
    
    #Diagonais
    elif linha1[0] == 'O' and linha2[1] == 'O' and linha3[2] == 'O':
        
        mostrao.config(text= f'Pontos O: {ptso}')
        return 'O'
    elif linha3[0] == 'O' and linha2[1] == 'O' and linha1[2] == 'O' == 'O':
        
        mostrao.config(text= f'Pontos O: {ptso}')
        return 'O'

    # Velha
    else:
        return 'V'

def trocavez1():
    global vencedor, vez, ptsx, ptso
    if linha1[0] == ' ':
        botao1.config(text=vez)
        linha1[0] = vez
        if vez == 'X':
            vez = 'O'
        elif vez == 'O':
            vez = 'X'
        mostravez.config(text= vez)
    if quemganhou() == 'X':
        vencedor = 'X'
        ptsx += 1
        mostrax.config(text = f'Pontos X: {ptsx}')
        aguarda()
    if quemganhou() == 'O':
        vencedor = 'O'
        ptso += 1 
        mostrao.config(text = f'Pontos O: {ptso}')
        aguarda()
    mostravencedor.config(text= f'Vencedor: {vencedor}')

def trocavez2():
    global vencedor, vez, ptsx, ptso
    if linha1[1] == ' ':
        botao2.config(text=vez)
        linha1[1] = vez
        if vez == 'X':
            vez = 'O'
        elif vez == 'O':
            vez = 'X'
        mostravez.config(text= vez)
    if quemganhou() == 'X':
        vencedor = 'X'
        ptsx += 1
        mostrax.config(text = f'Pontos X: {ptsx}')
        aguarda()
    if quemganhou() == 'O':
        vencedor = 'O'
        ptso += 1
        mostrao.config(text = f'Pontos O: {ptso}')
        aguarda()
    mostravencedor.config(text= f'Vencedor: {vencedor}')

def trocavez3():
    global vencedor, vez, ptsx, ptso
    if linha1[2] == ' ':
        botao3.config(text=vez)
        linha1[2] = vez
        if vez == 'X':
            vez = 'O'
        elif vez == 'O':
            vez = 'X'
        mostravez.config(text= vez)
    if quemganhou() == 'X':
        vencedor = 'X'
        ptsx += 1
        mostrax.config(text = f'Pontos X: {ptsx}')
        aguarda()
    if quemganhou() == 'O':
        vencedor = 'O'
        ptso += 1
        mostrao.config(text = f'Pontos O: {ptso}')
        aguarda()
    mostravencedor.config(text= f'Vencedor: {vencedor}')

def trocavez4():
    global vencedor, vez, ptsx, ptso
    if linha2[0] == ' ':
        botao4.config(text=vez)
        linha2[0] = vez
        if vez == 'X':
            vez = 'O'
        elif vez == 'O':
            vez = 'X'
        mostravez.config(text= vez)
    if quemganhou() == 'X':
        vencedor = 'X'
        ptsx += 1
        mostrax.config(text = f'Pontos X: {ptsx}')
        aguarda()
    if quemganhou() == 'O':
        vencedor = 'O'
        ptso += 1
        mostrao.config(text = f'Pontos O: {ptso}')
        aguarda()
    mostravencedor.config(text= f'Vencedor: {vencedor}')

def trocavez5():
    global vencedor, vez, ptsx, ptso
    if linha2[1] == ' ':
        botao5.config(text=vez)
        linha2[1] = vez
        if vez == 'X':
            vez = 'O'
        elif vez == 'O':
            vez = 'X'
        mostravez.config(text= vez)
    if quemganhou() == 'X':
        vencedor = 'X'
        ptsx += 1
        mostrax.config(text = f'Pontos X: {ptsx}')
        aguarda()
    if quemganhou() == 'O':
        vencedor = 'O'
        ptso += 1
        mostrao.config(text = f'Pontos O: {ptso}')
        aguarda()
    mostravencedor.config(text= f'Vencedor: {vencedor}')

def trocavez6():
    global vencedor, vez, ptsx, ptso
    if linha2[2] == ' ':
        botao6.config(text=vez)
        linha2[2] = vez
        if vez == 'X':
            vez = 'O'
        elif vez == 'O':
            vez = 'X'
        mostravez.config(text= vez)
    if quemganhou() == 'X':
        vencedor = 'X'
        ptsx += 1
        mostrax.config(text = f'Pontos X: {ptsx}')
        aguarda()
    if quemganhou() == 'O':
        vencedor = 'O'
        ptso += 1
        mostrao.config(text = f'Pontos O: {ptso}')
        aguarda()
    mostravencedor.config(text= f'Vencedor: {vencedor}')

def trocavez7():
    global vencedor, vez, ptsx, ptso
    if linha3[0] == ' ':
        botao7.config(text=vez)
        linha3[0] = vez
        if vez == 'X':
            vez = 'O'
        elif vez == 'O':
            vez = 'X'
        mostravez.config(text= vez)
    if quemganhou() == 'X':
        vencedor = 'X'
        ptsx += 1
        mostrax.config(text = f'Pontos X: {ptsx}')
        aguarda()
    if quemganhou() == 'O':
        vencedor = 'O'
        ptso += 1
        mostrao.config(text = f'Pontos O: {ptso}')
        aguarda()
    mostravencedor.config(text= f'Vencedor: {vencedor}')

def trocavez8():
    global vencedor, vez, ptsx, ptso
    if linha3[1] == ' ':
        botao8.config(text=vez)
        linha3[1] = vez
        if vez == 'X':
            vez = 'O'
        elif vez == 'O':
            vez = 'X'
        mostravez.config(text= vez)
    if quemganhou() == 'X':
        vencedor = 'X'
        ptsx += 1
        mostrax.config(text = f'Pontos X: {ptsx}')
        aguarda()
    if quemganhou() == 'O':
        vencedor = 'O'
        ptso += 1
        mostrao.config(text = f'Pontos O: {ptso}')
        aguarda()
    mostravencedor.config(text= f'Vencedor: {vencedor}')

def trocavez9():
    global vencedor, vez, ptsx, ptso
    if linha3[2] == ' ':
        botao9.config(text=vez)
        linha3[2] = vez
        if vez == 'X':
            vez = 'O'
        elif vez == 'O':
            vez = 'X'
        mostravez.config(text= vez)
    if quemganhou() == 'X':
        vencedor = 'X'
        ptsx += 1
        mostrax.config(text = f'Pontos X: {ptsx}')
        aguarda()
        
    if quemganhou() == 'O':
        vencedor = 'O'
        ptso += 1
        mostrao.config(text = f'Pontos O: {ptso}')
        aguarda()
    mostravencedor.config(text= f'Vencedor: {vencedor}')

linha1 = [' ', ' ', ' ']
linha2 = [' ', ' ', ' ']
linha3 = [' ', ' ', ' ']

#GUI
botao1 = Button(root, bd= 3, text= linha1[0], command= trocavez1, font=('Arial', 25))
botao2 = Button(root, bd= 3, text= linha1[1], command= trocavez2, font=('Arial', 25))
botao3 = Button(root, bd= 3, text= linha1[2], command= trocavez3, font=('Arial', 25))
botao4 = Button(root, bd= 3, text= linha2[0], command= trocavez4, font=('Arial', 25))
botao5 = Button(root, bd= 3, text= linha2[1], command= trocavez5, font=('Arial', 25))
botao6 = Button(root, bd= 3, text= linha2[2], command= trocavez6, font=('Arial', 25))
botao7 = Button(root, bd= 3, text= linha3[0], command= trocavez7, font=('Arial', 25))
botao8 = Button(root, bd= 3, text= linha3[1], command= trocavez8, font=('Arial', 25))
botao9 = Button(root, bd= 3, text= linha3[2], command= trocavez9, font=('Arial', 25))
restgame = Button(root, bd= 3, text= 'Restart\nTabuleiro', command= restartgame, font=('Arial', 10))
restpts = Button(root, bd= 3, text= 'Restart\nPontuação', command= restartpts, font=('Arial', 10))
mostrax = tk.Label(root, text=f'Pontos X: {ptsx}', font=('Arial', 15))
mostrao = tk.Label(root, text=f'Pontos O: {ptso}', font=('Arial', 15))
mostravez = tk.Label(root, text= vez, font=('Arial', 20))
mostravencedor = tk.Label(root, text= vencedor, font=('Arial', 13))
infobutton = Button(root, bd= 3, text= 'About', command=ab, font=('Arial', 10))
closebutton = Button(root, bd= 3, text= 'Fechar', command= lambda: root.destroy(), font=('Arial', 10))

botao1.place(x= 0, y=0, width=100, height=100)
botao2.place(x= 100, y=0, width=100, height=100)
botao3.place(x= 200, y=0, width=100, height=100)
botao4.place(x= 0, y=100, width=100, height=100)
botao5.place(x= 100, y=100, width=100, height=100)
botao6.place(x= 200, y=100, width=100, height=100)
botao7.place(x= 0, y=200, width=100, height=100)
botao8.place(x= 100, y=200, width=100, height=100)
botao9.place(x= 200, y=200, width=100, height=100)
mostrax.place(x= 310, y=10)
mostrao.place(x= 310, y= 40)
restgame.place(x= 310, y= 230)
restpts.place(x= 310, y= 180)
infobutton.place(x= 453, y= 270)
closebutton.place(x= 390, y= 270)

mostravez.place(x= 300, y= 65, width=80, height=80)
mostravencedor.place(x= 300, y= 130)

root.mainloop()