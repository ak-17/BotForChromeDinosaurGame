from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *


class Coordinates():
	replayBtn = (360,230)
	dinohead = (125,240)

def restartGame():
	pyautogui.click(Coordinates.replayBtn)

def pressSpace():
	pyautogui.keyDown('space')
	time.sleep(0.05)
	print("Jump")
	pyautogui.keyUp('space')

def imageGrab():
	#box = (160,425,185,452)
	box = (Coordinates.dinohead[0]+30,Coordinates.dinohead[1]-13,Coordinates.dinohead[0]+55,Coordinates.dinohead[1]+25)
	image = ImageGrab.grab(box)
	grayImage = ImageOps.grayscale(image)
	a = array(grayImage.getcolors())
	return a.sum()

restartGame() 
while(True):
	if(imageGrab()!=1197):
		pressSpace()
		time.sleep(0.05)     
#def main():
#	restartGame()
#	while (True):
#		if(imageGrab()!=922):
#			pressSpace()
#			time.sleep(0.05)


#main()

#http://apps.thecodepost.org/trex/trex.html
