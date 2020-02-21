import serial
ser = serial.Serial('/dev/pts/3', 9600, timeout=1)  # open serial port
print(ser.name)         # check which port was really used
ser.write(b'hello')     # write a string
ser.close()             # close port

#with serial.Serial('/dev/ttyS1', 19200, timeout=1) as ser:
#    x = ser.read()          # read one byte
#    s = ser.read(10)        # read up to ten bytes (timeout)
#    line = ser.readline()   # read a '\n' terminated line
