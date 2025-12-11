import os
import csv
import tkinter as tk
from tkinter import ttk

dados_cliente = "dados_cliente.csv"
campos_cliente = ['registro_cliente','nome','sobrenome','cidade','bairro']
entrada_clientes = {}


def abrir_formulario_cliente():
    popup_cliente = tk.Toplevel()
    popup_cliente.title('Adicionar Cliente')
    popup_cliente.geometry('350x350')


    for campo in campos_cliente:
        tk.Label(popup_cliente, text=campo).pack(pady=5)
        entrada = tk.Entry(popup_cliente)

        entrada.pack()
        entrada_clientes[campo] = entrada

    def salvar_clientes():
        dados = {campo:entrada_clientes[campo].get() for campo in entrada_clientes }
        adicionar_dados_cliente(dados)
        popup_cliente.destroy()

    def clear():
        for campo in entrada_clientes:
            entrada_clientes[campo].delete(0,tk.END)
    
    tk.Button(popup_cliente, text="Salvar", command=salvar_clientes).pack(pady=5)
    tk.Button(popup_cliente,text="Limpar",command=clear).pack(pady=5)


def adicionar_dados_cliente(data):
    arquivo_cliente = os.path.isfile(dados_cliente)
    with open(dados_cliente,"a",encoding='utf-8') as arquivo:
        escrever = csv.DictWriter(arquivo,fieldnames=campos_cliente)
        escrever.writerow(data)
        
def exibir_cliente():
    if not os.path.isfile(dados_cliente):
        tk.Message.showerror('Erro', 'Arquivo não encontrado')
        return 
    
    tabela_cliente = tk.Toplevel()
    tabela_cliente.title('Clientes')
    tabela_cliente.geometry('750x500')

    coluna_clientes = campos_cliente

    tabela = ttk.Treeview(tabela_cliente,columns=coluna_clientes,show='headings')
    tabela.pack(fill='both')

    for colunas in coluna_clientes:
        tabela.heading(colunas,text=colunas)
        tabela.column(colunas,width=100)

    with open(dados_cliente,"r",encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            valores = [linha.get(colunas,None) for coluna in coluna_clientes]
            tabela.insert("","end",values=valores)