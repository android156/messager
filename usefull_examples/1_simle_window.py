"""Подключаем файл с разметкой интерфейса, созданного через qtdesigner"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, qApp
from PyQt5 import uic
import threading


class MyWindow(QWidget):
    def __init__(self, filename, parent=None):
        super().__init__()
        self.filename = filename

        # Использование функции loadUi()
        uic.loadUi(self.filename, self)
        # Обработка события нажатия кнопки
        self.btnQuit.clicked.connect(qApp.quit)





if __name__ == '__main__':
    """
    Каждое приложение PyQt5 должно создать объект Qapplication. 
    Этот объект находится в модуле QtGui. 
    Параметр sys.argv - это список аргументов командной строки. 
    Скрипты на Python могут быть запущены из консоли, 
    и с помощью аргументов мы можем контролировать запуск приложения.
    """
    app1 = QApplication(sys.argv)
    app2 = QApplication(sys.argv)
    window_obj = MyWindow('test.ui')
    window_obj2 = MyWindow('test3.ui')
    window_obj.show()
    window_obj2.show()
    """
    В конце мы запускаем основной цикл приложения. Отсюда начинается обработка событий. 
    Приложение получает события от оконной системы и распределяет их по виджетам. 
    Когда цикл заканчивается, и если мы вызовем метод exit(), то наше окно (главный виджет) 
    будет уничтожено. Метод sys.exit() гарантирует чистый выход. 
    Окружение будет проинформировано о том, как приложение завершилось.
    """
    sys.exit(app1.exec_())

