#! /usr/bin/python

import serial
import time
from xbee import ZigBee

serial_port = serial.Serial('COM4', 9600)

def print_data(data):
    """
    This method is called whenever data is received
    from the associated XBee device. Its first and
    only argument is the data contained within the
    frame.
    """

    myData = data['rf_data']
    print(data)
    print(myData)
    fd = open("log.txt", "a")
    fd.write(myData.decode("utf-8") + "\n")
    fd.close()

xbee = ZigBee(serial_port, callback=print_data)

while True:
    try:
        time.sleep(0.001)
    except KeyboardInterrupt:
        break

xbee.halt()
serial_port.close()