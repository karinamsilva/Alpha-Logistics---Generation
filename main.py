import tkinter as tk 
#Biblioteca de interface grafica para python
from tkinter import ttk
#Widgets do python

from frete_function import * 
from clients_functions import * 
 
root = tk.Tk()
#cria tela principal do sistema 
root.title('Projeto Scrum - Logistica')

#tamanho da tela (Largura x Altura)
root.geometry('400x300')

# Cabeçalho

header = ttk.Label(root,text='Logistica Alpha', font=('Arial',20, 'bold'))
body = ttk.Label(root,text='Frete mais rápido é aqui',font=('Arial',11,'italic'))
#qual tela, qual informação e qual fonte

#atribuir na tela
header.pack(pady=20)
body.pack(pady=5)

# area dos botões

button_screen = ttk.Frame(root)
#espaço para os botões e inseriu na tela principal 

button_screen.pack(pady=20)

ver_frete_button = ttk.Button(button_screen, text="Ver Frete")
#infos = onde e texto
add_frete_button = ttk.Button(button_screen, text="Adicionar Frete", command=abrir_formulario_frete)
ver_cliente_button = ttk.Button(button_screen,text="Ver Clientes")
add_cliente_button = ttk.Button(button_screen,text="Adicionar Cliente", command=abrir_formulario_cliente)

#para visualizar botões, cria tabela e informa qual coluna irá exibir
ver_frete_button.grid(row=0,column=0, pady=10,padx=10)
add_frete_button.grid(row=0,column=1, pady=10,padx=10)
ver_cliente_button.grid(row=1,column=0, pady=10,padx=10)
add_cliente_button.grid(row=1,column=1, pady=10,padx=10)



#ver a tela 
root.mainloop()

