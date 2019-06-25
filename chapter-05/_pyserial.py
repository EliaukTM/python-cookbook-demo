#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你想通过串行端口读写数据，典型场景就是和一些硬件设备打交道 (比如一个机器
人或传感器)。
"""
import serial

if __name__ == '__main__':
    ser = serial.Serial('/dev/tty.usbmodem641',  # Device name varies
                        baudrate=9600,
                        bytesize=8,
                        parity='N',
                        stopbits=1)

    ser.write(b'G1 X50 Y50\r\n')
    resp = ser.readline()