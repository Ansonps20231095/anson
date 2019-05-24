import globalvariables

import time
import board
import neopixel

pixpin = board.A3
numpix = 128


strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)


def lookupColor(color,i):
    if color == 10:
        strip[i] = (0,0,0)
    # orange
    elif color == 11:
        strip[i] = (255,179,0)
    # yellow
    elif color == 12:
        strip[i] = (55,55,0)
    # green
    elif color == 13:
        strip[i] = (0,255,0)
    # blue
    elif color == 14:
        strip[i] = (0,0,255)
    # violet
    elif color == 15:
        strip[i] = (62,0,205)
    # red
    elif color == 17:
        strip[i] = (255,0,0)

    # light grey
    elif color == 20:
      strip[i] = (203,203,203)

    # white
    elif color == 40:
      strip[i] = (255,255,255)

    # grey
    elif color == 30:
      strip [i] = (90,90,90)


# ----------------------------------------------------------------------------------------------------
# START DO NOT MODIFY THE CODE BETWEEN THE ---
# ----------------------------------------------------------------------------------------------------


def showMessageL(nextMessage,duration,myMessage,startingPoint):
    # start - show Message
    if globalvariables.myStart == 0:
        globalvariables.myStart = 1
        globalvariables.countToMaxLength = startingPoint

    i = 0
    for r in range(0,8):
        for c in range(globalvariables.countToMaxLength,globalvariables.countToMaxLength+8):
            temp = c % len(myMessage[0])
            color = myMessage[r][temp]
            lookupColor(color,i)
            i += 1

    for r in range(0,8):
        for c in range(globalvariables.countToMaxLength+8,globalvariables.countToMaxLength+16):
            temp = c % len(myMessage[0])
            color = myMessage[r][temp]
            lookupColor(color,i)
            i += 1

    strip.write()

    globalvariables.countToMaxLength += 1
    globalvariables.durationCounter += 1
    if globalvariables.countToMaxLength > duration:
        globalvariables.countToMaxLength = 0
        globalvariables.myStart = 0
        globalvariables.durationCounter = 0
        globalvariables.messageID = nextMessage


# ----------------------------------------------------------------------------------------------------
# END DO NOT MODIFY THE CODE BETWEEN THE ---
# ----------------------------------------------------------------------------------------------------



while True:
    if globalvariables.messageID == 1:
        # Call function - showMessage(nextMessageID, messageDuration, message, start)
        showMessageL(2,16,globalvariables.message1,0)

    elif globalvariables.messageID == 2:
        # Call function - showMessage(nextMessageID, messageDuration, message, start)
        showMessageL(3,16,globalvariables.message2,0)

    elif globalvariables.messageID == 3:
        # Call function - showMessage(nextMessageID, messageDuration, message, start)
        showMessageL(4,16,globalvariables.message3,0)

    elif globalvariables.messageID == 4:
        # Call function - showMessage(nextMessageID, messageDuration, message, start)
        showMessageL(5,16,globalvariables.message4,0)

    elif globalvariables.messageID == 5:
        # Call function - showMessage(nextMessageID, messageDuration, message, start)
        showMessageL(1,16,globalvariables.message5,0)
