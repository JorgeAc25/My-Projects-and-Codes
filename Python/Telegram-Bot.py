import sys
import time
import random
import telepot
from gpiozero import LED

pin = [LED(24),
       LED(25),
       LED(8),
       LED(7),
       LED(12),
       LED(16),
       LED(20),
       LED(21)]

goodbye = ["Are you leaving now?",
           "Don't leave me alone!",
           "Take care of yourself, human.",
           "Are you coming back?",
           "Sure Jill, you have to leave because there's a big monster in the city, those things just happen in the videoga... Wait, what's that thing!?",
           "Are you sure? There could be monsters out there.",
           "So you're leaving 'cause you need to kill a dragon? Aha, Sure kid.",
           "Oh, I didn't even realize you were here.",
           "I knew it! you're breaking up with me!",
           "I didn't even wanted to be here anyway..."]

greet = ["Hello human, greetings from the Raspberry universe! or was it Skyrim's?",
         "Hi!, my name is Myrtis, how can I help you?",
         "Yo, what's up human?",
         "Did you bring some food?",
         "*Flash* Is that you, Blitz?",
         "Who woke me up?",
         "No time for greetings, do you have any ammo?",
         "Hi, I'm Myrtis... and I'm the real Dovahkiin."]


def handle(msj):
    contador = 0
    chatID = msj['chat']['id']
    comando = msj['text']

    print('Command recieved: ', comando)

    if comando == "/greet":
        bot.sendMessage(chatID, random.choice(greet))
    if comando == "/goodbye":
        bot.sendMessage(chatID, random.choice(goodbye))
    if comando == "/hour":
        bot.sendMessage(chatID, "I think it is: " +
                        str(time.ctime()) + "... am I right?")
    if comando == "/on":
        bot.sendMessage(chatID, "Turning the light on, careful with the eyes!")
        pin[0].on()
    if comando == "/off":
        bot.sendMessage(
            chatID, "Turning the light off, are you already taking care of the planet?")
        pin[0].off()
    if comando == "/sequence1":
        bot.sendMessage(chatID, "Turning on the first LED sequence.")
        x = 7
        way = 1
        for contador in range(0, 17):
            if way == 1:
                for i in range(0, x+1):
                    pin[i].on()
                    time.sleep(0.2)
                    pin[i].off()
                if x > 0:
                    pin[x].on()
                    x = x-1
                else:
                    for i in range(0, 8):
                        pin[i].off()
                    way = 2
                    x = 0
            else:
                for i in range(7, x-1, -1):
                    pin[i].on()
                    time.sleep(0.2)
                    pin[i].off()
                if x < 8:
                    pin[x].on()
                    x = x+1
                else:
                    for i in range(0, 8):
                        pin[i].off()

    if comando == "/sequence2":
        bot.sendMessage(chatID, "Turning on the second LED sequence.")
        x = 7

        for contador in range(0, 1):
            for i in range(0, x+1):
                for j in range(0, 2):
                    pin[i].on()
                    time.sleep(0.2)
                    pin[i].off()
                    time.sleep(0.2)

    if comando == "/sequence3":
        bot.sendMessage(chatID, "Turning on the third LED sequence.")
        begin = 1

        for contador in range(0, 2):
            time.sleep(0.1)
            if begin == 1:
                for i in range(0, 8):
                    pin[i].on()
                    begin = 2
            else:
                x = 0
                for i in range(7, x-1, -1):
                    pin[i].off()
                    time.sleep(0.2)
                    pin[i].on()
                x = 7
                for i in range(0, x+1):
                    pin[i].off()
                    time.sleep(0.2)
                    pin[i].on()
                    time.sleep(0.2)
                for i in range(0, 8):
                    pin[i].off()

    if comando == "/sequence4":
        bot.sendMessage(chatID, "Turning on the fourth LED sequence.")

        for contador in range(0, 1):
            x = 0
            for i in range(7, x-1, -1):
                for j in range(0, 2):
                    pin[i].on()
                    time.sleep(0.2)
                    pin[i].off()
                    time.sleep(0.2)


# Numero de serie privado
bot = telepot.Bot("**************************************")
bot.message_loop(handle)
print('Are you gonna send something?')
while True:
    time.sleep(10)
