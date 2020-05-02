import tkinter
import bioGenerator
import random
from PIL import Image, ImageTk

def getReply(catName):
    meowString = "meow"
    ranNo = random.randint(0, 10)

    for i in range(0, ranNo):
        meowString = meowString + " meow "

    reply = "\n" + catName + "> " + meowString
    return reply

def sendMsg(txtMsgBox, sendBox, catName):
    txtMsgBox.configure(state='normal')
    getInput = sendBox.get("1.0","end-1c")
    msg = "\n player> " + getInput
    txtMsgBox.insert(tkinter.END, msg)
    reply = getReply(catName)
    txtMsgBox.insert(tkinter.END, reply)
    txtMsgBox.configure(state='disabled')

def chatWindow(catName, img):
    window = tkinter.Tk()
    window.title("Chat")
    window.geometry("400x600")
    window.configure(background='black')
    window.resizable(False, False)

    baseFrame = tkinter.Frame(window, width=400, height=100)
    nameFrame = tkinter.Frame(window, width=400, height=100, background="Red")
    chatFrame = tkinter.Frame(window, width=400, height=400, background="White")

    label = tkinter.Label(
        text="RediCatz, Meet Cats in your Area",
        fg="white",
        bg="black"
    )

    name = tkinter.Label(nameFrame,
        text=catName,
        fg="white",
        bg="black"
    )

    txtMsgBox = tkinter.Text(
        window, height=30, width=50
    )
    messageToSend = catName + "> " + "Meow"
    txtMsgBox.insert(tkinter.END, messageToSend)
    txtMsgBox.configure(state='disabled')

    msgBox = tkinter.Text(
        baseFrame, height=2, width=20
    )
    
    send = tkinter.Button(baseFrame, text="Send", fg="Black", width=10, height=1, command = lambda: sendMsg(txtMsgBox, msgBox, catName))
    
    
    loadedImage = Image.open(img)
    resize = loadedImage.resize((20, 20))

    loadedImage = ImageTk.PhotoImage(resize)
    labelimage = tkinter.Label(nameFrame, image=loadedImage)

    label.grid(row=0, column=0)
    labelimage.grid(row=0, column=0)
    name.grid(row=0, column=1)
    txtMsgBox.grid(row=3, column=0)
    msgBox.grid(row=0, column=0)
    baseFrame.grid(row=4, column=0)
    nameFrame.grid(row=1, column=0)

    send.grid(row=0, column=1)


    window.mainloop()

chatWindow("Barry", "img/cat8.jpg")