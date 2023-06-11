import sys, os
from PyQt5.QtWidgets import  QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QMainWindow, QFileDialog
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from WindowUI import Ui_MusicPlayer

class MainWindow(QMainWindow) :
    #This is where all the magic happens. On the __init__ definition it's the responsible to call all the actions on the rest of definitions.
    def __init__(self):
        super().__init__()

        self.ui = Ui_MusicPlayer()
        self.ui.setupUi(self) # It setups everything from the UI file.
        
        self.player = QMediaPlayer() # It links all functions from the QMediaPlayer module to only player.

        self.player.setVolume(self.ui.VolumeSlider.value()) # The volume is set to 0, and in order to change it to 100%, you should move the slider.

        self.ui.PlayButton.clicked.connect(self.play) # Play button action
        self.ui.PauseButton.clicked.connect(self.pause) # Pause button action
        self.ui.ResumeButton.clicked.connect(self.resume) # Resume button action
        self.ui.StopButton.clicked.connect(self.stop) # Stop button action
        self.ui.VolumeSlider.sliderMoved.connect(self.volume) # Volume slider action


    def play(self):
        FileName, _ = QFileDialog.getOpenFileName(self, "Open Music") # It asks to the user to open a music file (YOU MUST NEED TO HAVE A CODEC INSTALLED IN ORDER TO WORK)
        SongName = os.path.basename(FileName) # It simplifies the name of the directory to simply the file name. For exampple, instead of showing C:\user\music\music.mp3, only shows music.mp3
        url = QUrl.fromLocalFile(FileName) # It grabs the file directory
        content = QMediaContent(url) # And then it uses to play the music
        self.ui.CurrentlyPlaying.setText(f"Currently playing: {SongName}") # When the music is playing, the label changes to show the name of the currently playing song.

        self.player.setMedia(content) # It establishes the song
        self.player.play() # And then it plays it.


    def pause(self, name):
        self.player.pause() # It pauses the song


    def resume(self):
        self.player.play() # It resumes it in case you have paused it.


    def stop(self):
        self.player.stop() # It makes stop the song

    
    def volume(self, position) :
        self.player.setVolume(position) # It changes the volume


# Here are some core things of Qt, there is no much that I can talk about it.
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
