import tkinter
from PIL import Image, ImageTk
import random

# top level widget which represents the main window of an application
root = tkinter.Tk()
root.geometry('400x400')
root.title('Dice Rolling Simulator')

# adding label into the frame

l0 = tkinter.Label(root, text="")
l0.pack()

# adding label with different font and formatting
l1 = tkinter.Label(root, text="Welcome to Dice Rolling Simulator!", fg="light green",
                   bg="dark green",
                   font="Helvetica 16 bold italic")
l1.pack()

# adding images into the list
dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']
# here i am randomise these images for getting dice number form 1 to 6
# i am storing this generated random image in variable image1

image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# lets construct the label widget for image

label_image = tkinter.Label(root, image=image1)
label_image.image = image1

# packing a widget in the parent widget
label_image.pack(expand=True)


# function activated by clicking the button

def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # upadte the image
    label_image.configure(image=image1)
    # keeping a reference
    label_image.image = image1


# now lets create the button widget
button = tkinter.Button(root, text="Roll the Dice",
                        fg="blue",
                        command=rolling_dice)
# pack this button widget into the parent widget
button.pack(expand=True)
# calling to the mainloop of Tk
# keeps window open
root.mainloop()
