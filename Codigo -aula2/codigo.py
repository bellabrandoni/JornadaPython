            #Passo a passo do projeto
    #1- Entrar no sistema da empresa
#https://dlp.hashtagtreinamentos.com/python/intensivao/login

##### importando bibliotecas ##########
import pyautogui
import time

#Configuracao de pausa de 1 segundo e meio a cada coamando pyautogui
pyautogui.PAUSE = 1.5
#comandos pyautogui
#pyautogui.click #-> clicar em algum lugar da tela
#pyautogui.write #-> escrever um texto
#pyautogui.press #-> pressionar 1 unica tecla do teclado
    #2 - Abrir o navegador 
pyautogui.press("win") #-> pressiona a tecla windows
pyautogui.write("chrome") #-> escreve chrome na tela do windows
pyautogui.press("enter")

    #- Criar variavel para o link - Entrar no sistema da empresa
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#Pausa para o camando especifico abaixo - biblioteca time
time.sleep(2)


    #3 - login - email e senha 
#a posucao foi capturada no codigo auxiliar.py
pyautogui.press("tab")

#logando campo de  email
pyautogui.write("isabella14brandao@gmail.com")

#logando campo de senha - passando para tecla tab
pyautogui.press("tab")
pyautogui.write("sua senha aqui")

#clicar no botao de logar - com click

pyautogui.press("enter")

#tempo para logar n a proxima pagina
time.sleep(3)
    #4 - importar a base de dados
#Importando biblioteca pandas 
import pandas
#-. A biblioteca pandas vai ler o arquivo csv 
tabela = pandas.read_csv("produtos.csv")

#visualizando arquivo csv no terminal - ver se o comando de cima foi executando
#print(tabela)

    #5 Cadastrar um produto
#Clicar no primeiro campo marca
#descobrir a posicao do campo 
#pyautogui.click(x=430, y=236)

"""digitando o codigo do produto
pyautogui.write("codigo do produto")
#pulando para proximas categorias 
pyautogui.press("tab")

# marca 
pyautogui.write("marca")
pyautogui.press("tab")
# tipo de produto
pyautogui.write("tipo")
pyautogui.press("tab")
#categoria
pyautogui.write("categoria")
pyautogui.press("tab")
#preco
pyautogui.write("preco")
pyautogui.press("tab")
#custo
pyautogui.write("custo")
pyautogui.press("tab")
#observacao
pyautogui.write("obs")
pyautogui.press("tab")

Apertando o botao enviar 
pyautogui.press("enter")"""

    #6 Repetir o processo 4 até acabar 
#para cada linha(index) na tabela aplique este for 
for linha in tabela.index:
    pyautogui.click(x=408, y=271)
    
        #codigo do produto 
        #loc . -> localiza detro da tabela selecionando lista de informacoes [linha, nome dacoluna da tabela] -na tabela 
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(codigo)
    #pulando para proximas categorias 
    pyautogui.press("tab")
    # marca 
    #marca = tabela.loc[linha,"marca"]
    pyautogui.write(tabela.loc[linha,"marca"])
    pyautogui.press("tab")
    # tipo de produto
    pyautogui.write(tabela.loc[linha,"tipo"])
    pyautogui.press("tab")
    #categoria -str - transformando em texto
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
    #preco - str-transformando em texto
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    #custo - str-transformando em texto
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")
    #observacao
    #criando variavel obs
    obs = tabela.loc[linha,"obs"]
    #condicao para verificar se a obs esta null
    # pandas.isna -> isna  significa é vazio 
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    #Apertando o botao enviar 
    pyautogui.press("enter")
    #rolagem - voltando para cadastrar novos produtos no incio da tela
    pyautogui.scroll(5000)