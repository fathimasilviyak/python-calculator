from tkinter import *


#creating window for calculator
from tkinter import Button

window=Tk()
window.geometry("+500+150")
window.title("Calculator")
window.configure(background="black")
#creating diaplay screen
display_screen = Label(window,
                       text="0",
                       font=("Serif", 40),
                       pady=20,
                       fg="white",
                       bg="#1F2333",
                       borderwidth=20,
                       relief="sunken",
                       anchor=E)
btn_clr = Button(window,
             text="C",
             width=4,
             bg="#434B69", fg="white",
             font=("Serif 24 bold"))
btn_open = Button(window,
             text="(",
             width=4,
             bg="#434B69", fg="white",
             font=("Serif 24 bold"))
btn_close = Button(window,
             text=")",
             width=4,
             bg="#434B69", fg="white",
             font=("Serif 24 bold"))
btn_div = Button(window,
               text="/",
               width=4,
               bg="#434B69", fg="white",
               font=("Serif 24 bold"))
btn_7 = Button(window,
             text="7",
             width=4,
             bg="#141933", fg="white",
             font=("Serif 24 bold"))
btn_8 = Button(window,
             text="8",
             width=4,
             bg="#141933", fg="white",
             font=("Serif 24 bold"))
btn_9 = Button(window,
             text="9",
             width=4,
             bg="#141933", fg="white",
             font=("Serif 24 bold"))
btn_mul = Button(window,
               text="x",
               width=4,
               bg="#434B69", fg="white",
               font=("Serif 24 bold"))
btn_4 = Button(window,
             text="4",
             width=4,
             bg="#141933", fg="white",
             font=("Serif 24 bold"))
btn_5 = Button(window,
             text="5",
             width=4,
             bg="#141933", fg="white",
             font=("Serif 24 bold"))
btn_6 = Button(window,
             text="6",
             width=4,
             bg="#141933", fg="white",
             font=("Serif 24 bold"))
btn_minus = Button(window,
               text="-",
               width=4,
               bg="#434B69", fg="white",
               font=("Serif 24 bold"))
btn_1 = Button(window,
             text="1",
             width=4,
             bg="#141933", fg="white",
             font=("Serif 24 bold"))
btn_2 = Button(window,
             text="2",
             width=4,
             bg="#141933", fg="white",
             font=("Serif 24 bold"))
btn_3 = Button(window,
             text="3",
             width=4,
             bg="#141933", fg="white",
             font=("Serif 24 bold"))
btn_plus = Button(window,
               text="+",
               width=4,
               bg="#434B69", fg="white",
               font=("Serif 24 bold"))
btn_0 = Button(window,
             text="0",
             width=4,
             bg="#141933", fg="white",
             font=("Serif 24 bold"))
btn_dot = Button(window,
             text=".",
             width=4,
             bg="#141933", fg="white",
             font=("Serif 24 bold"))
btn_equal = Button(window,
             text="=",
             width=4,
             bg="#149DDD", fg="white",
             font=("Serif 24 bold"))




display_screen.grid(row=0, columnspan=4, sticky="nsew")
btn_clr.grid(row=1, column=0)
btn_open.grid(row=1, column=1)
btn_close.grid(row=1, column=2)
btn_div.grid(row=1, column=3)
btn_7.grid(row=2, column=0)
btn_8.grid(row=2, column=1)
btn_9.grid(row=2, column=2)
btn_mul.grid(row=2, column=3)
btn_4.grid(row=3, column=0)
btn_5.grid(row=3, column=1)
btn_6.grid(row=3, column=2)
btn_minus.grid(row=3, column=3)
btn_1.grid(row=4, column=0)
btn_2.grid(row=4, column=1)
btn_3.grid(row=4, column=2)
btn_plus.grid(row=4, column=3)
btn_0.grid(row=5, column=0, columnspan=2, sticky="snew")
btn_dot.grid(row=5, column=2)
btn_equal.grid(row=5, column=3)
window.mainloop()