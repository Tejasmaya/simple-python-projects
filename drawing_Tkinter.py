# '''
# Steps for creating Paint or Drawing Application in Python Tkinter
# Step 1: Create a Python file with .py extension and import all the necessary libraries
# '''

# from tkinter import filedialog, messagebox
# from tkinter import *
# from tkinter.ttk import Scale
# from tkinter import colorchooser, filedialog, messagebox
# from typing_extensions import Self
# import PIL.ImageGrab as ImageGrab

# '''
# Tkinter is a Python package for creating graphical user interfaces. It’s simple to use and comes packaged with Python. We can use GUI applications to visualize our data. PIL.ImageGrab package is used to save the image file on our local computer.

# Before importing all the packages it is required to install them in our working directories. For this particular project, we need to install Tkinter and pillow packages. You can install these packages using the pip command in your terminal.

# Command to install Tkinter :

# pip install tk
# Command to install pillow:

# pip install pillow
# This command will begin downloading and installing Tkinter-related packages. Once completed, a notification indicating successful installation will display.

# Step 2: Defining a Class and Creating a Tkinter Window GUI
# '''

# class Draw():
#     def __init__(self,root):
#         self.root =root
#         self.root.title("Copy Assignment Painter")
#         self.root.geometry("810x530")
#         self.root.configure(background="white")
#         self.root.resizable(0,0)


# '''
# Now we will create a class having the class name Draw() and define __init__. After that, we can call Tkinter Constructor but for this particular application, we have called root as a constructor.

# self.root.title : To define the title of our GUI Application.
# self.root.geometry : To define the size of the Window.
# self.root.resizable(0,0) : By using this property we cannot increase or decrease the size of the root window.
# '''

# if __name__ == "__main__":
#     root = Tk()
#     p = Draw(root)
#     root.mainloop()

# # root.mainloop() is used for holding the GUI of our Application.

# '''
# Step 3: Creating Widgets for our Tkinter Window
# 1. Code for the color Panel(on left side of drawing application in tkinter):
# '''

# # Pick a color for drawing from color pannel
# self.pick_color = LabelFrame(self.root,text='Colors',font =('arial',15),bd=5,relief=RIDGE,bg="white")
# self.pick_color.place(x=0,y=40,width=90,height=185)
# colors = ['blue','red','green', 'orange','violet','black','yellow','purple','pink','gold','brown','indigo']
# i=j=0
# for color in colors:
#     Button(self.pick_color,bg=color,bd=2,relief=RIDGE,width=3,command=lambda col=color:self.select_color(col)).grid(row=i,column=j)
#     i+=1
#     if i==6:
#         i=0
#         j=1

# '''
# We have initialized pick_color as our LabelFrame and placed it on the root. After that, we can define various attributes such as text, color, background color, height, width, ridge, and many more according to our requirements.

# We can define the colors required for painting using Lists. For each and every color palette we will create a button using a for loop where (i = row and j= column).  

# When the user clicks on the color button then it will execute the following command: command=lambda col=color:self.select_color(col).

# 2. Code for Eraser, Reset, Background Color, and Save buttons(left side options in drawing app in Python):
# '''

# # Erase Button and its properties  
# self.eraser_btn= Button(self.root,text="Eraser",bd=4,bg='white',command=self.eraser,width=9,relief=RIDGE)
# self.eraser_btn.place(x=0,y=197)

# # Reset Button to clear the entire screen
# self.clear_screen= Button(self.root,text="Clear Screen",bd=4,bg='white',command= lambda : self.background.delete('all'),width=9,relief=RIDGE)
# self.clear_screen.place(x=0,y=227)

# # Save Button for saving the image in local computer
# self.save_btn= Button(self.root,text="ScreenShot",bd=4,bg='white',command=self.save_drawing,width=9,relief=RIDGE)
# self.save_btn.place(x=0,y=257)

# # Background Button for choosing color of the Canvas
# self.bg_btn= Button(self.root,text="Background",bd=4,bg='white',command=self.canvas_color,width=9,relief=RIDGE)
# self.bg_btn.place(x=0,y=287)

# '''
# When a user clicks on the buttons then the following functions will be called.

# self.eraser_btn : command=self.eraser
# self.clear_screen : command= lambda : self.background.delete(‘all’)
# self.save_btn : command=self.save_drawing
# self.bg_btn : command=self.canvas_color
# 3. Code for creating a Scale for Pen(Pointer) and Eraser:
# '''

# self.pointer_frame= LabelFrame(self.root,text='size',bd=5,bg='white',font=('arial',15,'bold'),relief=RIDGE)
# self.pointer_frame.place(x=0,y=320,height=200,width=70)

# self.pointer_size =Scale(self.pointer_frame,orient=VERTICAL,from_ =48 , to =0, length=168)
# self.pointer_size.set(1)
# self.pointer_size.grid(row=0,column=1,padx=15)

# '''
# For this application we are using ttk scale bar so we need to import this from Tkinter using the following command:
# '''

# from tkinter.ttk import Scale

# '''
# After that, we initialize pointer_size to Scale and place it on pointer_frame. Here we need to define orient = VERTICAL as by default the orientation is horizontal. The default value is set to 1 using self.pointer_size.set(1) command.

# 4. Code for Creating the Canvas:
# '''

# #Defining a background color for the Canvas
# self.background = Canvas(self.root,bg='white',bd=5,relief=GROOVE,height=470,width=680)
# self.background.place(x=80,y=40)


# #Bind the background Canvas with mouse click
# self.background.bind("<B1-Motion>",self.paint)

# '''
# Here, self.background has been set to Canvas and placed on self.root. Then a canvas would be made, but we couldn’t draw anything on it. Therefore, in order to achieve that goal, the following code must be used: self.background.bind(“B1-Motion>”,self.paint).

# Step 4: Defining Functions for GUI Drawing Application Program
# 1. Function for Drawing the lines on Canvas:
# '''

# def paint(self,event):      
#         x1,y1 = (event.x-2), (event.y-2)  
#         x2,y2 = (event.x+2), (event.y+2)  

# '''
# Here is where the paint function that is invoked during binding is defined.

# Four variables are declared and designated as x1, y1, x2, and y2 in this function, defining the starting point and ending position of the mouse movement.

# 2. Function for choosing the color of pointer:
# '''


# def select_color(self, col):
#     self.pointer = col

# '''
# The pointer’s default color is black, but once the select_color function is defined and the self.pointer is initialized to the col, the default color is changed to the chosen color.

# 3. Function for defining the eraser:
# '''

# def eraser(self):
#         self.pointer= self.erase

# '''
# 4. Function for choosing the background color of the Canvas:
# '''

# def canvas_color(self):
#         color=colorchooser.askcolor()
#         self.background.configure(background=color[1])
#         self.erase= color[1]

# '''
# Now for choosing the background color of Canvas we need to import using

# from tkinter import colorchooser command

# color=colorchooser.askcolor():  This code will open up a dialog box for choosing a wide range of colors for the background of Canvas.
# self.background.configure(background=color[1]) : This code will change the background color of Canvas from default color to chosen color.
# self.erase= color[1]:  This code will change the color of the eraser from the default color to chosen color.
# 5. Function for saving the image file in Local Computer:
# '''


# def save_drawing(self):
#      try:
#             # self.background update()
#             file_ss = filedialog.asksaveasfilename(defaultextension='jpg')
#             print(file_ss)
#             x = self.root.winfo_rootx() + self.background.winfo_x()
#             print(x, self.background.winfo_x())
#             y = self.root.winfo_rooty() + self.background.winfo_y()
#             print(y)

#             x1 = x + self.background.winfo_width()
#             print(x1)
#             y1 = y + self.background.winfo_height()
#             print(y1)
#             ImageGrab.grab().crop((x, y, x1, y1)).save(file_ss)
#             messagebox.showinfo(
#                 'Screenshot Successfully Saved as' + str(file_ss))

#      except:
#             print("Error in saving the screenshot")

# '''
# Now to save the image file we need to import using the following commands:

# '''

# from tkinter import filedialog,messagebox
# import PIL.ImageGrab as ImageGrabfrom 

# '''
# filedialog.asksaveasfilename(defaultextension=’jpg’) :  This code will keep the default extension of the file as .jpg format for saving.
# self.root.winfo_rootx() + self.background.winfo_x(): This code will return the info root window with respect to the x-axis.
# self.root.winfo_rooty() + self.background.winfo_y(): This code will return the info root window with respect to the y-axis.
# x + self.background.winfo_width(): This code will return the width of the window.
# y + self.background.winfo_height():  This code will return the height of the window.
# ImageGrab.grab().crop((x , y, x1, y1)).save(file_ss): This code will save the image file to the local computer.
# '''


############################################################################################################################################################################################################################################################################################################################################################


# Drawing Application Using Python

# importing all the necessary Libraries

from tkinter import *
from tkinter.ttk import Scale
from tkinter import colorchooser, filedialog, messagebox
import PIL.ImageGrab as ImageGrab


# Defining Class and constructor of the Program
class Draw():
    def __init__(self, root):

        # Defining title and Size of the Tkinter Window GUI
        self.root = root
        self.root.title("Copy Assignment Painter")
        #         self.root.geometry("810x530")
        self.root.configure(background="white")
        #         self.root.resizable(0,0)

        # variables for pointer and Eraser
        self.pointer = "black"
        self.erase = "white"

        # Widgets for Tkinter Window

        # Configure the alignment , font size and color of the text
        text = Text(root)
        text.tag_configure("tag_name", justify='center', font=(
            'arial', 25), background='#292826', foreground='orange')

        # Insert a Text
        text.insert("1.0", "Drawing Application in Python")

        # Add the tag for following given text
        text.tag_add("tag_name", "1.0", "end")
        text.pack()

        # Pick a color for drawing from color pannel
        self.pick_color = LabelFrame(self.root, text='Colors', font=(
            'arial', 15), bd=5, relief=RIDGE, bg="white")
        self.pick_color.place(x=0, y=40, width=90, height=185)

        colors = ['blue', 'red', 'green', 'orange', 'violet', 'black',
                  'yellow', 'purple', 'pink', 'gold', 'brown', 'indigo']
        i = j = 0
        for color in colors:
            Button(self.pick_color, bg=color, bd=2, relief=RIDGE, width=3,
                   command=lambda col=color: self.select_color(col)).grid(row=i, column=j)
            i += 1
            if i == 6:
                i = 0
                j = 1

        # Erase Button and its properties
        self.eraser_btn = Button(self.root, text="Eraser", bd=4,
                                 bg='white', command=self.eraser, width=9, relief=RIDGE)
        self.eraser_btn.place(x=0, y=197)

        # Reset Button to clear the entire screen
        self.clear_screen = Button(self.root, text="Clear Screen", bd=4, bg='white',
                                   command=lambda: self.background.delete('all'), width=9, relief=RIDGE)
        self.clear_screen.place(x=0, y=227)

        # Save Button for saving the image in local computer
        self.save_btn = Button(self.root, text="ScreenShot", bd=4,
                               bg='white', command=self.save_drawing, width=9, relief=RIDGE)
        self.save_btn.place(x=0, y=257)

        # Background Button for choosing color of the Canvas
        self.bg_btn = Button(self.root, text="Background", bd=4,
                             bg='white', command=self.canvas_color, width=9, relief=RIDGE)
        self.bg_btn.place(x=0, y=287)

        # Creating a Scale for pointer and eraser size
        self.pointer_frame = LabelFrame(self.root, text='size', bd=5, bg='white', font=(
            'arial', 15, 'bold'), relief=RIDGE)
        self.pointer_frame.place(x=0, y=320, height=200, width=70)

        self.pointer_size = Scale(
            self.pointer_frame, orient=VERTICAL, from_=48, to=0, length=168)
        self.pointer_size.set(1)
        self.pointer_size.grid(row=0, column=1, padx=15)

        # Defining a background color for the Canvas
        self.background = Canvas(
            self.root, bg='white', bd=5, relief=GROOVE, height=700, width=1420)
        self.background.place(x=80, y=40)

        # Bind the background Canvas with mouse click
        self.background.bind("<B1-Motion>", self.paint)

    # Functions are defined here

    # Paint Function for Drawing the lines on Canvas

    def paint(self, event):
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)

        self.background.create_oval(
            x1, y1, x2, y2, fill=self.pointer, outline=self.pointer, width=self.pointer_size.get())

    # Function for choosing the color of pointer
    def select_color(self, col):
        self.pointer = col

    # Function for defining the eraser
    def eraser(self):
        self.pointer = self.erase

    # Function for choosing the background color of the Canvas
    def canvas_color(self):
        color = colorchooser.askcolor()
        self.background.configure(background=color[1])
        self.erase = color[1]

    # Function for saving the image file in Local Computer
    def save_drawing(self):
        try:
            # self.background update()
            file_ss = filedialog.asksaveasfilename(defaultextension='jpg')
            # print(file_ss)
            x = self.root.winfo_rootx() + self.background.winfo_x()
            # print(x, self.background.winfo_x())
            y = self.root.winfo_rooty() + self.background.winfo_y()
            # print(y)

            x1 = x + self.background.winfo_width()
            # print(x1)
            y1 = y + self.background.winfo_height()
            # print(y1)
            ImageGrab.grab().crop((x, y, x1, y1)).save(file_ss)
            messagebox.showinfo(
                'Screenshot Successfully Saved as' + str(file_ss))

        except:
            print("Error in saving the screenshot")


if __name__ == "__main__":
    root = Tk()
    p = Draw(root)
    root.mainloop()
