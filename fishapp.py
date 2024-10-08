import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget
from PyQt5.QtGui import QIcon, QPixmap, QFont, QFontDatabase
from PyQt5.QtCore import Qt, QTimer, QTime
import pygame
import time

#the actual gui
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fish.exe")
        self.setGeometry(700, 300, 700, 700)
        self.setWindowIcon(QIcon("logo.jpeg"))
        self.label = QLabel("Fish.exe opened", self)
        #time for background (pure chatgpt and pure pain for my beginner brain
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        #QPixmap and stuff (label to seperate code all still pure chatgpt)
        pixmap = QPixmap('mountain.jpeg')
        scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.background_label.setPixmap(scaled_pixmap)
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initui()
#window resize image stuff
    def resizeEvent(self, event):
            self.background_label.setGeometry(0, 0, self.width(), self.height())
            pixmap = QPixmap('mountain.jpeg')
            scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            self.background_label.setPixmap(scaled_pixmap)




#clock stuff
    def initui(self):
        self.time_label.setStyleSheet("font-size: 15px; color: white;")
        font_id = QFontDatabase.addApplicationFont("SpaceMono-Regular.ttf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)


        #making the buttons
        self.button1 = QPushButton("Play Last Christmas", self)
        self.button1.setGeometry(10, 70, 200, 50)
        self.button1.setStyleSheet("font-size: 15px; background-image: url(white.jpeg);")
        self.button1.clicked.connect(self.on_button1_click)

        self.button2 = QPushButton("Play Sweater Weather", self)
        self.button2.setGeometry(10, 135, 200, 50)
        self.button2.setStyleSheet("font-size: 15px; background-image: url(white.jpeg);")
        self.button2.clicked.connect(self.on_button2_click)

        self.button3 = QPushButton("Play a Christmas Audio thing", self)
        self.button3.setGeometry(10, 200, 200, 50)
        self.button3.setStyleSheet("font-size: 15px; background-image: url(white.jpeg);")
        self.button3.clicked.connect(self.on_button3_click)

        self.button4 = QPushButton("Play One beer left", self)
        self.button4.setGeometry(10, 265, 200, 50)
        self.button4.setStyleSheet("font-size: 15px; background-image: url(white.jpeg);")
        self.button4.clicked.connect(self.on_button4_click)

        self.button5 = QPushButton("Play Pope is a rockstar", self)
        self.button5.setGeometry(10, 330, 200, 50)
        self.button5.setStyleSheet("font-size: 15px; background-image: url(white.jpeg);")
        self.button5.clicked.connect(self.on_button5_click)

        self.button6 = QPushButton("Play Not Allowed", self)
        self.button6.setGeometry(10, 395, 200, 50)
        self.button6.setStyleSheet("font-size: 15px; background-image: url(white.jpeg);")
        self.button6.clicked.connect(self.on_button6_click)

        self.button7 = QPushButton("Play 7 years", self)
        self.button7.setGeometry(10, 460, 200, 50)
        self.button7.setStyleSheet("font-size: 15px; background-image: url(white.jpeg);")
        self.button7.clicked.connect(self.on_button7_click)

        self.button8 = QPushButton("Play Let go", self)
        self.button8.setGeometry(10, 525, 200, 50)
        self.button8.setStyleSheet("font-size: 15px; background-image: url(white.jpeg);")
        self.button8.clicked.connect(self.on_button8_click)

        self.button9 = QPushButton("Play Call me what you want", self)
        self.button9.setGeometry(10, 590, 200, 50)
        self.button9.setStyleSheet("font-size: 15px; background-image: url(white.jpeg);")
        self.button9.clicked.connect(self.on_button9_click)

        self.buttonA = QPushButton("Play hex", self)
        self.buttonA.setGeometry(10, 655, 200, 50)
        self.buttonA.setStyleSheet("font-size: 15px; background-image: url(white.jpeg)")
        self.buttonA.clicked.connect(self.on_buttonA_click)
#pause
        self.buttonB = QPushButton("pause", self)
        self.buttonB.setGeometry(10, 30, 100, 25)
        self.buttonB.setStyleSheet("font-size: 15px; background-image: url(white.jpeg)")
        self.buttonB.clicked.connect(self.on_buttonB_click)
#unpause
        self.buttonC = QPushButton("resume", self)
        self.buttonC.setGeometry(110, 30, 100, 25)
        self.buttonC.setStyleSheet("font-size: 15px; background-image: url(white.jpeg)")
        self.buttonC.clicked.connect(self.on_buttonC_click)

#clock
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm ap")
        self.time_label.setText(current_time)



#buttons code
    def on_button1_click(self):
        sound_file = "Last Christmas but you are in a bathroom at a party.mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
        pygame.mixer.music.queue('The Neighbourhood - Sweater Weather (8D AUDIO).mp3')
        self.button1.setText("Playing Last Christmas")


    def on_button2_click(self):
        sound_file1 = "The Neighbourhood - Sweater Weather (8D AUDIO).mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file1)
        pygame.mixer.music.play()
        pygame.mixer.music.queue('christmas audio.mp3')
        self.button2.setText("Playing Sweater Weather")

    def on_button3_click(self):
        sound_file2 = "christmas audio.mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file2)
        pygame.mixer.music.play()
        pygame.mixer.music.queue('One beer left.mp3')
        self.button3.setText("Playing Christmas Audio thing")

    def on_button4_click(self):
        sound_file3 = "One beer left.mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file3)
        pygame.mixer.music.play()
        pygame.mixer.music.queue('SALES - Pope Is a Rockstar (8D AUDIO).mp3')
        self.button4.setText("Playing One beer left")

    def on_button5_click(self):
        sound_file4 = "SALES - Pope Is a Rockstar (8D AUDIO).mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file4)
        pygame.mixer.music.play()
        pygame.mixer.music.queue('Not Allowed.mp3')
        self.button5.setText("Playing Pope is a rockstar")

    def on_button6_click(self):
        sound_file5 = "Not Allowed.mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file5)
        pygame.mixer.music.play()
        pygame.mixer.music.queue('Lukas Graham - 7 Years [Official Music Video].mp3')
        self.button6.setText("Playing Not Allowed")



    def on_button7_click(self):
        sound_file6 = "Lukas Graham - 7 Years [Official Music Video].mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file6)
        pygame.mixer.music.play()
        pygame.mixer.music.queue('let go.mp3')
        self.button7.setText("Playing 7 Years")


    def on_button8_click(self):
        sound_file7 = "let go.mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file7)
        pygame.mixer.music.play()
        pygame.mixer.music.queue('call me what u want.mp3')
        self.button8.setText("Playing Let go")


    def on_button9_click(self):
        sound_file8 = "call me what u want.mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file8)
        pygame.mixer.music.play()
        pygame.mixer.music.queue('Hex.mp3')
        self.button9.setText("Playing Call me when you want")


    def on_buttonA_click(self):
        sound_fileA = "Hex.mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(sound_fileA)
        pygame.mixer.music.play()
        self.buttonA.setText("Playing hex")

    def on_buttonB_click(self):
        pygame.mixer.music.pause()

    def on_buttonC_click(self):
        pygame.mixer.music.unpause()







#what even is this
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    background ="mountain.jpeg"
    background = "white.jpeg"
    window.show()
    sys.exit(app.exec_())


