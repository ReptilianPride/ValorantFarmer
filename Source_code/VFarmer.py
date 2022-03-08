import pyautogui
import time

def record():
    return pyautogui.position()

def wait():
    time.sleep(5)
    
def press(key):
    pyautogui.keyDown(key)
    time.sleep(2)
    pyautogui.keyUp(key)
    time.sleep(0.3)
    
def moveAround():
    for key in "dadawsdadaawsdaddad":
        press(key)

print("*"*20)
print("VALO-Farmer Version2 by CipherKill")
print("*"*20)
print("Instructions:")
print("[1]Tell where the location of 'skip' button is after deathmatch")
print("[2]Tell where the location of the 'play again' button is after deathmatch")
print("[3]Follow futher instructions")
print("-"*20)
input("\nPress [RETURN] to start program...\n")
input("Press [RETURN] to snap mouse location->1")
skipButton=record()
input("Press [RETURN] to snap mouse location->2")
playAgain=record()
print("\nUSE CTRL+C OR CTRL+Z TO STOP PROGRAM\n")
time.sleep(1)
print("Farming in progress...")
time.sleep(0.5)
print("[!]Shift to VALORANT now!")
time.sleep(5)
i=int(0)
while(True):
    i=i+1
    print("[Iter]:",i)
    pyautogui.click(skipButton)
    print("[Clicked skip]")
    time.sleep(1)
    pyautogui.click(playAgain)
    print("[Clicked play]")
    time.sleep(1)
    print("[Moving]")
    moveAround()
    
