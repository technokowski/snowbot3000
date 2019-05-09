import os
import random

class Speaker():

    def __init__(self, name="-v alex ", rate="-r 100 "):
        self.name = str(name)
        self.rate = str(rate)

    def __repr__(self):
        iamwhoiam = "I am who I am"
        return repr(iamwhoiam)

    def speak(self, words):
        words = self.stripper(words)
        os.system('say ' + self.name + self.rate + str(words))

    def change_rate(self, rate):
        self.rate = "-r " + rate + " "

    def change_voice(self, name):
        self.name = "-v " + name + " "

    def stripper(self, stripped_word):
        stripped_word = stripped_word.replace("'","")
        return stripped_word

    def singer(self, word):
        word = self.stripper(word)
        few_vals = ['40', '50', '60']
        few_rates = ['-r 90', '-r 120', '-r 170', '-r 100', '-r 150']
        os.system('say ' + self.name + random.choice(few_rates) + " [[pbas " + random.choice(few_vals) +"]]" + str(word))
