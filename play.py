
# Import required libraries
import sys
import RPi.GPIO as GPIO
import time
import importlib
import serial_arduino as s

def theEnd(ser):
    # cleanup will free PINS and exit will terminate code execution
    s.sendSerialMsg(ser, "goff", True)
    time.sleep(1)
    s.sendSerialMsg(ser, "coff", True)
    time.sleep(1)
    s.sendSerialMsg(ser, "roff", True)
    time.sleep(1)
    s.closeSerial(ser)
    print("serial off, exitting")
    GPIO.cleanup()
    #sys.exit()

def serialStart():
    print("connecting serial...")
    ser = s.connectSerial()
    return ser

def play(m, inp = "", note = "", length = 1, serial = False):
    #print(f"Arguments count: {len(sys.argv)}")
    ser = False
    if serial: 
        ser = serialStart()
    if ser:
        print("ser set")
    else:
        print("ser NOT set")
    # Set trigger PIN according with your cabling
    triggerPIN1 = 12
    triggerPIN2 = 16

    # Set PIN to output
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(triggerPIN1,GPIO.OUT)
    GPIO.setup(triggerPIN2,GPIO.OUT)

    # define PWM signal and start it on trigger PIN
    buzzer1 = GPIO.PWM(triggerPIN1, 220) # Set frequency to 1 Khz
    buzzer2 = GPIO.PWM(triggerPIN2, 880) # Set frequency to 1 Khz
    start1 = False
    start2 = False
    start3 = False
    start4 = False
    start5 = False
    stop1 = True
    stop2 = True
    stop3 = True
    stop4 = True
    stop5 = True
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    step = 1

    rec = False
    com = False
    recc = 0
    #for note in range( size ):
    if inp == "freq":
        buzzer1.ChangeFrequency(int(note))
        buzzer2.ChangeFrequency(int(note))
        buzzer1.start(50) # Set dutycycle to 10
        buzzer2.start(50) # Set dutycycle to 10
        time.sleep(float(length))
        buzzer1.stop() # Set dutycycle to 10
        buzzer2.stop() # Set dutycycle to 10
        theEnd(ser)
        return 1
    if inp == "note":
        buzzer1.ChangeFrequency(getattr(m,note))
        buzzer2.ChangeFrequency(getattr(m,note))
        buzzer1.start(50) # Set dutycycle to 10
        buzzer2.start(50) # Set dutycycle to 10
        time.sleep(float(length))
        buzzer1.stop() # Set dutycycle to 10
        buzzer2.stop() # Set dutycycle to 10
        theEnd(ser)
        return 1
    if inp == "serial":
        s.sendSerialMsg(ser, note)
        time.sleep(float(length))
        #s.sendSerialMsg(ser, note[0:1]+"off")
        theEnd(ser)#sends all off msgs
        return 1

    size = len(m.violin)
    if len(m.bass) > size: 
        size = len(m.bass)
    while count1 < len(m.violin)-1:
        if m.v_dur[count1] == 0:
            if len(m.v_dur) > count1+step:
                count1=count1+step
            stop1 = True
            buzzer1.stop()
            #print("stop1")
        if m.b_dur[count2] == 0:
            if len(m.b_dur) > count2+step:
                count2=count2+step
            stop2 = True
            buzzer2.stop()
            #print("stop2")
        if serial == True and len(m.record) > 0 and m.r_dur[count3] == 0:
            print("rec count3="+str(count3)+" serial="+str(serial)+" data="+str(m.r_dur[count3]))
            print("stop3")
            if len(m.r_dur) > count3+step:
                count3=count3+step
            stop3 = True
            #if rec and recc > 2:
            s.sendSerialMsg(ser, "roff")
            #rec = False
            #recc = 0
        if serial and len(m.compresor) > 0 and m.c_dur[count4] == 0:
            if len(m.c_dur) > count4+step:
                count4=count4+step
            stop4 = True
            #if com and recc > 2:
            s.sendSerialMsg(ser, "coff")
            print("stop4")
            #com = False
            #recc = 0
        if serial and len(m.guitar) > 0 and m.g_dur[count5] == 0:
            if len(m.g_dur) > count5+step:
                count5=count5+step
            stop5 = True
            #if com and recc > 2:
            s.sendSerialMsg(ser, "goff")
            print("stop5")
            #com = False
            #recc = 0
        #print("step")
        time.sleep(0.01)


        if count1 < len(m.violin) and m.v_dur[count1] > 0:
            #print("play "+str(violin[count1])+" "+str(v_dur[count1]))
            m.v_dur[count1] = m.v_dur[count1]-step
            if stop1:
                stop1 = False
                start1 = True
        if count2 < len(m.bass) and m.b_dur[count2] > 0:
            #print("play "+str(violin[count1])+" "+str(v_dur[count1]))
            m.b_dur[count2] = m.b_dur[count2]-step
            if stop2:
                stop2 = False
                start2 = True
        if serial and count3 < len(m.record) and m.r_dur[count3] > 0:
            print("gonna play rec "+str(m.record[count3])+" dur "+str(m.r_dur[count3]))
            m.r_dur[count3] = m.r_dur[count3]-step
            if stop3:
                stop3 = False
                start3 = True
        if serial and count4 < len(m.compresor) and m.c_dur[count4] > 0:
            print("play com "+str(m.compresor[count4])+" dur "+str(m.c_dur[count4]))
            #print("play "+str(violin[count1])+" "+str(v_dur[count1]))
            m.c_dur[count4] = m.c_dur[count4]-step
            if stop4:
                stop4 = False
                start4 = True
        if serial and count5 < len(m.guitar) and m.g_dur[count5] > 0:
            print("play g "+str(m.guitar[count5])+" dur "+str(m.g_dur[count5]))
            #print("play "+str(violin[count1])+" "+str(v_dur[count1]))
            m.g_dur[count5] = m.g_dur[count5]-step
            if stop5:
                stop5 = False
                start5 = True
            
        # this row makes buzzer work for 1 second, then
        if start1 and m.violin[count1] > 0:
            buzzer1.ChangeFrequency(m.violin[count1])
            buzzer1.start(50) # Set dutycycle to 10
            start1 = False
            #print("sound start1")
        if start2 and m.bass[count2] > 0:
            buzzer2.ChangeFrequency(m.bass[count2])
            buzzer2.start(50) # Set dutycycle to 10
            start2 = False
            #print("sound start2")
        if  serial and start3 and m.record[count3] > 0:
            start3 = False
            print("sound start3")
            #if  rec == False and recc > 0.5:
            #    rec = True
            if ser:
                print("ser still ok here")
            s.sendSerialMsg(ser, "rec")
            #    recc = 0
        if  serial and start4 and m.compresor[count4] > 0:
            start4 = False
            print("sound start4")
            s.sendSerialMsg(ser, "com3")
        if  serial and start5 and m.guitar[count5] > 0:
            start5 = False
            print("sound start5")
            s.sendSerialMsg(ser, "gon")

        #time.sleep(0.1*v_dur[count1])
        time.sleep(m.tempo)
        recc = recc+m.tempo

    theEnd(ser)

if __name__ == '__main__':
    inp = ""
    note = ""
    length = 1
    #get args
    m = False
    serial = False
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")
        if i == 1:
            inp = arg
        if i == 2:
            note = arg
        if i == 3:
            length = arg
    if inp == "":
        print("melody, imperial_marsh, click, mario_bross, mario")
        inp = input() #3
        print(" loading "+inp)
    #loader = importlib.find_loader(inp)
    if inp == "freq":
        m = lambda: None
    if inp == "note":
        #do nothing

        m = importlib.import_module( "tones" ) #as m
    if inp == "note" or inp =="freq":
        
        m.violin = []
        m.bass = []
        m.record = []
        m.compresor = []
    if not inp == "note" and not inp == "freq" and not inp == "":    
        serial = True
        loader = importlib.util.find_spec(inp)
        if loader is not None:
            m = importlib.import_module( inp ) #as m
        else:
            print("not found exit")
            sys.exit()
    #import imperial_marsh as m
    #import melody as m
    print("play:"+inp+" "+note+" "+str(length)+" serial="+str(serial))
    play(m, inp, note, length, serial)
# Please find below some addictional commands to change frequency and
# dutycycle without stopping buzzer, or to stop buzzer:
#
# buzzer.ChangeDutyCycle(10)
# buzzer.ChangeFrequency(1000)
# buzzer.stop()
