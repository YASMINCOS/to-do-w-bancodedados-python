
from tkinter import *
from tkinter import ttk
from typing import List

from pandas import wide_to_long
from dados import *


co_preta = "#000000"  
co_1 = "#59656F"
co_branca = "#feffff"  
co_azul = "#0074eb"  
co_vermelho = "#ff0000"
co_verde = "#008000" 


janela=Tk()
janela.resizable(width=False,height=False)
janela.geometry('500x225')
janela.title
janela.configure(background=co_1)

#dividindo janela

frame_esquerda=Frame(janela,width=300,height=200,bg=co_branca,relief="flat")
frame_esquerda.grid(row=0,column=0,sticky=NSEW)

frame_direita=Frame(janela,width=200,height=250,bg=co_branca,relief="flat")
frame_direita.grid(row=0,column=1,sticky=NSEW)

#dividindo frame esquerda

frame_esquerda_cima=Frame(frame_esquerda,width=200,height=50,bg=co_branca,relief="flat")
frame_esquerda_cima.grid(row=0,column=0,sticky=NSEW)



frame_esquerda_baixo=Frame(frame_esquerda,width=300,height=150,bg=co_branca,relief="flat")
frame_esquerda_baixo.grid(row=1,column=0,sticky=NSEW)

#criando botoes

def  main(a):
    ###novo##
    if a == "novo":
        
        for widget in frame_esquerda_baixo.winfo_children():
            widget.destroy()
        
        def adicionar():
            tarefa_entry=entry.get()
            inserir([tarefa_entry])
            mostrar()
        
        lb=Label(frame_esquerda_baixo,text="Insira nova tarefa",width=42,height=6,anchor=CENTER)
        lb.grid(row=0,column=0,sticky=NSEW) 
        
        entry=Entry(frame_esquerda_baixo,width=15)
        entry.grid(row=1,column=0,sticky=NSEW)    
        
        b_adicionar=Button(frame_esquerda_baixo,command=adicionar,text="Adicionar", width=9,height=1,pady=10,bg=co_1,fg=co_branca,font="8",anchor="center",relief=RIDGE)
        b_adicionar.grid(row=2,column=0,sticky=NSEW,pady=15)
        ##atualizar##
    if a =="atualizar":
            
            for widget in frame_esquerda_baixo.winfo_children():
                widget.destroy()
             
            def on():   
                
                
                lb=Label(frame_esquerda_baixo,text="Atualizar tarefa",width=42,height=6,anchor=CENTER)
                lb.grid(row=0,column=0,sticky=NSEW) 
                    
                entry=Entry(frame_esquerda_baixo,width=15)
                entry.grid(row=1,column=0,sticky=NSEW)    
                    
            
                valor_selecionador=listbox.curselection()[0]
                
                palavra=listbox.get(valor_selecionador)
                entry.insert(0,palavra)
                
                tarefas=selecionar()
                def alterar():
                 for item in tarefas:
                     if palavra==item[1]:
                      nova=[entry.get(),item[0]]
                      atualize(nova)
                      entry.delete(0,END)
                mostrar()
                
                b_at=Button(frame_esquerda_baixo,command=alterar,text="Atualizar", width=9,height=1,pady=10,bg=co_1,fg=co_branca,font="8",anchor="center",relief=RIDGE)
                b_at.grid(row=2,column=0,sticky=NSEW,pady=15)
    
            on()
b_novo = Button(frame_esquerda_cima,command=lambda:main("novo"),text="Novo", width=10,height=1,bg=co_azul,fg=co_branca,font="5",anchor="center",relief=RIDGE)
b_novo.grid(row=0,column=0,sticky=NSEW,pady=1)


def remove():
    valor_selecionador=listbox.curselection()[0]
    palavra = listbox.get(valor_selecionador)
    
       
    tarefas=selecionar()
    for item in tarefas:
        if palavra == item[1]:
            deletar([item[0]])
            
    mostrar()
    
b_remover=Button(frame_esquerda_cima,text="Remover", command=remove,width=10,height=1,bg=co_vermelho,fg=co_branca,font="5",anchor="center",relief=RIDGE)
b_remover.grid(row=0,column=1,sticky=NSEW,pady=1)



           

b_atualizar=Button(frame_esquerda_cima,text="Atualizar", command=lambda:main("atualizar"),width=10,height=1,bg=co_verde,fg=co_branca,font="5",anchor="center",relief=RIDGE)
b_atualizar.grid(row=0,column=2,sticky=NSEW,pady=1)

##adicionando listabok e label

label=Label(frame_direita,text="Tarefas",width=37,height=1,pady=7,padx=10,relief="flat",anchor=W, font=('Courier 20 bold'),bg=co_branca,fg=co_preta)
label.grid(row=0,column=0,sticky=NSEW,pady=1)

listbox=Listbox(frame_direita,font=("Courier 9 bold"),width=1)
listbox.grid(row=1,column=0,sticky=NSEW,pady=5)


###adicionando tarefas listbox
def  mostrar():
    listbox.delete(0,END)
    
    tarefas=selecionar()

    for item in tarefas:
        print(item[1])
        listbox.insert(END,item[1])
mostrar()

janela.mainloop()
