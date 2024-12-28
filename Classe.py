from subprocess import Popen
import json
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

class Usuario:
    def __init__(self, nome, filmesAssistidos):
        self.nome = nome
        self.filmesAssistidos = filmesAssistidos

    def para_dicionario(self):
        return {"nome": self.nome, "filmesAssistidos": self.filmesAssistidos}

    @classmethod
    def para_objeto(cls, data):
        return cls(data["nome"], data["filmesAssistidos"])
    
    @classmethod
    def verificacao(cls, banco_de_usuarios,janela_login):

        def processar_entrada():
            
            nome_inserido = campo_nome.get().strip()
            
            nome = next((usuario for usuario in banco_de_usuarios.usuarios if usuario.nome == nome_inserido), None)

            if nome is None:
                            
                    messagebox.showinfo("Não encotrado", "Esse nome de Usuario não existe")
                            
            else:
                    
                    messagebox.showinfo("Entrando", f"Bem vido {nome_inserido}")
                    janela_verificacao.destroy()
                    janela_login.destroy()

        janela_verificacao = tk.Toplevel()

        tk.Label(janela_verificacao, text="Nome:").grid(column=0, row=0, padx=10, pady=5, sticky="w")
        campo_nome = tk.Entry(janela_verificacao, width=30)
        campo_nome.grid(column=1, row=0, padx=10, pady=5)

        tk.Button(janela_verificacao, text="Entrar",command=processar_entrada).grid(column=1, row=1)

        janela_verificacao.mainloop()


class BancoDeDados:
    def __init__(self):
        self.usuarios = []
        self.filmes = []
        self.carregar("usuario")
        self.carregar("filme")

    def salvar(self, novo, tipo):
        if tipo == "usuario":
            banco_tipo = "Banco_de_Usuarios.json"
            self.usuarios.append(novo)
            dados_para_salvar = [usuario.para_dicionario() for usuario in self.usuarios]

        elif tipo == "filme":
            banco_tipo = "Banco_de_Filmes.json"
            self.filmes.append(novo)
            dados_para_salvar = [filme.para_dicionario() for filme in self.filmes]

        with open(banco_tipo, 'w') as file:
            json.dump(dados_para_salvar, file, indent=4)

    def carregar(self, tipo):
        if tipo == "usuario":
            banco_tipo = "Banco_de_Usuarios.json"
            try:
                with open(banco_tipo, 'r') as file:
                    dicionario_usuarios = json.load(file)
                    self.usuarios = [Usuario.para_objeto(usuario) for usuario in dicionario_usuarios]
            except FileNotFoundError:
                self.usuarios = []

        elif tipo == "filme":
            banco_tipo = "Banco_de_Filmes.json"
            try:
                with open(banco_tipo, 'r') as file:
                    dicionario_filmes = json.load(file)
                    self.filmes = [Filme.para_objeto(filme) for filme in dicionario_filmes]
            except FileNotFoundError:
                self.filmes = []
        
    

class Filme:
    def __init__(self, nome, ano, nota, qtdAvalaiacoes = 0, poster= "Caminho_poster"):
        self.nome = nome
        self.ano = ano 
        self.nota = nota
        self.qtdAvaliacoes = qtdAvalaiacoes
        self.poster = poster
    def __eq__(self, other):

        if isinstance(other, str):

            return self.nome == other
        
        return False
    
    @staticmethod
    def encontrar_poster(nome):
         
          busca = f"https://api.themoviedb.org/3/search/movie?api_key=dc1dffa08f0aca6d03c2e75d3c25de0a&query={nome}"
          resposta_Api = requests.get(busca)

          if resposta_Api.status_code == 200:
            resultados = resposta_Api.json().get('results', [])

            if resultados:
                filme = resultados[0] 
                poster_path = filme.get("poster_path")
                if poster_path:
                    return "https://image.tmdb.org/t/p/w500" + poster_path
            
            return None
    
    def para_dicionario(self):
        return{"nome": self.nome,"ano": self.ano,"nota": self.nota, "qtdAvaliacoes": self.qtdAvaliacoes, "poster": self.poster}
    
    @classmethod
    def para_objeto(cls, data):
        return cls(data["nome"], data["ano"], data["nota"], data["qtdAvaliacoes"], data["poster"])

    def exibir(self):


        def avaliar(janela_filme):
                
                instrucao1 = tk.Label(janela_filme, text ="Escolha uma nota entre 0 e 5")
                instrucao1.grid(column=1, row=6)

                campo_avaliacao = tk.Entry(janela_filme, width=25)
                campo_avaliacao.grid(column=1, row = 7)

                Botao_confirmar = tk.Button(janela_filme, text="Confirmar", command=lambda: verificacao())
                Botao_confirmar.grid(column=1, row =8)
               

                def verificacao():

                            notau = campo_avaliacao.get()
                            instrucao1.destroy()
                            campo_avaliacao.destroy()
                            Botao_confirmar.destroy()

                            try:

                                notau = float(notau)
                                self.nota = float(self.nota)

                                if notau > 5 or notau < 1:

                                    messagebox.showerror("Erro", "A nota precisa ser um valor entre 1 e 5")
                                    return
                                
                                else:
                                    
                                    self.qtdAvaliacoes = self.qtdAvaliacoes + 1

                                    if self.nota == 0:
                                        self.nota = notau

                                    self.nota = (self.nota * (self.qtdAvaliacoes - 1) + notau) / self.qtdAvaliacoes

                                    with open("Banco_de_Filmes.json", "r") as file:
                                        lista = json.load(file)

                                    novo_banco = [filme for filme in lista if filme["nome"] != self.nome]
                                    novo_banco.append({"nome": self.nome, "ano": self.ano, "nota": self.nota})

                                    with open("Banco_de_Filmes.json", 'w') as file:
                                        json.dump(novo_banco, file, indent = 4)

                                    messagebox.showinfo( 'Aviso',f'A nova nota de {self.nome} é {self.nota}.\n')
                                    
                                    return

                            except ValueError:
                                messagebox.showerror("A nota precisa ser um número")

                return
        

        janela_filme = tk.Toplevel()
        janela_filme.title(f'{self.nome}')

        nome = tk.Label(janela_filme, text=f'Nome: {self.nome}')
        nome.grid(column=1, row=2)

        ano = tk.Label(janela_filme,text= f'Ano: {self.ano}')
        ano.grid(column=1, row=3)

        nota = tk.Label(janela_filme,text= f'Nota: {self.nota}')
        nota.grid(column=1, row =4)

        Botao_avaliar = tk.Button(janela_filme, text='Avaliar', command= lambda: avaliar(janela_filme))
        Botao_avaliar.grid(column=1, row=6)

        Caminho_do_poster = Filme.encontrar_poster(self.nome)

        if Caminho_do_poster:
            resposta = requests.get(Caminho_do_poster)
            if resposta.status_code == 200:
                imagem = Image.open(BytesIO(resposta.content))
                poster_tk = ImageTk.PhotoImage(imagem)

                area_do_poster = tk.Canvas(janela_filme, width=500, height=700)
                area_do_poster.grid(column=1, row=5)
                area_do_poster.create_image(250, 350, image=poster_tk)
                area_do_poster.image = poster_tk

        else:

            tk.Label(janela_filme, text= "Poster nao encontrado").grid(column=1, row=5)

        Botao_voltar = tk.Button(janela_filme, text ='Voltar',command = janela_filme.destroy)
        Botao_voltar.grid(column=4, row=9)

        janela_filme.mainloop()

        
                        
  

        
    
    

        




    #Ler avaliações == ir para a lista de avaliações do filme