#!/usr/local/bin/python

import sys, signal
import pygame
import time
from serial import Serial, SerialException

def signal_handler(signal, frame):
    print("\nprogram exiting gracefully")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

pygame.init()
sound = pygame.mixer.Sound('beep.wav')
pianoa = pygame.mixer.Sound('piano-a.wav')
pianob = pygame.mixer.Sound('piano-b.wav')
pianoc = pygame.mixer.Sound('piano-c.wav')
pianod = pygame.mixer.Sound('piano-d.wav')
pianoe = pygame.mixer.Sound('piano-e.wav')
pianof = pygame.mixer.Sound('piano-f.wav')
pianog = pygame.mixer.Sound('piano-g.wav')


cxn = Serial('/dev/ttyACM1', baudrate=9600)
notes = []

while(True):
    while cxn.inWaiting() < 1:
        pass
    result = cxn.readline()
    try:
        resistance = float(result.strip().decode("utf-8").strip("'"))
        print (resistance)
        if resistance > 695 and resistance < 705:
            notes.append("a")
            time.sleep(3)
        elif resistance > 885 and resistance < 900:
            notes.append("b")
            time.sleep(3)
        elif resistance > 930 and resistance < 940:
            notes.append("c")
            time.sleep(3)
        elif resistance > 995 and resistance < 1005:
            notes.append("d")
            time.sleep(3)
        elif resistance > 1265 and resistance < 1285:
            notes.append("e")
            time.sleep(3)
        elif resistance > 1435 and resistance < 1450:
            notes.append("f")
            time.sleep(3)
        elif resistance > 1585 and resistance < 1595:
            notes.append("g")
            time.sleep(3)
        elif resistance > 2005 and resistance < 2015:
            for note in notes:
                if note == "a":
                    pianoa.play()
                    time.sleep(2)
                elif note == "b":
                    pianob.play()
                    time.sleep(2)
                elif note == "c":
                    pianoc.play()
                    time.sleep(2)
                elif note == "d":
                    pianod.play()
                    time.sleep(2)
                elif note == "e":
                    pianoe.play()
                    time.sleep(2)
                elif note == "f":
                    pianof.play()
                    time.sleep(2)
                elif note == "g":
                    pianog.play()
                    time.sleep(2)
            notes.clear()

    except ValueError:
        print("Please plug in a valid resistor")
