from subprocess import Popen
import json
import tkinter as tk
from tkinter import messagebox

class Usuario:
    def __init__(self, nome, email, filmesAssistidos):
        self.nome = nome
        self.email = email
        self.filmesAssistidos = filmesAssistidos

class BancoDeDados:

    def __init__(self):
        self.dados = []
        self.carregar()


    def salvar(self, novo):

        self.dados.append(novo) 

        with open('Banco_de_Filmes.json', 'w') as file:
            json.dump([filme.para_dicionario() for filme in self.dados], file, indent = 4)

    def carregar(self):

        try: 
            with open('Banco_de_filmes.json', 'r') as file:
                dicionario_filmes = json.load(file)   
                self.dados = [Filme.para_objeto(filme) for filme in dicionario_filmes]  

        except FileNotFoundError:
            self.dados = []  
    
    

class Filme:
    def __init__(self, nome, ano, nota):
        self.nome = nome
        self.ano = ano 
        self.nota = nota
        self.qtdAvaliacoes = 0

    def __eq__(self, other):

        if isinstance(other, str):

            return self.nome == other
        
        return False
    
    def para_dicionario(self):
        return{"nome": self.nome,"ano": self.ano,"nota": self.nota}
    
    @classmethod
    def para_objeto(cls, data):
        return cls(data["nome"], data["ano"], data["nota"])

    def exibir(self):


        
        janela_filme = tk.Toplevel()
        janela_filme.title(f'{self.nome}')

        nome = tk.Label(janela_filme, text=f'Nome: {self.nome}')
        nome.grid(column=1, row=2)

        ano = tk.Label(janela_filme,text= f'Ano: {self.ano}')
        ano.grid(column=1, row=3)

        nota = tk.Label(janela_filme,text= f'Nota: {self.nota}')
        nota.grid(column=1, row =4)

        Botao_avaliar = tk.Button(janela_filme, text='Avaliar', command= lambda: avaliar(janela_filme))
        Botao_avaliar.grid(column=1, row=5)

        Botao_voltar = tk.Button(janela_filme, text ='Voltar',command = janela_filme.destroy)
        Botao_voltar.grid(column=4, row=9)

        janela_filme.mainloop

        def avaliar(janela_filme):
                
                instrucao1 = tk.Label(janela_filme, text ="Escolha uma nota entre 0 e 5")
                instrucao1.grid(column=1, row=6)

                campo_avaliacao = tk.Entry(janela_filme, width=25)
                campo_avaliacao.grid(column=1, row = 7)

                Botao_confirmar = tk.Button(janela_filme, text="Confirmar", command=lambda: verificacao())
                Botao_confirmar.grid(column=1, row =8)
               

                def verificacao():

                            notau = campo_avaliacao.get()
                            instrucao1.destroy
                            campo_avaliacao.destroy
                            Botao_confirmar.destroy
                        

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

        
                        
  

        
    
    

        




    #Ler avaliações == ir para a lista de avaliações do filme