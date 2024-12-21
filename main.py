
from Classe import Usuario
from Classe import Filme
from Classe import BancoDeDados
import tkinter as tk

banco = BancoDeDados()




def cadastro():

        def criar_objeto():

                nome = campo_cadastro1.get()
                ano = campo_cadastro2.get()
                nota = campo_cadastro3.get()

                #try:
                 #       nome = str(nome)
                 #       ano = int(ano)
                #        nota = float(nota)

               # except:

                
                nome = Filme(nome, ano, nota)
                banco.salvar(nome)

                for bloco in blocos:
                        bloco.destroy()
                blocos.clear()

                aviso = tk.Label(janela_cadastro, text='Filme cadastrado com sucesso')
                aviso.grid(column=2, row= 3)

                voltar = tk.Button(janela_cadastro, width= 10, command= janela_cadastro.destroy)
                voltar.grid(column=2, row = 5)

        
        janela_cadastro = tk.Toplevel()
        janela_cadastro.title('Cadastro')

        blocos = []
        

        instrucao1= tk.Label(janela_cadastro, text= "Digite o nome do Filme:")
        instrucao1.grid(column=2,  row = 0)
        blocos.append(instrucao1)

        campo_cadastro1 = tk.Entry(janela_cadastro, width=30)
        campo_cadastro1.grid(column=2, row= 1)
        blocos.append(campo_cadastro1)


        instrucao2= tk.Label(janela_cadastro, text= "Digite o ano do Filme:")
        instrucao2.grid(column=2,  row = 3)
        blocos.append(instrucao2)

        campo_cadastro2 = tk.Entry(janela_cadastro, width=30)
        campo_cadastro2.grid(column=2, row= 4)
        blocos.append(campo_cadastro2)


        instrucao3= tk.Label(janela_cadastro, text= "Qual nota vc daria para este filme")
        instrucao3.grid(column=2,  row = 6)
        blocos.append(instrucao3)

        campo_cadastro3 = tk.Entry(janela_cadastro, width=30)
        campo_cadastro3.grid(column=2, row= 7)
        blocos.append(campo_cadastro3)

        Botao_cadastro3 = tk.Button(janela_cadastro, command= criar_objeto)
        Botao_cadastro3.grid(column=2, row = 8)
        blocos.append(Botao_cadastro3) 

        
        

        janela_cadastro.mainloop()



def pesquisar():

        pesquisa = campo_pesquisa.get()
        campo_pesquisa.delete(0, tk.END) 

        if pesquisa.lower() == 'sair':
                
                texto_encerramento = tk.Label(janela, text = "Programa encerrado")
                texto_encerramento.grid(column= 2, row = 3)
                exit()


        procura = next((filme for filme in banco.dados if filme == pesquisa), None)

        if procura is None:
                        
                
                texto_aviso = tk.Label(janela, text = f'O filme {pesquisa} não foi encontrado.')
                texto_aviso.grid(column= 2, row = 2)

                texto_pergunta = tk.Label(janela, text = 'Deseja cadastrar um Filme?')
                texto_pergunta.grid(column= 2, row = 3)

                botao_cadastro = tk.Button(janela, text = 'Sim', command = cadastro)
                botao_cadastro.grid(column= 1, row = 4)

                #Criar uma função de retorno para a Busca, Talvez fechar e abrir a janela
                botao_cadastro2 = tk.Button(janela, text = 'Não', command = cadastro)
                botao_cadastro2.grid(column= 3, row = 4)

                        
        else:
                procura.exibir()

                teste  = input("Deseja avaliar este título?\nSim(s)     Não(n)\n") 

                if teste.lower() == "s":
                        
                        Filme.avaliar(procura)


janela = tk.Tk()

texto_orientacao = tk.Label(janela, text = "Qual filme vc esta procurando?")
texto_orientacao.grid(column = 2, row = 0)

campo_pesquisa = tk.Entry(janela, width = 30)
campo_pesquisa.grid(column= 2, row= 1)

Botao_pesquisa = tk.Button(janela, command = pesquisar)
Botao_pesquisa.grid(column= 3, row =1)



janela.mainloop()