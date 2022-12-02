
import sys
import serial
import time

#ser = 0

def closeSerial(ser):
    if ser:
        ser.write(b"exit")
        ser.close()

def connectSerial():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

    ser.reset_input_buffer()
    #print("send ping")
    ser.write(b"ping")
    if getSerialResponseOK(ser):
        #print("got pong")
        return ser
    return False

def getSerialResponseOK(ser):
    if ser:
        #print("ROK?")
        waiting = True
        while waiting:
            if ser.in_waiting >0:
                waiting = False
                l = ser.readline()
                while l:
                    sline = l.decode('utf-8').rstrip()
                    if sline == "ok" or sline == "pong":
                        return True
                    print(sline)
                    l = ser.readline()
            else:
                time.sleep(1)
                print(".")
    return False

def sendSerialMsg(ser, msg, ok = False):

    if ser:
        lineb = bytes(msg.rstrip(), 'utf-8')
        print(lineb)
        ser.write(lineb)
        if ok and getSerialResponseOK(ser):
            return True
    return False

if __name__ == '__main__':
    print("Starting")
    ser = connectSerial()
    if ser:
        print("Started OK")
    else:
        testCall("NOK")
    while True:
        for line in sys.stdin:
            if line.rstrip() == "exit":
                closeSerial(ser)
                sys.exit()
            sendSerialMsg(ser, msg = line)

    print ("Lost connection!")
    closeSerial(ser)
    sys.exit()
