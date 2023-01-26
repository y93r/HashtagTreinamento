import pyautogui
import time

pyautogui.alert('O código vai começar. Não mexa em NADA enquanto o código tiver rodando. Quando finalizar, eu te aviso')

pyautogui.PAUSE = 1
# apertar o windows do teclado
pyautogui.press('win')
# digitar chrome
pyautogui.write("chrome")
# apertar enter
pyautogui.press('enter')

# entrar no Gmail
pyautogui.write('gmail')
pyautogui.press('enter')

#esperar o gmail
while not pyautogui.locateOnScreen('logo_gmail.png'):
    time.sleep(1)

#tirar print das imagens que você vai clicar
# localizar a imagem -> vai te dar 4 informações: posicao x, posicao y, largura e altura

# entrar em contatos
x, y, largura, altura = pyautogui.locateOnScreen('tres_pontinhos.png')
pyautogui.click(x + largura/2, y + altura/2)

time.sleep(1)
x, y, largura, altura = pyautogui.locateOnScreen('contatos.png')
pyautogui.click(x + largura/2, y + altura/2)

#esperar o contatos
while not pyautogui.locateOnScreen('tela_contatos.png'):
    time.sleep(1.5)
    
# exportar os contatos
x, y, largura, altura = pyautogui.locateOnScreen('exportar.png')
pyautogui.click(x + largura/2, y + altura/2)
x, y, largura, altura = pyautogui.locateOnScreen('confirmar_exportar.png')
pyautogui.click(x + largura/2, y + altura/2) 

time.sleep(1.5)
pyautogui.press('enter')

#Enviar email
import pandas as pd
import pyperclip

time.sleep(2)
df = pd.read_csv(r'C:\Users\Usuário\Downloads\contacts.csv')
df = df.dropna(axis=1)
display(df)

#(combinação de teclas)
pyautogui.hotkey('ctrl', 'pgup')

for email in df['E-mail 1 - Value']:
    #clicar no botão escrever
    time.sleep(1.5)
    x, y, largura, altura = pyautogui.locateOnScreen('escrever.png')
    pyautogui.click(x + largura/2, y + altura/2)
    time.sleep(1.5)
    # escrever o email
    pyautogui.write(email)
    pyautogui.press('enter')
    #tab para o assunto do email
    pyautogui.press('tab')
    pyautogui.write('Teste RPA')
    #tab para o corpo do email
    pyautogui.press('tab')
    texto = """
    Boa noite,
    
    Testando um negócio aqui.
    
    Abs e tmj"""
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('ctrl', 'enter')
    
    
pyautogui.alert('O código terminou, o pc é seu de novo!')
