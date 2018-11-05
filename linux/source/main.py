import sys
from PyQt5 import QtWidgets
import subprocess
import des2, re

class ExampleApp(QtWidgets.QMainWindow, des2.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.textEdit.setText('25')
        self.startBtn.clicked.connect(self.start)
        self.stopBtn.clicked.connect(self.stop)

    def start(self):
        reboot = ' '
        if self.checkBoxReboot.checkState() != 0:
            reboot = ' -r'
        time = self.textEdit.toPlainText()
        
        if re.search('\D', time) != None:
            self.label.setText("err: только цифры")
        else:
            if not time:
                time = '1'
            subprocess.call('shutdown -h ' + time + reboot, shell=True)
            shutText = 'Выключение PC: '
            if re.search('-r', reboot) != None:
                shutText = 'Перезагрузка PC: '
            self.label.setText(shutText + time + ' мин')

    def stop(self):
        subprocess.call('shutdown -c', shell=True)
        self.label.setText('Таймер остановлен')

def shoot():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()
    
shoot()
