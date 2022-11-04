import time
import pyautogui
import tkinter as tk

def baixar_estoque():
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(0.5)
    pyautogui.write('ZMM247')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1.5)
    pyautogui.press('f2') 
    time.sleep(0.5)
    pyautogui.hotkey('shift', 'down')
    time.sleep(0.5)
    pyautogui.write('CDF3')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.hotkey('shift', 'down')
    time.sleep(0.5)
    pyautogui.write('FCDC')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.hotkey('shift', 'down')
    time.sleep(0.5)
    pyautogui.hotkey('shift', 'down')
    time.sleep(0.5)
    pyautogui.hotkey('shift', 'space')
    time.sleep(0.5)
    pyautogui.press('f8')
    time.sleep(1.5)
    pyautogui.hotkey('shiftleft', 'tab', 'up')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    root = tk.Tk()
    root.withdraw()
    estoque = root.clipboard_get()
    estoque = [i.split('\t') for i in estoque.split('\n')][:-1]
    estoque = [[i[0], int(float(i[2].replace(',', '.'))), i[3]] for i in estoque]
    estoque = sorted(estoque, key=lambda x: x[2])
    '''pyautogui.hotkey('ctrl', 'end')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    ultimo = root.clipboard_get()
    estoque = [ultimo]'''
    '''while True:
        pyautogui.press('up')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)
        linha = root.clipboard_get()
        colunas = linha.split('	')
        celulas = [colunas[0], colunas[2], colunas[3]]
        estoque.append(celulas)
        if linha == primeiro:
            break
    estoque = sorted(estoque, key=lambda x: x[2])
    estoque = [[i[0], int(float(i[1].replace(',', '.'))), i[2]] for i in estoque]'''

    return estoque

if __name__ == "__main__":
    print(baixar_estoque())
#[['00-100.035', '72,000', '24'],['00-100.018', '70,000', '24'], ['00-105.130', '12,000', '24'], ['00-100.038', '143,000', '23'], ['00-100.035', '72,000', '23'], ['00-105.287', '78,000', '23'], ['00-100.033', '115,000', '22'], ['00-105.231', '3,861', '22'], ['00-105.018', '28,000', '21'], ['00-100.038', '288,000', '21'], ['00-100.035', '29,000', '21'], ['00-100.033', '143,000', '21'], ['00-105.159', '63,000', '21'], ['00-100.043', '27,000', '20'], ['00-100.038', '141,000', '20'], ['00-100.033', '140,000', '20'], ['00-100.018', '61,000', '20'], ['00-105.140', '14,000', '20'], ['00-100.038', '71,000', '18'], ['00-100.033', '37,000', '18'], ['00-100.038', '66,000', '17'], ['00-105.219', '67,000', '17'], ['00-100.038', '72,000', '15'], ['00-100.038', '26,000', '13'], ['00-100.033', '0,000', '0'], ['00-105.231', '0,000', '0']]

