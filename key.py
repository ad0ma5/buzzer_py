import keyboard as kb
 
while True:
    print(kb.read_key())
    if kb.read_key() == "a":
        break

    kb.on_press_key("r", lambda _:print("You pressed r")) 
        
