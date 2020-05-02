import tkinter
import bioGenerator
import chatWindow
import api
import random
from PIL import Image, ImageTk

def likeCat(catName, imgPath):
    chatWindow.chatWindow(catName, str(imgPath))
    current_index = current_index + 1

def dislikeCat():
    print("bye")
    current_index = current_index + 1

def getImage(current_index):
    imgPath = "img/cat" + str(current_index) + ".jpg"
    catName = bioGenerator.get_name()
    return (imgPath, catName)


window = tkinter.Tk()
window.title("RediCatz")
window.geometry("400x600")
window.configure(background='black')
window.resizable(False, False)

baseFrame = tkinter.Frame(window, width=400, height=100, background="Red")

current_index = random.randint(1, 100)

imgPath = "img/cat" + str(current_index) + ".jpg"
catName = bioGenerator.get_name()

label = tkinter.Label(
    text="RediCatz, Meet Cats in your Area",
    fg="white",
    bg="black"
)

name = tkinter.Label(
    text=catName,
    fg="white",
    bg="black"
)

description = tkinter.Text(
    window, height=6, width=50
)

description.insert(tkinter.END, bioGenerator.get_bio())
description.insert(tkinter.END, "\n\n")
description.insert(tkinter.END, bioGenerator.get_cat_fact())
description.configure(state='disabled')

like = tkinter.Button(baseFrame, text="Like", fg="green", width=10, height=2, command = lambda: likeCat(catName, imgPath))

dislike = tkinter.Button(baseFrame, text="Dislike", fg="red", width=10, height=2, command = dislikeCat)

loadedImage = Image.open(imgPath)
resize = loadedImage.resize((400, 400))

loadedImage = ImageTk.PhotoImage(resize)
labelimage = tkinter.Label(window, image=loadedImage)

label.grid(row=0, column=0)
labelimage.grid(row=1, column=0)
name.grid(row=2, column=0)
description.grid(row=3, column=0)
baseFrame.grid(row=4, column=0)

like.grid(row=0, column=1)
dislike.grid(row=0, column=0)

# label.pack()
# like.pack(side=tkinter.BOTTOM)
# dislike.pack(side=tkinter.BOTTOM)
# labelimage.pack()



window.mainloop()