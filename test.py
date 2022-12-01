import sys
import importlib

print("hi")
inp =  ""
#inp = raw_input() #2
inp = input() #3
print("importing "+inp)
importlib.import_module( inp )
sys.exit()
