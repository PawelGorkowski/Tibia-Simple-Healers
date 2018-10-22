from PIL import ImageGrab
import pyautogui
from win32.win32gui import *
import time

'''
    Retorna qual janela está ativa

    return bool
'''
def getTibiaActive():
    tibia = GetWindowText(GetForegroundWindow()).lower()
    if tibia.__contains__('tibia'):
        return True
    else:
        return False

'''
    captura imagem se estiver na tela
    param:
        img: nome do arquivo a ser checado
        save: nome do arquivo para salvar
    
    Ex: capture('manaFull', 'manaAtual')
    return void
'''
def checkImgToCapture(img, save):
    pos = pyautogui.locateCenterOnScreen('Picture/'+ img +'.png')
    print(pos)
    a = ImageGrab.grab(bbox=(pos[0]-45, pos[1]-5, pos[0]+45, pos[1]+6))
    a.save('Healing/'+ save +'.png')

'''
    Retorna porcentagem sobre os pixels
    param: 
        percent: valor em porcentagem
        whole: Total do valor
    
    Ex: pecentage(80, 86) 
        resultado = 68.8
'''

def percentage(percent, whole):
  return (percent * whole) / 100.0

'''
    captureWpt()
'''

#def captureWpt():