
import webbrowser
from tkinter import *
import tkinter as tk


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
    #set master
        self.master = master
        self.master.geometry('{}x{}'.format(500,500))

    #buttons
        #generate
        self.btn1=Button(self.master, text='Generate', width=10, height=1, command=self.gen)
        self.btn1.grid(row=0, column=0, padx=5, pady=5)
        #close
        self.btn2=Button(self.master, text='Close', width=10, height=1, command=self.close)
        self.btn2.grid(row=1, column=0, padx=5, pady=5)

    #textbox
        self.vartxt1 = StringVar()
        self.txt1=Entry(self.master, text=self.vartxt1, width=50, bg='lightgray')
        self.txt1.grid(row=0, column=1, columnspan=3, padx=5, pady=10)



    #definitions
    def close(self):
        self.master.destroy()   #closes program

    def gen(self):
        print('self.vartxt1.get()', self.vartxt1.get())
        f = open('index.html', 'w')
        f.write('''<!DOCTYPE html>
            <html lang = en>
                <head>
                    <meta charset='utf-8'>
                </head>
                <body>
                    <h1>
                        Stay tuned for our amazing summer sale!
                    </h1>
                </body>
            </html>''')
        webbrowser.open('index.html', 'w')

        


if __name__ == '__main__':
    root=tk.Tk()
    App=ParentWindow(root)
    root.mainloop()

