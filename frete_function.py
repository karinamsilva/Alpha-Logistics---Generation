import os 
import csv
import tkinter as tk 
from tkinter import ttk

#função sistema operacional

dados_frete = "dados_frete.csv"

campo_fretes = ['registro_frete','origem','destino','cliente','produto','status']
fretes = {}

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

def exibir_fretes():
    #colocar fator correção ao exibir dados
    if not os.path.isfile(dados_frete):
        tk.Message.showerror('Erro', 'Arquivo não encontrado')
        return 
    #criar janela da tabela de fretes
    tabela_frete = tk.Toplevel()
    tabela_frete.title('Fretes')
    tabela_frete.geometry('750x500')

    #dizer para a tabela os campos que tem (colunas)
    colunas_fretes = campo_fretes

    tabela = ttk.Treeview(tabela_frete,columns=colunas_fretes, show='headings')
    #treeview, comando para mostrar os dados
    #itens são 1-onde, 2-colunas,3-cabeçalhos
    tabela.pack(fill='both')

    #config colunas 
    for colunas in colunas_fretes:
        tabela.heading(colunas,text=colunas)
        #cabeçalho
        tabela.column(colunas,width=100)
        #config tamanho da coluna

    with open(dados_frete,"r",encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        #ler o csv 
        
        for linha in leitor: 
            #para cada linha lida do csv, cria um campo para o valor 
            valores = [linha.get(colunas,None) for coluna in colunas_fretes]
            tabela.insert("","end",values=valores)
