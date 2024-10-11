from colorama import Fore
import os
import time
import pyautogui
from pynput import keyboard, mouse

os.system('mode con: cols=129 lines=40')

titulo_1 = '''
                                                                                        
                                                                           
        █████                        ▄▄▄▄    ██▓     ▒█████   ▄████▄   ██ ▄█▀                   
       ████████                     ▓█████▄ ▓██▒    ▒██▒  ██▒▒██▀ ▀█   ██▄█▒                    
       ████████                     ▒██▒ ▄██▒██░    ▒██░  ██▒▒▓█    ▄ ▓███▄░                    
       ████████                     ▒██░█▀  ▒██░    ▒██   ██░▒▓▓▄ ▄██▒▓██ █▄                    
       ████████                     ░▓█  ▀█▓░██████▒░ ████▓▒░▒ ▓███▀ ░▒██▒ █▄                   
       ████████                     ░▒▓███▀▒░ ▒░▓  ░░ ▒░▒░▒░ ░ ░▒ ▒  ░▒ ▒▒ ▓▒                   
       ████████                     ▒░▒   ░ ░ ░ ▒  ░  ░ ▒ ▒░   ░  ▒   ░ ░▒ ▒░                   
       ████████   █                  ░    ░   ░ ░   ░ ░ ░ ▒  ░        ░ ░░ ░                    
       ████████████                  ░          ░  ░    ░ ░  ░ ░      ░  ░                      
       ████████  ██                       ░                  ░                                  
       ████████  ██                                                             
       ████████████              [--]      Switcher Macro for Minecraft       [--]                                  
       ████████████              [--]      By https://github.com/ilsiuk       [--]                              
       ████████████████          [--]  Discord https://discord.gg/F3GGyNYAkj  [--]                                            
       ████████████████████      [--]-----------------------------------------[--]                                               
       ████████████████████████                                              
       █████████████████████████                                                
       █████████████████████████                                                
       ████████  ████████████████                 [1] Switcher                                
       ██████       ████████████                                                
                       █████████                                                
                             ██                                                  
                                                                                                                                                                    
'''

titulo_2 = '''
                                                                                        
                                                                           
        █████                        ▄▄▄▄    ██▓     ▒█████   ▄████▄   ██ ▄█▀                   
       ████████                     ▓█████▄ ▓██▒    ▒██▒  ██▒▒██▀ ▀█   ██▄█▒                    
       ████████                     ▒██▒ ▄██▒██░    ▒██░  ██▒▒▓█    ▄ ▓███▄░                    
       ████████                     ▒██░█▀  ▒██░    ▒██   ██░▒▓▓▄ ▄██▒▓██ █▄                    
       ████████                     ░▓█  ▀█▓░██████▒░ ████▓▒░▒ ▓███▀ ░▒██▒ █▄                   
       ████████                     ░▒▓███▀▒░ ▒░▓  ░░ ▒░▒░▒░ ░ ░▒ ▒  ░▒ ▒▒ ▓▒                   
       ████████                     ▒░▒   ░ ░ ░ ▒  ░  ░ ▒ ▒░   ░  ▒   ░ ░▒ ▒░                   
       ████████   █                  ░    ░   ░ ░   ░ ░ ░ ▒  ░        ░ ░░ ░                    
       ████████████                  ░          ░  ░    ░ ░  ░ ░      ░  ░                      
       ████████  ██                       ░                  ░                                  
       ████████  ██                                                             
       ████████████              [--]      Switcher Macro for Minecraft       [--]                                  
       ████████████              [--]      By https://github.com/ilsiuk       [--]                              
       ████████████████          [--]  Discord https://discord.gg/F3GGyNYAkj  [--]                                            
       ████████████████████      [--]-----------------------------------------[--]                                               
       ████████████████████████                                                
       █████████████████████████                                                
       █████████████████████████                                                
       ████████  ████████████████                                               
       ██████       ████████████                                                
                       █████████                                                
                             ██                                                  
                                                                                                                                                                    
'''



def menu():
    os.system('cls' if os.name == 'nt' else 'clear')

    print(Fore.GREEN + titulo_1)
    preguntar = True

    while preguntar:
        opcion = input("Seleccione una opción:")
        opcion = int(opcion)

        if opcion == 1:
            preguntar = False
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            menu()
            
menu()

print(Fore.GREEN + titulo_2)

tecla_macro = input(Fore.GREEN + "¿Qué tecla deseas usar para switchearte? : ")
tecla_toggle = input(Fore.GREEN + "¿Qué tecla deseas usar para togglear el macro? (activar/descactivar) : ")
tecla_slot4 = input(Fore.GREEN + "¿Qué tecla tienes bindeada para el slot 4 de la hotbar? : ")
tecla_slot5 = input(Fore.GREEN + "¿Qué tecla tienes bindeada para el slot 5 de la hotbar? : ")
tecla_slot6 = input(Fore.GREEN + "¿Qué tecla tienes bindeada para el slot 6 de la hotbar? : ")
tecla_slot7 = input(Fore.GREEN + "¿Qué tecla tienes bindeada para el slot 7 de la hotbar? : ")

posiciones = [None] * 8
toggle_macro = True 
macro_en_ejecucion = False
mouse_listener = None

print(Fore.GREEN + "Posiciona el mouse en el casco equipado y apreta la tecla Z.")

def registrar_posicion():
    global posiciones
    for i in range(len(posiciones)):
        if posiciones[i] is None:
            posiciones[i] = pyautogui.position()
            if i == 0:
                print(Fore.GREEN + "Posiciona el mouse en la pechera equipada y apreta la tecla Z.")
            elif i == 1:
                print(Fore.GREEN + "Posiciona el mouse en el pantalón equipado y apreta la tecla Z.")
            elif i == 2:
                print(Fore.GREEN + "Posiciona el mouse en las botas equipadas y apreta la tecla Z.")
            elif i == 3:
                print(Fore.GREEN + "Posiciona el mouse en el casco en el inventario y apreta la tecla Z.")
            elif i == 4:
                print(Fore.GREEN + "Posiciona el mouse en la pechera en el inventario y apreta la tecla Z.")
            elif i == 5:
                print(Fore.GREEN + "Posiciona el mouse en el pantalón en el inventario y apreta la tecla Z.")
            elif i == 6:
                print(Fore.GREEN + "Posiciona el mouse en las botas en el inventario y apreta la tecla Z.")
            break

class MouseListener:
    def __init__(self):
        self.listener = mouse.Listener(on_move=self.on_move)
        self.active = False

    def on_move(self, x, y):
        return False

    def start(self):
        if not self.active:
            self.listener.start()
            self.active = True

    def stop(self):
        if self.active:
            self.listener.stop()
            self.active = False

def macro():
    global macro_en_ejecucion, mouse_listener
    if macro_en_ejecucion or not toggle_macro:
        return

    macro_en_ejecucion = True
    mouse_listener = MouseListener()
    mouse_listener.start() 

    pyautogui.PAUSE = 0  

    pyautogui.press('e')  
    time.sleep(0.05)  

    for i in range(4, 8):
        pyautogui.moveTo(posiciones[i])
        time.sleep(0.01)  
        pyautogui.press([tecla_slot4, tecla_slot5, tecla_slot6, tecla_slot7][i-4])
        time.sleep(0.05)

    for i in range(4):
        pyautogui.moveTo(posiciones[i])
        time.sleep(0.01)  
        pyautogui.press([tecla_slot4, tecla_slot5, tecla_slot6, tecla_slot7][i])
        time.sleep(0.05)  

    for i in range(4):
        pyautogui.moveTo(posiciones[i + 4]) 
        time.sleep(0.01)  
        pyautogui.press([tecla_slot4, tecla_slot5, tecla_slot6, tecla_slot7][i])
        time.sleep(0.05)  

    pyautogui.press('e')  
    time.sleep(0.01) 

    macro_en_ejecucion = False
    mouse_listener.stop() 

def on_press(key):
    global toggle_macro
    try:
        if key.char == 'z':
            registrar_posicion()
        elif key.char == tecla_macro and all(pos is not None for pos in posiciones):
            macro()
        elif key.char == tecla_toggle:
            toggle_macro = not toggle_macro
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

while True:
    if all(pos is not None for pos in posiciones) and not macro_en_ejecucion:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.GREEN + titulo_2)
        print(Fore.GREEN + "El macro ya está listo para usar. ")
        break

listener.join()
