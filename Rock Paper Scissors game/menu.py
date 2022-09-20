import sys
import random
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QStackedWidget, QPushButton, QMenuBar,QStatusBar
from PyQt6.QtGui import QPixmap
from PyQt6 import uic
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("gui/RPS start menu.ui",self)

        self.setWindowTitle("Rock Paper Scissors")
        self.startBttn.clicked.connect(self.start_clicked)
        self.infoBttn.clicked.connect(self.info)


    #Changes screen after start button is clicked
    def start_clicked(self):
        w.setCurrentIndex(1)

    def info(self):
        self.newWindow = infoWindow()
        self.newWindow.show()
        
class gameScreen(QMainWindow):
    def __init__(self):
        super(gameScreen, self).__init__()
        uic.loadUi("gui/RPS game.ui",self)
        
        global compChoice

        randomChoice = random.randrange(1,4)
        if randomChoice == 1:
            compChoice = "rock"
        elif randomChoice == 2:
            compChoice = "paper"
        elif randomChoice == 3:
            compChoice = "scissors"
                      
        #Calls functions for PC player when one of the buttons are pressed
        self.option1.clicked.connect(self.compRock)
        self.option2.clicked.connect(self.compPaper)
        self.option3.clicked.connect(self.compScissors)
        self.reset.clicked.connect(self.opReset)

    #Function that is called when rock button is pressed
    def compRock(self):
        
        self.whatUChose.setText("rock")
        self.user.setPixmap(QPixmap("assets/rock.png"))
        time.sleep(0.5)
        
        self.whatPCChose.setText(compChoice)
        if compChoice == "rock":
            self.computer.setPixmap(QPixmap("assets/rockFlipped.png"))            
            self.roundWin.setText("It's a tie")
        elif compChoice == "paper":
            self.computer.setPixmap(QPixmap("assets/paperFlipped.png"))
            self.roundWin.setText("Paper beats rock, you lose")
        elif compChoice == "scissors":
            self.computer.setPixmap(QPixmap("assets/scissorsFlipped.png"))
            self.roundWin.setText("Rock beats scissors, you win!")

    #Function that is called when paper button is pressed
    def compPaper(self):

        self.whatUChose.setText("paper")
        self.user.setPixmap(QPixmap("assets/paper.png"))
        time.sleep(0.5)

        self.whatPCChose.setText(compChoice)

        if compChoice == "rock":
            self.computer.setPixmap(QPixmap("assets/rockFlipped.png"))     
            self.roundWin.setText("Paper covers rock, you win!")
        elif compChoice == "paper":
            self.computer.setPixmap(QPixmap("assets/paperFlipped.png"))
            self.roundWin.setText("It's a tie")
        elif compChoice == "scissors":
            self.computer.setPixmap(QPixmap("assets/scissorsFlipped.png"))
            self.roundWin.setText("Scissors beats paper, you lose")

    #Function that is called when scissors button is pressed
    def compScissors(self):

        self.whatUChose.setText("scissors")
        self.user.setPixmap(QPixmap("assets/scissors.png"))
        time.sleep(0.5)
               
        self.whatPCChose.setText(compChoice)
        if compChoice == "rock":
            self.computer.setPixmap(QPixmap("assets/rockFlipped.png"))     
            self.roundWin.setText("Rock beats scissors, you lose")
        elif compChoice == "paper":
            self.computer.setPixmap(QPixmap("assets/paperFlipped.png"))
            self.roundWin.setText("Scissors beats paper, you win!")
        elif compChoice == "scissors":
            self.computer.setPixmap(QPixmap("assets/scissorsFlipped.png"))            
            self.roundWin.setText("It's a tie")

    def opReset(self):
        self.whatUChose.clear()
        self.whatPCChose.clear()
        self.roundWin.clear()
        self.computer.setPixmap(QPixmap("assets/rockFlipped.png"))           
        self.user.setPixmap(QPixmap("assets/rock.png"))

        global compChoice
        randomChoice = random.randrange(1,4)
        if randomChoice == 1:
            compChoice = "rock"
        elif randomChoice == 2:
            compChoice = "paper"
        elif randomChoice == 3:
            compChoice = "scissors"

class infoWindow(QMainWindow):
    def __init__(self):
        super(infoWindow, self).__init__()
        uic.loadUi("gui/RPS instructions.ui",self)
        self.setWindowTitle("instructions")
        self.setFixedSize(270, 121)

app = QApplication(sys.argv)

w = QStackedWidget()
win = MainWindow()
win2 = gameScreen()
win3 = infoWindow()
w.addWidget(win)
w.addWidget(win2)
w.setFixedSize(1000, 550)
w.show()
app.exec()