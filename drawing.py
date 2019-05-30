from PIL import ImageTk,  ImageDraw, ImageFilter
import PIL 
from tkinter import *
import numpy as np 
import matplotlib.pyplot as plt

def imageprepare(argv):
    im = PIL.Image.open(argv).convert('L')
    width = float(im.size[0])
    height = float(im.size[1])
    newImage = PIL.Image.new('L', (28, 28), (255)) 
    img = im.resize((28, 28), PIL.Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
    tv = list(img.getdata())  
    tva = [(255 - x) * 1.0 / 255.0 for x in tv]
    return tva


class Draw_field:
    def __init__(self, width = 560, height = 560):
        self.width = 560
        self.height = 560
        center = height//2
        self.white = (255, 255, 255)
        green = (0,128,0)
        root = Tk()

        self.cv = Canvas(root, width=self.width, height=self.height, bg='white')
        self.cv.pack()

        self.image1 = PIL.Image.new("RGB", (self.width, self.height), self.white)
        self.draw = ImageDraw.Draw(self.image1)
        
        self.cv.pack(expand=YES, fill=BOTH)
        self.cv.bind("<B1-Motion>", self.paint)
        button=Button(text="predict",command=self.predict)
        button2 = Button(text='reset' , command = self.reset)
        button.pack()
        button2.pack()
        root.mainloop()

    def predict(self):
        filename = "temp.png"
        self.image1.save(filename)
        image = imageprepare(filename)
        image = np.array(image, dtype='float').reshape(784,1)
        pixels = image.reshape((28, 28))
        plt.imshow(pixels, cmap= 'gray_r')
        plt.show()

        #Do stuff .. 

    def paint(self, event):
        x1, y1 = (event.x - 10), (event.y - 10)
        x2, y2 = (event.x + 20), (event.y + 10)
        self.cv.create_oval(x1, y1, x2, y2, fill="black",width=20)
        self.draw.line([x1, y1, x2, y2],fill="black",width=30)

    def reset(self):
        self.cv.delete("all")
        self.image1 = PIL.Image.new("RGB", (self.width, self.height), self.white)
        self.image1.save("temp.png")
        self.draw = ImageDraw.Draw(self.image1)


draw = Draw_field()
