import os
import csv
import tkinter as tk

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
        
