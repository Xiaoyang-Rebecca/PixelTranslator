from Tkinter import *
import ttk
from  PIL import Image, ImageDraw, ImageOps
import pyscreenshot as ImageGrab
import os, subprocess
import time

width = 256
height = 256
center = height//2
white = (255)#, 255, 255)
green = (0,128,0)

lastx, lasty = 0, 0

def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

def addLine(event):
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y))
    lastx, lasty = event.x, event.y

def getter(widget):
    x=root.winfo_rootx()+widget.winfo_x()
    y=root.winfo_rooty()+widget.winfo_y()
    # x0 = int(canvas.canvasx(0))
    # y0 = int(canvas.canvasy(0))
    x1 = x+int(width)#widget.winfo_width()
    y1 = y+int(height)#widget.winfo_height()
    #print(x,y,x1,y1)
    #print(root.winfo_rootx(),root.winfo_rooty(),widget.winfo_x(),widget.winfo_y(),widget.winfo_width(),widget.winfo_height())
    ImageGrab.grab().crop((x,y,x1,y1)).save("temp.jpg")

root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = Canvas(root,width=width, height=height,bg='white')

# image1 = Image.new("L", (width, height), white)
# draw = ImageDraw.Draw(image1)

canvas.grid(column=0, row=0, sticky=(N, W, E, S))
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)
canvas.pack()
# button = Button (frame, text="Good-bye", command=getter(anvas))
# button.pack()

# getter(canvas)
# button=Button(root, text="Save", command=getter(canvas))
# #button=Button(root, text="Quit", command=quit)

# button.pack()
root.after(12000, lambda:getter(canvas))
root.after(13000, lambda: quit)#exit())
root.mainloop()

#process image
im=Image.new("RGB",(2*width,height),"white")
im1=Image.open("temp.jpg")
im1=ImageOps.invert(im1)
right=(width,0,2*width,height)
im.paste(im1,right)
im.save('GAN_demo/sample.jpg')

#send test image
os.system('scp /home/aditi/GAN_demo/sample.jpg xli63@uhpc.hpcc.uh.edu:/uhpc/roysam/xiaoyang/Project_leaf/Codes/pix2pix-tensorflow/datasets/GANinput_vein/test_demo') #fix this
print('Copied')

#run the test
os.system('ssh -X xli63@uhpc.hpcc.uh.edu nohup sbatch /uhpc/roysam/xiaoyang/demo_gan.sh')
time.sleep(300)
#copy back
os.system('scp xli63@uhpc.hpcc.uh.edu:/uhpc/roysam/xiaoyang/Project_leaf/Codes/pix2pix-tensorflow/test/GANoutput_demo/*.png /home/aditi/GAN_demo/')

os.system("xdg-open /home/aditi/GAN_demo/test_0001.png")
 