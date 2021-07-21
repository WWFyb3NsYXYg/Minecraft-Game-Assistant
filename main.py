#pyinstaller --icon=app.ico --noconsole main.py
import keyboard
import pyautogui
import configparser
from pathlib import Path
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtGui import QIcon #библиотека для иконки

app = QtWidgets.QApplication([])
from PyQt5.QtWidgets import QLineEdit
ui = uic.loadUi("app.ui") # загружаем интерфейс
ui.setWindowTitle("Minecraft Game Assistant") # устанавливам название файла
ui.setWindowIcon(QIcon('logo.png')) # устанавливам иконку файла
config = configparser.ConfigParser()  # создаём объекта парсера
#config.read("settings.ini")  # читаем конфиг


myfile = Path('settings.ini')  #Path of your .ini file
config.read(myfile)

ui.le = QLineEdit()



#графа для ввода команд: a_0, a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9;
#кнопка сохранения: btn_save; 

def res_read():
	#print("Reading...")
	
	ui.a_1.setText(config["Set"]["a_1"])
	ui.a_2.setText(config["Set"]["a_2"])
	ui.a_3.setText(config["Set"]["a_3"])
	ui.a_4.setText(config["Set"]["a_4"])
	ui.a_5.setText(config["Set"]["a_5"])
	ui.a_6.setText(config["Set"]["a_6"])
	ui.a_7.setText(config["Set"]["a_7"])
	ui.a_8.setText(config["Set"]["a_8"])
	ui.a_9.setText(config["Set"]["a_9"])
	ui.a_0.setText(config["Set"]["a_0"])

res_read()
	

def res_save():
	#print("Saving...")
	
	config.set('Set', 'a_1', ui.a_1.text())
	config.set('Set', 'a_2', ui.a_2.text())
	config.set('Set', 'a_3', ui.a_3.text())
	config.set('Set', 'a_4', ui.a_4.text())
	config.set('Set', 'a_5', ui.a_5.text())
	config.set('Set', 'a_6', ui.a_6.text())
	config.set('Set', 'a_7', ui.a_7.text())
	config.set('Set', 'a_8', ui.a_8.text())
	config.set('Set', 'a_9', ui.a_9.text())
	config.set('Set', 'a_0', ui.a_0.text())
	config.write(myfile.open("w"))
	
def send(cmd):
    pyautogui.typewrite('/')
    pyautogui.typewrite(cmd)
    pyautogui.press('enter')

keyboard.add_hotkey('Alt + 1',lambda: send(config["Set"]["a_1"]))
keyboard.add_hotkey('Alt + 2',lambda: send(config["Set"]["a_2"]))
keyboard.add_hotkey('Alt + 3',lambda: send(config["Set"]["a_3"]))
keyboard.add_hotkey('Alt + 4',lambda: send(config["Set"]["a_4"]))
keyboard.add_hotkey('Alt + 5',lambda: send(config["Set"]["a_5"]))
keyboard.add_hotkey('Alt + 6',lambda: send(config["Set"]["a_6"]))
keyboard.add_hotkey('Alt + 7',lambda: send(config["Set"]["a_7"]))
keyboard.add_hotkey('Alt + 8',lambda: send(config["Set"]["a_8"]))
keyboard.add_hotkey('Alt + 9',lambda: send(config["Set"]["a_9"]))
keyboard.add_hotkey('Alt + 0',lambda: send(config["Set"]["a_0"]))

#keyboard.wait('Ctrl + Q')





ui.btn_save.clicked.connect(res_save)  #кнопка



ui.show()
app.exec()