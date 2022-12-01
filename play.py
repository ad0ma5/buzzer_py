
# Import required libraries
import sys
import RPi.GPIO as GPIO
import time
import importlib
import test_serial as s
ser = s.connectSerial()
inp = ""
#print(f"Arguments count: {len(sys.argv)}")
for i, arg in enumerate(sys.argv):
    #print(f"Argument {i:>6}: {arg}")
    if i == 1:
        inp = arg
if inp == "":
    print("melody, imperial_marsh, click, mario_bross, mario")
    inp = input() #3
    print(" loading "+inp)
#loader = importlib.find_loader(inp)
loader = importlib.util.find_spec(inp)
if loader is not None:
    m = importlib.import_module( inp ) #as m
else:
    print("not found exit")
    sys.exit()
#import imperial_marsh as m
#import melody as m

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
size = len(m.violin)
if len(m.bass) > size: 
    size = len(m.bass)
start1 = False
start2 = False
stop1 = True
stop2 = True
count1 = 0
count2 = 0
step = 1
rec = False
com = False
recc = 0
#for note in range( size ):
while count1 < len(m.violin)-1:
    if m.v_dur[count1] == 0:
        if len(m.v_dur) > count1+step:
            count1=count1+step
        stop1 = True
        buzzer1.stop()
        if rec and recc > 2:
            s.sendSerialMsg(ser, msg = "roff")
            rec = False
            recc = 0
        #print("stop1")
    if m.b_dur[count2] == 0:
        if len(m.b_dur) > count2+step:
            count2=count2+step
        stop2 = True
        buzzer2.stop()
        if com and recc > 2:
            s.sendSerialMsg(ser, msg = "coff")
            com = False
            recc = 0
        #print("stop2")

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
        
    # this row makes buzzer work for 1 second, then
    if start1 and m.violin[count1] > 0:
        buzzer1.ChangeFrequency(m.violin[count1])
        buzzer1.start(50) # Set dutycycle to 10
        if  rec == False and recc > 0.5:
            rec = True
            s.sendSerialMsg(ser, msg = "rec")
            recc = 0
        start1 = False
        #print("sound start1")
    if start2 and m.bass[count2] > 0:
        buzzer2.ChangeFrequency(m.bass[count2])
        buzzer2.start(50) # Set dutycycle to 10
        if  com == False and recc > 0.5:
            com = True
            s.sendSerialMsg(ser, msg = "com1")
            recc = 0
        start2 = False
        #print("sound start2")

    #time.sleep(0.1*v_dur[count1])
    time.sleep(m.tempo)
    recc = recc+m.tempo


# cleanup will free PINS and exit will terminate code execution
s.sendSerialMsg(ser, "coff", True)
time.sleep(1)
s.sendSerialMsg(ser, "roff", True)
time.sleep(1)
s.closeSerial(ser)
print("serial off, exitting")
GPIO.cleanup()
sys.exit()

# Please find below some addictional commands to change frequency and
# dutycycle without stopping buzzer, or to stop buzzer:
#
# buzzer.ChangeDutyCycle(10)
# buzzer.ChangeFrequency(1000)
# buzzer.stop()
