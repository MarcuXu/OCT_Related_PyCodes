'''
Author: MJ.XU
Date: 2022-07-10 17:17:39
LastEditTime: 2022-09-29 17:35:32
LastEditors: MJ.XU
Description:
Personal URL: https://macuxavier.github.io/
'''

import time
import serial
import csv

myinput_1 = bytes([0X01, 0X03, 0X00, 0X00, 0X00, 0X01, 0X84, 0X0A])
myinput_2 = bytes([0X02, 0X03, 0X00, 0X00, 0X00, 0X01, 0X84, 0X0A])
myinput_3 = bytes([0X03, 0X03, 0X00, 0X00, 0X00, 0X01, 0X84, 0X0A])


# https://blog.csdn.net/diaozhuzhen9762/article/details/101372542
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:
            self.fall = True
            return True
        else:
            return False


def serial_send(portx, bps, send_item):
    timex = None
    ser = serial.Serial(portx, bps, timeout=timex)
    # print("串口详情参数：", ser)

    # 十六进制的发送
    result = ser.write(send_item)
    ser.close()  # 关闭串口
    return result


# This is a kind of PY 'swicth' test
v = 2

for case in switch(v):
    if case(1):
        myinput = myinput_1
        # print 1
        break
    if case(2):
        myinput = myinput_2
        # print 2
        break
    if case(3):
        myinput = myinput_3
        # print 10
        break
    if case():  # default, could also just omit condition or 'if True'
        print("something else!")

total_lenth = 0
try:
    # portx = "COM1"
    # bps = 115200
    # #超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
    # timex = None
    # ser = serial.Serial(portx, bps, timeout=timex)
    # print("串口详情参数：", ser)
    # #十六进制的发送
    # result = ser.write(myinput)
    ####################################
    # https://blog.csdn.net/qq_30653631/article/details/90544662
    # https://www.cnblogs.com/zhoulonghai/p/12881344.html
    with open('Python_USB_CAN_Test_working with 2 channels simultaneuously\\a.csv', 'r') as csv_file:
        spamreader = csv.reader(csv_file)
        for row in spamreader:
            # print(type(row[0]))
            # print(row)# type of row: list
            sent_lenth = serial_send("COM1", 115200, [int(x, 16) for x in row])
            total_lenth += sent_lenth
            time.sleep(0.01)
    ############################################
    # for i in range(3): # this is the test for the loop sending
    #     sent_lenth = serial_send("COM1", 115200, myinput)
    #     time.sleep(0.01)
    # real_ser.close()
    # result = ser.write(chr(0x06).encode("utf-8"))  #写数据
    # print(type(myinput_1[0])) # check the type of input
    print("写入总字节数:%d" % total_lenth)

    # 十六进制的读取
    # print(ser.read().hex())  #读一个字节
    print("---------------")

except Exception as e:
    print("---异常---：", e)
