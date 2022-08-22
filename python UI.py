from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit,QPushButton,QLabel,QDialog

bill=[56351651,51563900,35153114]
app = QApplication([])

def checkAnswer(target,digits): 
    times=10**digits
    for numbers in bill:
        if(target==numbers%times):
            return True
    return False
def bonus(times):
    if times==3:
        return 200
    elif times==4:
        return 1000
    elif times==5:
        return 4000
    elif times==6:
        return 10000
    elif times==7:
        return 40000
    elif times==8:
        return 10000000
            
class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('0710的作業.ui', self,)
        self.lineEdit=self.findChild(QLineEdit,"lineEdit")
        self.status_jackpot=False
        self.pushButton=self.findChild(QPushButton,"pushButton")
        self.pushButton2=self.findChild(QPushButton,"pushButton_2")
        self.label = self.findChild(QLabel,"label_18")
        self.label2 = self.findChild(QLabel,"label_2")
        self.label3 = self.findChild(QLabel, "label_21")
        self.label4 = self.findChild(QLabel, "label_19")
        self.label5 = self.findChild(QLabel, "label_20")
        self.pushButton.clicked.connect(self.actionGo)
        self.pushButton2.clicked.connect(self.turn)

        
    def showUp(self):
        self.show()

    def turn(self):
        dlg= Ui2(self)
        result=dlg.exec()
        if result==True:
            print("Ok!")
            print(bill)
            bill[0]=dlg.lineEdit.text()
            bill[1]=dlg.lineEdit2.text()
            bill[2]=dlg.lineEdit3.text()
            self.label3.setText(bill[0])
            self.label4.setText(bill[1])
            self.label5.setText(bill[2])
            
        else:
            print("Cancel!")

    def new(self):
        dlg= Ui3(self)
        result=dlg.exec()


    def actionGo(self):
        if(self.status_jackpot==False):
            if checkAnswer(int(self.lineEdit.text()),3):
                self.label2.setText("請輸入完整號碼")
                dlg= Ui3(self)
                result=dlg.exec()
                if result==True:
                    print("Ok!")
                    print(dlg.lineEdit.text())
                else:
                    print("Cancel!")
                    self.status_jackpot=True
            else:
                self.label.setText("沒中歐")
        else:
            print("完整")
            for i in range(4,9):
                times=10**i
                now_target=int(self.lineEdit.text())%times
                if checkAnswer(now_target,i):
                    print("Currently on the",i,"th")
                    if i==8:
                        print("congratulations","Currently on the 8th")
                        money=bonus(i)
                        self.label.setText("中了"+str(money)+"元")
                    continue
                else :
                    money=bonus(i-1)
                    self.label.setText("中了"+str(money)+"元")
                    break
class Ui2(QDialog):
    def __init__(self,parent=None):
        super(Ui2, self).__init__(parent)
        uic.loadUi('Dialog.ui', self)
        self.lineEdit=self.findChild(QLineEdit,"lineEdit")
        self.lineEdit2=self.findChild(QLineEdit,"lineEdit_2")
        self.lineEdit3=self.findChild(QLineEdit,"lineEdit_3")


class Ui3(QDialog):
    def __init__(self,parent=None):
        super(Ui3, self).__init__(parent)
        uic.loadUi('輸入完整號碼.ui', self)
        self.lineEdit=self.findChild(QLineEdit,"lineEdit")


      
ui = Ui()
ui.showUp()

app.exec()
