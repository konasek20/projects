from tkinter import *
import autololko 

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # linkne co to tlačítko má udělat 
        exitButton = Button(self, text="Exit", command=autololko) 

        # poloha
        exitButton.place(x=100, y=120)

    def clickExitButton(self):
        exit()
        
root = Tk()
app = Window(root)
root.wm_title("Auto přimímač lolka")
root.geometry("320x200")
root.mainloop()
