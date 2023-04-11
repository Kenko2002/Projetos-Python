from tkinter import *

def jogar(botao, jogA, jogB, simbA, simbB, lista, contador, vencedor):
	if vencedor["text"] == "Vez: " + jogA.get() or vencedor["text"] == "Vez: " + jogB.get():
		if (botao["text"] != simbA.get()) and (botao["text"] != simbB.get()):
			cont = int(contador["text"])
			if cont % 2 == 0:
				texto = simbA.get()
				vencedor["text"] = "Vez: " + jogB.get()
			else:
				texto = simbB.get()
				vencedor["text"] = "Vez: " + jogA.get()
			botao["text"] = texto
			cont += 1
			contador["text"] = str(cont)
		venceu(lista, contador, botao, vencedor, jogA, jogB, simbA, simbB)

def venceu(lista, contador, botao, vencedor, jogA, jogB, simbA, simbB):
	if lista[0]["text"] == lista[1]["text"] == lista[2]["text"] == simbA.get():
		contador["text"] = "0"
		vencedor["text"] = jogA.get() + " ganhou a partida!!! Clique em NOVO JOGO"
		lista[0]["bg"] = "Green"
		lista[1]["bg"] = "Green"
		lista[2]["bg"] = "Green"



	elif lista[0]["text"] == lista[3]["text"] == lista[6]["text"] == simbA.get():
		contador["text"] = "0"
		vencedor["text"] = jogA.get() + " ganhou a partida!!! Clique em NOVO JOGO"
		lista[0]["bg"] = "Green"
		lista[3]["bg"] = "Green"
		lista[6]["bg"] = "Green"



	elif lista[3]["text"] == lista[4]["text"] == lista[5]["text"] == simbA.get():
		contador["text"] = "0"
		vencedor["text"] = jogA.get() + " ganhou a partida!!! Clique em NOVO JOGO"
		lista[3]["bg"] = "Green"
		lista[4]["bg"] = "Green"
		lista[5]["bg"] = "Green"



	elif lista[6]["text"] == lista[7]["text"] == lista[8]["text"] == simbA.get():
		contador["text"] = "0"
		vencedor["text"] = jogA.get() + " ganhou a partida!!! Clique em NOVO JOGO"
		lista[6]["bg"] = "Green"
		lista[7]["bg"] = "Green"
		lista[8]["bg"] = "Green"



	elif lista[1]["text"] == lista[4]["text"] == lista[7]["text"] == simbA.get():
		contador["text"] = "0"
		vencedor["text"] = jogA.get() + " ganhou a partida!!! Clique em NOVO JOGO"
		lista[1]["bg"] = "Green"
		lista[4]["bg"] = "Green"
		lista[7]["bg"] = "Green"



	elif lista[2]["text"] == lista[5]["text"] == lista[8]["text"] == simbA.get():
		contador["text"] = "0"
		vencedor["text"] = jogA.get() + " ganhou a partida!!! Clique em NOVO JOGO"
		lista[2]["bg"] = "Green"
		lista[5]["bg"] = "Green"
		lista[8]["bg"] = "Green"



	elif lista[0]["text"] == lista[4]["text"] == lista[8]["text"] == simbA.get():
		contador["text"] = "0"
		vencedor["text"] = jogA.get() + " ganhou a partida!!! Clique em NOVO JOGO"
		lista[0]["bg"] = "Green"
		lista[4]["bg"] = "Green"
		lista[8]["bg"] = "Green"



	elif lista[2]["text"] == lista[4]["text"] == lista[6]["text"] == simbA.get():
		contador["text"] = "0"
		vencedor["text"] = jogA.get() + " ganhou a partida!!! Clique em NOVO JOGO"
		lista[2]["bg"] = "Green"
		lista[4]["bg"] = "Green"
		lista[6]["bg"] = "Green"



	elif lista[0]["text"] == lista[1]["text"] == lista[2]["text"] == simbB.get():
		contador["text"] = "0"
		vencedor["text"] = jogB.get() + " ganhou a partida!!! Clique em NOVO JOGO"
		lista[0]["bg"] = "Green"
		lista[1]["bg"] = "Green"
		lista[2]["bg"] = "Green"



	elif lista[0]["text"] == lista[3]["text"] == lista[6]["text"] == simbB.get():
		contador["text"] = "0"
		vencedor["text"] = jogB.get() + " ganhou a partida!!! Clique em NOVO JOGO"
		lista[0]["bg"] = "Green"
		lista[3]["bg"] = "Green"
		lista[6]["bg"] = "Green"



	elif lista[3]["text"] == lista[4]["text"] == lista[5]["text"] == simbB.get():
		contador["text"] = "0"
		vencedor["text"] = jogB.get() + " ganhou a partida!!! Clique em NOVO JOGO"
		lista[3]["bg"] = "Green"
		lista[4]["bg"] = "Green"
		lista[5]["bg"] = "Green"



	elif lista[6]["text"] == lista[7]["text"] == lista[8]["text"] == simbB.get():
		contador["text"] = "0"
		vencedor["text"] = jogB.get() + " ganhou a partida!!! Clique em NOVO JOGO"
		lista[6]["bg"] = "Green"
		lista[7]["bg"] = "Green"
		lista[8]["bg"] = "Green"



	elif lista[1]["text"] == lista[4]["text"] == lista[7]["text"] == simbB.get():
		contador["text"] = "0"
		vencedor["text"] = jogB.get() + " ganhou a partida!!! Clique em NOVO JOGO"
		lista[1]["bg"] = "Green"
		lista[4]["bg"] = "Green"
		lista[7]["bg"] = "Green"



	elif lista[2]["text"] == lista[5]["text"] == lista[8]["text"] == simbB.get():
		contador["text"] = "0"
		vencedor["text"] = jogB.get() + " ganhou a partida!!! Clique em NOVO JOGO"
		lista[2]["bg"] = "Green"
		lista[5]["bg"] = "Green"
		lista[8]["bg"] = "Green"



	elif lista[0]["text"] == lista[4]["text"] == lista[8]["text"] == simbB.get():
		contador["text"] = "0"
		vencedor["text"] = jogB.get() + " ganhou a partida!!! Clique em NOVO JOGO"
		lista[0]["bg"] = "Green"
		lista[4]["bg"] = "Green"
		lista[8]["bg"] = "Green"



	elif lista[2]["text"] == lista[4]["text"] == lista[6]["text"] == simbB.get():
		contador["text"] = "0"
		vencedor["text"] = jogB.get() + " ganhou a partida!!! Clique em NOVO JOGO"
		lista[2]["bg"] = "Green"
		lista[4]["bg"] = "Green"
		lista[6]["bg"] = "Green"



	elif int(contador["text"]) == 9:
		vencedor["text"] = "Deu velha!!! Clique em NOVO JOGO"

def iniciar(nomeJogA, nomeJogB, simbA, simbB, vencedor, lista):
	ok = True
	if (permissaoPComecar(nomeJogA, nomeJogB, simbA, simbB)):
		for b in lista:
			if b["text"] != "":
				ok = False
		if ok:
			vencedor["text"] = "Vez: " + nomeJogA.get()

def permissaoPComecar(nomeJogA, nomeJogB, simbA, simbB):
	if (nomeJogA.get() != "") and (nomeJogB.get() != "") and (simbA.get() != "") and (simbB.get() != ""):
		return True

def restart(lista, contador, vencedor, jogA):
	for b in lista:
		b["text"] = ""
	contador["text"] = "0"
	vencedor["text"] = "Vez: " + jogA.get()

def sair():
	quit()




def main(args):
	raiz =  Tk()

	raiz.geometry("400x400")

	font = ('Ruda','10', 'bold')
	
	frame5= Frame(raiz)
	frame5.pack()
	
	frame6= Frame(raiz)
	frame6.pack()

	frameSeparador = Frame(raiz, height = 7)
	frameSeparador.pack()
	
	frame2= Frame(raiz)
	frame2.pack()
	
	frame3= Frame(raiz)
	frame3.pack()
	
	frame4= Frame(raiz)
	frame4.pack()

	frame8= Frame(raiz, height = 20)
	frame8.pack()
	
	frame7= Frame(raiz, height = 50)
	frame7.pack()

	frame9= Frame(raiz, height = 50)
	frame9.pack()

	vencedor = Label(frame9, text = "Preencha os campos acima e aperte Iniciar para começar o jogo", font = ('Ruda','9', 'bold'))
	vencedor.pack()

	Label(frame5, text='Jogador 1: ', font= font, width = 8).pack(side=LEFT)
	nomeJogA = Entry (frame5, width = 10, font = font)
	nomeJogA.focus_force()
	nomeJogA.pack(side=LEFT)
	
	Label(frame5, text='Simbolo: ', font= font, width = 8).pack(side=LEFT)
	simbJogA = Entry (frame5, width = 10, font = font)
	simbJogA.focus_force()
	simbJogA.pack(side=LEFT)
	
	Label(frame6, text='Jogador 2: ', font= font, width = 8).pack(side=LEFT)
	nomeJogB = Entry (frame6, width = 10, font = font)
	nomeJogB.focus_force()
	nomeJogB.pack(side=LEFT)
	
	Label(frame6, text='Simbolo: ', font= font, width = 8).pack(side=LEFT)
	simbJogB = Entry (frame6, width = 10, font = font)
	simbJogB.focus_force()
	simbJogB.pack(side=LEFT)
	

	b01= Button(frame2, width = 3)
	b01['padx'],b01['pady'] = 25, 25
	b01['bg']='pink'
	
	b02= Button(frame2, width = 3)
	b02['padx'],b02['pady'] = 25, 25
	b02['bg']='pink'
	
	b03= Button(frame2, width = 3)
	b03['padx'],b03['pady'] = 25, 25
	b03['bg']='pink'
	
	b04= Button(frame3, width = 3)
	b04['padx'],b04['pady'] = 25, 25
	b04['bg']='pink'
	
	b05= Button(frame3, width = 3)
	b05['padx'],b05['pady'] = 25, 25
	b05['bg']='pink'
	
	b06= Button(frame3, width = 3)
	b06['padx'],b06['pady'] = 25, 25
	b06['bg']='pink'
	
	b07= Button(frame4, width = 3)
	b07['padx'],b07['pady'] = 25, 25
	b07['bg']='pink'
	
	b08= Button(frame4, width = 3)
	b08['padx'],b08['pady'] = 25, 25
	b08['bg']='pink'
	
	b09= Button(frame4, width = 3)
	b09['padx'],b09['pady'] = 25, 25
	b09['bg']='pink'


	
	b10= Button(frame7, text = "Iniciar")
	b10['padx'],b10['pady'] = 35, 5
	b10['bg']='blue'
	
	b11= Button(frame7, text = "Novo")
	b11['padx'],b11['pady'] = 35, 5
	b11['bg']='blue'
	
	b12= Button(frame7, text = "Sair", command = sair)
	b12['padx'],b12['pady'] = 35, 5
	b12['bg']='red'

	contador = Label(frame6, text='0')

	
	b01.pack(side= LEFT)
	b02.pack(side= LEFT)
	b03.pack(side= LEFT)
	b04.pack(side= LEFT)
	b05.pack(side= LEFT)
	b06.pack(side= LEFT)
	b07.pack(side= LEFT)
	b08.pack(side= LEFT)
	b09.pack(side= LEFT)
	
	b10.pack(side= RIGHT)
	b11.pack(side= RIGHT)
	b12.pack(side= LEFT)


 	#LISTA COM OS BOTÕES
	listaBotoes = []
	listaBotoes.append(b01)
	listaBotoes.append(b02)
	listaBotoes.append(b03)
	listaBotoes.append(b04)
	listaBotoes.append(b05)
	listaBotoes.append(b06)
	listaBotoes.append(b07)
	listaBotoes.append(b08)
	listaBotoes.append(b09)


	event1 = lambda e : jogar(b01, nomeJogA, nomeJogB, simbJogA, simbJogB, listaBotoes, contador, vencedor)
	event2 = lambda e : jogar(b02, nomeJogA, nomeJogB, simbJogA, simbJogB, listaBotoes, contador, vencedor)
	event3 = lambda e : jogar(b03, nomeJogA, nomeJogB, simbJogA, simbJogB, listaBotoes, contador, vencedor)
	event4 = lambda e : jogar(b04, nomeJogA, nomeJogB, simbJogA, simbJogB, listaBotoes, contador, vencedor)
	event5 = lambda e : jogar(b05, nomeJogA, nomeJogB, simbJogA, simbJogB, listaBotoes, contador, vencedor)
	event6 = lambda e : jogar(b06, nomeJogA, nomeJogB, simbJogA, simbJogB, listaBotoes, contador, vencedor)
	event7 = lambda e : jogar(b07, nomeJogA, nomeJogB, simbJogA, simbJogB, listaBotoes, contador, vencedor)
	event8 = lambda e : jogar(b08, nomeJogA, nomeJogB, simbJogA, simbJogB, listaBotoes, contador, vencedor)
	event9 = lambda e : jogar(b09, nomeJogA, nomeJogB, simbJogA, simbJogB, listaBotoes, contador, vencedor)
	eventIniciar = lambda e : iniciar(nomeJogA, nomeJogB, simbJogA, simbJogB, vencedor, listaBotoes)
	eventNovoJogo = lambda e : restart(listaBotoes, contador, vencedor, nomeJogA)

	b01.bind('<Button-1>', event1)
	b02.bind('<Button-1>', event2)
	b03.bind('<Button-1>', event3)
	b04.bind('<Button-1>', event4)
	b05.bind('<Button-1>', event5)
	b06.bind('<Button-1>', event6)
	b07.bind('<Button-1>', event7)
	b08.bind('<Button-1>', event8)
	b09.bind('<Button-1>', event9)
	b10.bind('<Button-1>', eventIniciar)
	b11.bind('<Button-1>', eventNovoJogo)

	raiz.mainloop()

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
