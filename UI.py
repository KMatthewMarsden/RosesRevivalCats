import tkinter

window = tkinter.Tk()

label = tkinter.Label(
    text="Hello, World!",
    fg="white",
    bg="black",
    width=15,
    height=15
)

label.pack()


window.mainloop()