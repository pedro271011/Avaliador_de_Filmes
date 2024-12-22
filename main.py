from Classe import Usuario
from Classe import Filme
from Classe import BancoDeDados
import tkinter as tk
from tkinter import messagebox

banco = BancoDeDados()
banco_de_usuarios = BancoDeDados()



def cadastro(tipo, banco):
    def criar_objeto():
        if tipo == "usuario":
            nome = campo_nome.get().strip()

            if not nome:
                messagebox.showerror("Erro", "O campo 'nome' não pode estar vazio.")
                return

            usuario = Usuario(nome, [])
            banco.salvar(usuario, "usuario")

            messagebox.showinfo("Sucesso", "Usuário cadastrado!")
            janela_cadastro.destroy()

        elif tipo == "filme":
            nome = campo_nome.get().strip()
            ano = campo_ano.get().strip()
            nota = campo_nota.get().strip()

            # Validações básicas
            if not nome or not ano or not nota:
                messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
                return

            try:
                ano = int(ano)
                nota = float(nota)
            except ValueError:
                messagebox.showerror("Erro", "Ano deve ser um número")
                return

            filme = Filme(nome, ano, nota)
            banco.salvar(filme, "filme")

            messagebox.showinfo("Sucesso", "Filme cadastrado!")
            janela_cadastro.destroy()

    # Janela de cadastro
    janela_cadastro = tk.Toplevel()
    janela_cadastro.title("Cadastro")

    # Nome
    tk.Label(janela_cadastro, text="Nome:").grid(column=0, row=0, padx=10, pady=5, sticky="w")
    campo_nome = tk.Entry(janela_cadastro, width=30)
    campo_nome.grid(column=1, row=0, padx=10, pady=5)

    if tipo == "filme":
        # Ano
        tk.Label(janela_cadastro, text="Ano:").grid(column=0, row=1, padx=10, pady=5, sticky="w")
        campo_ano = tk.Entry(janela_cadastro, width=30)
        campo_ano.grid(column=1, row=1, padx=10, pady=5)

        # Nota
        tk.Label(janela_cadastro, text="Nota:").grid(column=0, row=2, padx=10, pady=5, sticky="w")
        campo_nota = tk.Entry(janela_cadastro, width=30)
        campo_nota.grid(column=1, row=2, padx=10, pady=5)

   
    botao_cadastrar = tk.Button(janela_cadastro, text="Cadastrar", command=criar_objeto)
    botao_cadastrar.grid(column=0, row=3, columnspan=2, pady=10)

    janela_cadastro.mainloop()

def pesquisar():

        pesquisa = campo_pesquisa.get()
        campo_pesquisa.delete(0, tk.END) 

        if pesquisa.lower() == 'sair':
                
                texto_encerramento = tk.Label(janela, text = "Programa encerrado")
                texto_encerramento.grid(column= 2, row = 3)
                exit()


        procura = next((filme for filme in banco.filmes if filme == pesquisa), None)

        if procura is None:
                        
                messagebox.showinfo("Não encotrado", "O filme não foi encontrado. Cadastre esse filme!")
                        
        else:
                procura.exibir()

janela_login = tk.Tk()

orientacao = tk.Label(janela_login, text= "Seja bem vindo!")
orientacao.grid(column=2, row= 2)

botao_entrar = tk.Button(janela_login, text= "Entrar", command= Usuario.verificacao())
botao_entrar.grid(column=2, row=4)

botao_registro = tk.Button(janela_login, text= "criar nova conta", command=lambda: cadastro("usuario", banco_de_usuarios))
botao_registro.grid(column=2, row= 6)

janela_login.mainloop


janela = tk.Tk()

texto_orientacao = tk.Label(janela, text = "Qual filme vc esta procurando?")
texto_orientacao.grid(column = 2, row = 0)

campo_pesquisa = tk.Entry(janela, width = 30)
campo_pesquisa.grid(column= 2, row= 1)

Botao_pesquisa = tk.Button(janela, command = pesquisar)
Botao_pesquisa.grid(column= 3, row =1)

Botao_cadastro = tk.Button(janela, text="Cadastrar", command= lambda: cadastro("filme",banco))
Botao_cadastro.grid(column=2, row= 2)



janela.mainloop()