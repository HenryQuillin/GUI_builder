# Henry Quillin 
# GUI_builder
# 2 - 9 - 2021 

from tkinter import *

master = Tk()
master.geometry('250x750')
master.configure(background="#222222")
master.title('GUI_builder')

#canvas = Canvas(master, width='300', height='300')

 

'''
counter= 0
def lines():
    global counter
    canvas_height=20
    canvas_width=200
    y = int(canvas_height / 2) 
    x1 = 0
    x2 = canvas_width
    y1 = 0
    y2 = 0
    canvas.create_line(x1, y1+counter, x2, y2 + counter)
    counter = counter + 50 
    print(counter)
    #for x in range(0, 100, 10):
        #canvas.create_line(x1, y1, x2, y2)
        #canvas.create_line(x1, y1+x, x2, y2 + x)
'''
def change_bg_color(color):
    master.configure(background=color)


#frame container 
frame = Frame(master)
frame.pack
bottomframe = Frame(master) 


#inputs and labels 
e1 = Entry(master) 
e2 = Entry(master) 
e3 = Entry(master) 
e4 = Entry(master) 
Label(master, text='First Name').pack()
e1.pack()
Label(master, text='Last Name').pack()
e2.pack()
Label(master, text='email').pack() 
e3.pack()
Label(master, text='password').pack() 
e4.pack()
'''
e4.pack()
e1.pack()
e2.pack()
e3.pack()
e4.pack()
'''

red_button = Button(master, text='bg to red', command=lambda color='red': change_bg_color('red'), bg="red", fg="red", highlightbackground="red",
                activebackground="red")
red_button.pack()
blue_button = Button(master, text='bg to blue', command=lambda color='blue': change_bg_color('blue'), bg="blue", fg="blue", highlightbackground="blue", activebackground="blue")
blue_button.pack()
green_button = Button(master, text='bg to green', command=lambda color='green': change_bg_color('green'), bg="green", fg="green", highlightbackground="green", activebackground="green")
green_button.pack()
orange_button = Button(master, text='bg to orange', command=lambda color='orange': change_bg_color('orange'), bg="orange", fg="orange", highlightbackground="orange", activebackground="orange")
orange_button.pack()

slider = Scale(master, from_=0, to=10,orient=HORIZONTAL) 
slider.pack()
slider = Scale(master, from_=100, to=1000, bg='gray',orient=HORIZONTAL)
slider.pack()

#checkbox
var1 = IntVar() 
Checkbutton(master, text='male', variable=var1).pack()
var2 = IntVar() 
Checkbutton(master, text='female', variable=var2).pack()
var3 = IntVar() 
Checkbutton(master, text='save password', variable=var1).pack()
var4 = IntVar() 
Checkbutton(master, text="don't save password", variable=var2).pack()

#text
text1 = Text(master, height=2, width=25, bg='#094882') 
text1.pack()
text1.insert(END, "Do you like my buttons?") 
text2 = Text(master, height=2, width=28, bg='#146fc4') 
text2.pack()
text2.insert(END, "I hope you like my buttons?") 


#radio_buttons 
v = IntVar() 
Radiobutton(master, text='chose me', variable=v, value=1).pack() 
Radiobutton(master, text='No me', variable=v, value=2).pack() 
Radiobutton(master, text='Just me', variable=v, value=3).pack() 
Radiobutton(master, text='pick me', variable=v, value=4).pack() 

#scrollbar
scrollbar = Scrollbar(master) 
scrollbar.pack(side=RIGHT) 
mylist = Listbox(master, yscrollcommand = scrollbar.set ) 
for line in range(100): 
   mylist.insert(END, 'scrolling' + str(line)) 
mylist.pack() 
scrollbar.config( command = mylist.yview ) 

#spinbox
w = Spinbox(master, from_ = 0, to = 10) 
w.pack()

#pop up 
top = Toplevel() 
top.title('This is my pop-up') 
top.mainloop()

#dropdown
menu = Menu(master) 
master.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='Drop down', menu=filemenu) 
filemenu.add_command(label='option1') 
filemenu.add_command(label='option2') 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=master.quit) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About')





master.mainloop()