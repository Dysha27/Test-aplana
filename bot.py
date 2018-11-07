import random
import datetime
import os
import sys

path = "Test"
now = datetime.datetime.now()


class myMenu:
    items = []

    def AddItem(self, text, function):
        self.items.append({"text": text, "func": function})

    def Show(self):
        c = 1
        for l in self.items:
            print c, l["text"], "\n"
            c = c + 1

    def Do(self, n):
        try:
            self.items[n]["func"]()
        except IndexError:
            print("Error")


def chat_local():
    while True:
        word_you = raw_input("You: ")  # type: str
        if word_you == "quit":
            quit()
        elif word_you == "change":
            global path
            path = edit_file()
        elif word_you == "date":
            print ("Bot: " + str(now.date()))
        elif word_you == "time":
            print ("Bot: " + str(now.time()))
        elif word_you == "silent":
            silent()
        else:
            print ("Bot: " + random.choice([line for line in open(path, "r")])[:-1])


def edit_file():
    while True:
        path = raw_input("Enter the path:")  # type: str
        if os.path.exists(path):
            if os.path.isfile(path):
                print("File found!")
                return path
            elif os.path.isdir(path):
                print("Directory path entered!")
        else:
            print ("Object not found")


def silent():
    while True:
        word_you = raw_input("You: ")  # type: str
        if word_you == "quit":
            sys.exit()
        if word_you == "getUp":
            print("Bot: Hi, I woke up!")
            chat_local()


def quit():
    print "bye"
    sys.exit(0)


if __name__ == "__main__":
    m = myMenu()
    m.AddItem("Write bot", chat_local)
    m.AddItem("Quit", quit)

while True:
    m.Show()
    n = input("Enter the number>")
    m.Do(n - 1)
