
import sys
import serial
import time

#ser = 0

def closeSerial(ser):
    if ser:
        ser.write(b"exit")
        ser.close()

def connectSerial():
    #ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser = serial.Serial('/dev/ttyACM0', 200000, timeout=1)
    time.sleep(1)

    ser.reset_input_buffer()
    #print("send ping")
    ser.write(b"ping")
    ser.flush()
    if getSerialResponseOK(ser):
        print("got pong returning ser")
        return ser
    print("return False for ser")
    return False

def getSerialResponseOK(ser):
    if ser:
        print("ROK?")
        waiting = True
        while waiting:
            if ser.in_waiting >0:
                waiting = False
                l = ser.readline()
                while l:
                    sline = l.decode('utf-8').rstrip()
                    print(sline)
                    if sline == "ok" or sline == "pong":
                        print("OK")
                        return True
                    l = ser.readline()
            else:
                time.sleep(0.1)
                print(".")
    else:
        return False

def sendSerialMsg(ser, msg, ok = True):

    if ser:
        #lineb = bytes(msg.rstrip(), 'utf-8')
        lineb = bytes(msg, 'utf-8')
        #print(lineb)
        ser.write(lineb)
        ser.flush()
        if ok and getSerialResponseOK(ser):
            return True
        else:
            return True
    print("no ser for "+str(msg))
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
