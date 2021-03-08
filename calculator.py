from tkinter import *

#Configuração do tkinter
cal=Tk()
cal.title('Calculadora') #Título

cal['bg'] = 'black' #Cor de fundo

#visor

e = Entry(cal, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10) #grid de alocação

#Funções de execução

def click(numero): #Função clicar em numeros e no ponto
    casa = e.get() #Pega o numero do visor e armazena na função casa
    e.delete(0, END) #Deleta do visor, para evitar repetição
    e.insert(0, str(casa) + str(numero)) #Concatena ultimo número digitado com o primeiro numero já armazenado na variavel casa e insere no visor

def clear(): #Função limpar/clear
    e.delete(0, END)

def soma(): #Função somar
    num_1 = e.get() #pega variavel do visor e armazena na função num_1
    global f_num #transforma a variavel f_num em global
    global op #cria uma variavel op -operação- para o if statement do função 'igual'
    op = 'soma'
    f_num = float(num_1) #armazena a variavel num_1 no tipo float na variavel global f_num
    e.delete(0, END) #limpa o visor

def sub(): #Função Subtrair
    num_1 = e.get()
    global f_num
    global op
    op = 'sub'
    f_num = float(num_1)
    e.delete(0, END)

def mult():
    num_1 = e.get()
    global f_num
    global op
    op = 'mult'
    f_num = float(num_1)
    e.delete(0, END)

def div():
    num_1 = e.get()
    global f_num
    global op
    op = 'div'
    f_num = float(num_1)
    e.delete(0, END)

def iqual():
    num_2 = e.get()
    e.delete(0, END)

    if op == 'soma':
        e.insert(0, f_num + float(num_2))
    elif op == 'sub':
        e.insert(0, f_num - float(num_2))
    elif op == 'mult':
        e.insert(0, f_num * float(num_2))
    elif op == 'div':
        e.insert(0, f_num / float(num_2))

#Funções MS

def bms(): #Função armazenamento variavel ms
    global ms #cria a variavel global ms
    ms = e.get() #variavel ms recebe valor do visor

def msp(): #Função soma da variavel ms
    num_1 = e.get() #variavel num_1 recebe o valor do visor
    e.delete(0, END) #valor do visor é deletado
    e.insert(0, float(ms) + float(num_1)) #insere no visor a soma da variavel ms + num_1

def msm():
    num_1 = e.get() #variavel num_1 recebe o valor do visor
    e.delete(0, END) #valor do visor é deletado
    e.insert(0, float(num_1) - float(ms)) #insere no visor a variavel num_1 - a variavel armazenada ms
  
#Definir Botões

btn_1 = Button(text='1', padx= 30, pady=20, bg="white", command= lambda: click(1))
btn_2 = Button(text='2', padx= 30, pady=20, bg="white", command= lambda: click(2))
btn_3 = Button(text='3', padx= 30, pady=20, bg="white", command= lambda: click(3))
btn_4 = Button(text='4', padx= 30, pady=20, bg="white", command= lambda: click(4))
btn_5 = Button(text='5', padx= 30, pady=20, bg="white", command= lambda: click(5))
btn_6 = Button(text='6', padx= 30, pady=20, bg="white", command= lambda: click(6))
btn_7 = Button(text='7', padx= 30, pady=20, bg="white", command= lambda: click(7))
btn_8 = Button(text='8', padx= 30, pady=20, bg="white", command= lambda: click(8))
btn_9 = Button(text='9', padx= 30, pady=20, bg="white", command= lambda: click(9))
btn_0 = Button(text='0', padx= 30, pady=20, bg="white", command= lambda: click(0))

#Definir Botões de Operações

btn_a = Button(text='+', padx= 30, pady=20, bg="white", command= soma)
btn_m = Button(text='-', padx= 30, pady=20, bg="white", command= sub)
btn_x = Button(text='*', padx= 30, pady=20, bg="white", command= mult)
btn_d = Button(text='/', padx= 30, pady=20, bg="white", command= div)
btn_i = Button(text='=', padx= 30, pady=20, bg="white", command= iqual)
btn_c = Button(text='C', padx= 30, pady=20, bg="white", command= clear)
btn_p = Button(text='.', padx= 30, pady=20, bg="white", command= lambda: click('.'))
btn_ms = Button(text='MS', padx= 26, pady=20, bg="white", command= bms)
btn_msp = Button(text='+MS', padx= 23, pady=20, bg="white", command= msp)
btn_msm = Button(text='-MS', padx= 23, pady=20, bg="white", command= msm)

#Grid dos Botões

btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)

btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)

btn_0.grid(row=4, column=1)

#Grid dos Botões Operações

btn_a.grid(row=1, column=3)
btn_m.grid(row=2, column=3)
btn_x.grid(row=3, column=3)
btn_d.grid(row=4, column=3)
btn_i.grid(row=5, column=3)

btn_c.grid(row=4, column=2)
btn_p.grid(row=4, column=0)

btn_ms.grid(row=5, column=0)
btn_msp.grid(row=5, column=1)
btn_msm.grid(row=5, column=2)


cal.mainloop() #função de loop