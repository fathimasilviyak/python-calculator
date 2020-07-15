from tkinter import *

#creating window for calculator
window=Tk()
window.geometry("400x500+500+150")
window.title("Calculator")
window.configure(background="black")
#creating diaplay screen
display_screen = Label(window, text="0", font=("Serif", 40), fg="white", bg="#1F2333", anchor=NE)





display_screen.place(x=25, y=30, width=350, height=80)

window.mainloop()