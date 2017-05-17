import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

class MainForm(QWidget) :
	def __init__(self):
		super().__init__()
		self.player = QMediaPlayer(self)
		self.setupUI()
		
	def setupUI(self):
		self.resize(550,450)
		self.move(300,300)
		self.setWindowTitle("PyQt Player")
		
		self.videoWidget  = QVideoWidget()
		
		self.player.setVideoOutput(self.videoWidget)
		
		self.label1 = QLabel('progress')
		self.progressSlider = QSlider(Qt.Horizontal)
		self.label2 = QLabel('volume')
		self.volumeSlider = QSlider(Qt.Horizontal)
		self.volumeSlider.setValue(100)
		
		grid = QGridLayout()
		grid.addWidget(self.label1, 0, 0)
		grid.addWidget(self.progressSlider,0, 1)
		grid.addWidget(self.label2, 1, 0)
		grid.addWidget(self.volumeSlider, 1, 1)
		
		self.openButton = QPushButton('open')
		self.playButton = QPushButton('play')
		self.playButton.setEnabled(False)
		self.pauseButton = QPushButton('pause')
		self.pauseButton.setEnabled(False)
		self.stopButton = QPushButton('stop')
		self.stopButton.setEnabled(False)
		
		hbox = QHBoxLayout()
		hbox.addWidget(self.openButton)
		hbox.addWidget(self.playButton)
		hbox.addWidget(self.pauseButton)
		hbox.addWidget(self.stopButton)
		hbox.addStretch()
		
		layout = QVBoxLayout()
		
		layout.addWidget(self.videoWidget)
		
		layout.addLayout(grid)
		layout.addLayout(hbox)
		self.setLayout(layout)
		
		self.openButton.clicked.connect(self.openButtonClick)
		self.playButton.clicked.connect(self.playButtonClick)	
		self.pauseButton.clicked.connect(self.pauseButtonClick)
		self.stopButton.clicked.connect(self.stopButtonClick)
		
		self.progressSlider.sliderMoved.connect(self.progressSliderMoved)
		self.volumeSlider.sliderMoved.connect(self.volumeSliderMoved)
		
		self.player.positionChanged.connect(self.playerPositionChanged)
		self.player.durationChanged.connect(self.playerDurationChanged)
		
	def setPlayingMode(self, mode):
		if mode:
			self.playButton.setEnabled(False)
			self.pauseButton.setEnabled(True)
			self.stopButton.setEnabled(True)
		else:
			self.playButton.setEnabled(True)
			self.pauseButton.setEnabled(False)
			self.stopButton.setEnabled(False)
			
	def openButtonClick(self):
		import os
		fileName = QFileDialog.getOpenFileName(self,'Open',os.curdir,'MP4 Files (*.mp4)','*.mp4')
		if len(fileName[0])>0:
			self.player.setMedia(QMediaContent(QUrl.fromLocalFile(fileName[0])))
			if self.player.state() == QMediaPlayer.PlayingState:
				self.player.stop()
			self.setPlayingMode(False)
			
	def playButtonClick(self):
		self.player.play()
		self.setPlayingMode(True)
		
	def pauseButtonClick(self):
		self.player.pause()
		self.setPlayingMode(False)
		
	def stopButtonClick(self):
		self.player.stop()
		self.setPlayingMode(False)
		
	def progressSliderMoved(self):
		self.player.setPosition(self.progressSlider.value())
		
	def volumeSliderMoved(self):
		self.player.setVolume(self.volumeSlider.value())
		
	def playerPositionChanged(self, position):
		self.progressSlider.setValue(position)
		
	def playerDurationChanged(self, position):
		self.progressSlider.setMaximum(position)
   	
if __name__ == '__main__':
	a  = QApplication(sys.argv)
	
	form = MainForm()
	form.show()
	
	a.exec_()
   	
   			
   	
   	
   	    
   	    
   	    
   	    
