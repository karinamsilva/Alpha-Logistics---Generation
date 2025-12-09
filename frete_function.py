import os 
import csv


#função sistema operacional

dados_frete = "dados_frete.csv"

campo_fretes = ['registro_frete','origem','destino','cliente','produto','status']
fretes = {}

import tkinter as tk 

def abrir_formulario_frete():
    popup_frete = tk.Toplevel()
    popup_frete.title('Adicionar Fretes')
    popup_frete.geometry('350x350')

    label_fretes = ['registro_frete','origem','destino','cliente','produto','status']


    #sequenciar campo com dados

    for campo_dados in label_fretes: 
        tk.Label(popup_frete, text=campo_dados).pack(pady=5)
        #cria os textos para o usuario 
        entrada_fretes = tk.Entry(popup_frete)
        #o input(caixa de texto)
        entrada_fretes.pack()
        #entrada_fretes[campo_fretes]= fretes
        fretes[campo_dados] = entrada_fretes

    def salvar():
        dados = {campo:fretes[campo].get() for campo in fretes}
        adicionar_frete(dados)
        popup_frete.destroy()

    def clear():
        for campo in fretes:
            fretes[campo].delete(0,tk.END)


    tk.Button(popup_frete, text='Salvar', command=salvar).pack(pady=5)
    tk.Button(popup_frete, text='Limpar', command=clear).pack(pady=5)

def adicionar_frete(registro):
#para manipular o arquivo
    arquivo = os.path.isfile(dados_frete)
    #add valores 
    #sempre que usar with open informa:
    #1 arquivo, 2 modo, 3 novas linhas, 4 utf 8
    
    with open(dados_frete, "a", newline="", encoding="utf-8") as arquivo_fretes:
        escrever = csv.DictWriter(arquivo_fretes, fieldnames=campo_fretes)
        escrever.writerow(registro)

