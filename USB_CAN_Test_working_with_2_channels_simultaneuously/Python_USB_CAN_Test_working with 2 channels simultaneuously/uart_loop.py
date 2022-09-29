#!/usr/bin/python
# -*-coding: utf-8 -*-
# You can use it as a loop test
# https://blog.csdn.net/cai472861/article/details/105888584
import serial
import serial.tools.list_ports
import threading
import time
from datetime import datetime

# 列出所有当前的com x
port_list = list(serial.tools.list_ports.comports())
port_list_name = []
isrunning = True
myinput_1 = bytes([0X01, 0X03, 0X00, 0X00, 0X00, 0X01, 0X84, 0X0A])
myinput_2 = bytes([0X02, 0X03, 0X00, 0X00, 0X00, 0X01, 0X84, 0X0A])

input_charge = 0


class SerialPort:
    def __init__(self, port, buand):
        self.port = serial.Serial(port, buand)
        self.port.close()
        if not self.port.isOpen():
            self.port.open()

    def port_open(self):
        if not self.port.isOpen():
            self.port.open()

    def port_close(self):
        self.port.close()

    # This is a function of sending time frames
    # def send_data(self,data):
    #     while isrunning:
    #         # date = datetime.now().strftime('%H:%M:%S.%f')[:-3]
    #         print("send:", data)
    #         self.port.write(data)
    #         # self.port.write(date.encode())
    #         # input_charge += 1
    #         time.sleep(1)

    def send_data(self):
        #date = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        global input_charge
        while isrunning:
            if input_charge % 2:
                date = myinput_1
            else:
                date = myinput_2
            # date = datetime.now().strftime('%H:%M:%S.%f')[:-3]
            print("send:", date)
            self.port.write(date)
            # self.port.write(date.encode())
            # input_charge += 1
            time.sleep(1)

    def read_data(self):
        while isrunning:
            count = self.port.inWaiting()
            if count > 0:
                rec_str = self.port.read(count)
                print("receive:", rec_str)
                # If you use the time modal, pls exchange the below
                # print("receive:", rec_str.decode())
                # i += 1
        # if i == 5:
        #     isrunning = False
        #     print("Stopped the read_thread")


def test_control_input():
    global input_charge
    while isrunning:
        input_charge += 1
        time.sleep(1)


def show_all_com():
    if len(port_list) <= 0:
        print("the serial port can't find!")
    else:
        for itms in port_list:
            port_list_name.append(itms.device)


# The virtual ports are COM1 and COM2
if __name__ == '__main__':

    baunRate = 115200

    print("1.list all com")
    show_all_com()
    print(port_list_name)

    serialPort_w = 'COM1'
    print("2.open write port ", serialPort_w)
    mSerial_w = SerialPort(serialPort_w, baunRate)

    print("3.start write thread")
    t1 = threading.Thread(target=mSerial_w.send_data)
    t1.setDaemon(True)
    t1.start()

    # serialPort_r = 'COM2'
    # print("4.open read port ", serialPort_r)
    # mSerial_r = SerialPort(serialPort_r, baunRate)

    # print("5.start read thread")
    # t2 = threading.Thread(target=mSerial_r.read_data)
    # t2.setDaemon(True)
    # t2.start()

    print("6.start input change")
    real_control = test_control_input
    t3 = threading.Thread(target=real_control)
    t3.setDaemon(True)
    t3.start()

    # do something else, make main thread alive there
    while True:
        # target=mSerial_w.send_data
        time.sleep(1)
    # for i in range(5):
    #     time.sleep(10)
