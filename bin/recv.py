import serial
import sys

with serial.Serial('/dev/pts/6', 9600, timeout=1) as ser:

    while(ser.is_open):
        s = ser.read() #read one byte
        msg = ser.read(100)
        line = ser.readline() # read a '\n'
        print(msg)