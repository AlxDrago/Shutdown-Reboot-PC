import sys
from PyQt5 import QtWidgets
import des3, re, datetime, subprocess

class App(QtWidgets.QMainWindow, des3.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.textEdit.setText('25')
        self.hourInput.setText('18')
        self.minuteInput.setText('00')
        self.startBtn.clicked.connect(self.start)
        self.stopBtn.clicked.connect(self.stop)
        self.checkTimeShut.stateChanged.connect(self.checkHour)
        self.checkHour()

    #Метод проверки выключения по минутам или по часам
    def checkHour(self):
        global hour
        if self.checkTimeShut.checkState() != 0:
            self.textEdit.setDisabled(True)
            self.hourInput.setDisabled(False)
            self.minuteInput.setDisabled(False)
            hour = True
        else:
            self.hourInput.setDisabled(True)
            self.minuteInput.setDisabled(True)
            self.textEdit.setDisabled(False)
            hour = False

    #метод запуска
    def start (self):
        global reboot
        reboot = ' -s'
        if self.checkBoxReboot.checkState() != 0:
            reboot = ' -r'
        if hour == False:
            self.startOnMinute()
        else:
            self.startOnHour()

    def startOnMinute(self):
        global time
        time = self.textEdit.toPlainText()
        if re.search('\D', time) != None:
            self.label.setText('err: только цифры')
        else:
            if not time:
                time = '1'

        self.startNow()

    def startOnHour(self):
        global time, hourShut, minuteShut
        dateNow = datetime.timedelta(hours = datetime.datetime.now().hour, minutes = datetime.datetime.now().minute)
        hourShut = self.hourInput.toPlainText()
        minuteShut = self.minuteInput.toPlainText()
        dateShut = datetime.timedelta(hours = int(hourShut), minutes = int(minuteShut))
        time = (dateShut - dateNow).seconds / 60
        self.startNow()

    def startNow(self):
        subprocess.call('shutdown -t ' + str(int(time) * 60) + reboot, shell=True)
        shutText = 'Выключение PC: '
        if re.search('-r', reboot) != None:
            shutText = 'Перезагрузка PC: '
        if hour == False:
            self.label.setText(shutText + str(time) + ' мин')
        else:
            self.label.setText(shutText + str(hourShut + ' : ' + minuteShut) + ' мин')

    def stop(self):
        subprocess.call('shutdown -a', shell=True)
        self.label.setText('Таймер остановлен')

def shoot():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()
    
shoot()
