from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *


class Coordinates():
	replayBtn = (360,230)
	#coordinates of Replay button
	dinohead = (125,240)
	#coordinates of dinosaur head

def restartGame():
	pyautogui.click(Coordinates.replayBtn)
	#function to click the replay button

def pressSpace():
	#implemetation for jump
	pyautogui.keyDown('space')
	time.sleep(0.05)
	print("Jump")
	pyautogui.keyUp('space')

def imageGrab():
	#box = (160,425,185,452)
	box = (Coordinates.dinohead[0]+30,Coordinates.dinohead[1]-13,Coordinates.dinohead[0]+55,Coordinates.dinohead[1]+25)
	#define a box infront of dinosaur which will be our area of concern 
	#if we find something in this area we will assume its an obstacle
	image = ImageGrab.grab(box)
	grayImage = ImageOps.grayscale(image)
	#to analyse image in Greyscale
	a = array(grayImage.getcolors())
	#convert the image into a numpy array and return the value
	return a.sum()

#if theres nothing present in the area of intrest imageGrab() will give some value,
# if theres an obstacle in the area of intrest it will give some other value
#here the value for an empty area of intrest(no obstacle) is 1197
#we will jump whenever the value is not 1197
def main():
	restartGame() 
	while(True):
		if(imageGrab()!=1197):
			pressSpace()
			time.sleep(0.05)     


main()

#http://apps.thecodepost.org/trex/trex.html--- game link
