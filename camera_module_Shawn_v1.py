import time
import io
import socket
import struct
import guizero
import picamera
import picamera.array
# import cv2
import numpy as np
from PIL import Image

from guizero import App, Slider, ButtonGroup, CheckBox
from guizero import Combo, Waffle, Text, PushButton
from guizero import Picture, TextBox, Window
from time import sleep
from fractions import Fraction

app = App(title="Raspberry Pi Camera Module Controller")

intro = Text(app, text="I have not found a good app for this so I am writing it.")
ok = PushButton(app, text="Got it")

app.display()

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    # time.sleep(2)
    # camera.capture('foo.jpg')