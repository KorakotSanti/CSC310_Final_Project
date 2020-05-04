import tkinter as tk
import numpy as np
from PIL import Image, ImageDraw, ImageGrab
from skimage.io import imread
from skimage.exposure import rescale_intensity
from skimage.transform import resize
from joblib import load

class DigitRecognition:
    
    def __init__(self):
        # The entire GUI itself
        self.root = tk.Tk()
        self.root.title("Image Recognition")

        # add a Canvas where you will draw the digit
        self.canvas = tk.Canvas(self.root,width=400, height=400,highlightthickness=3, highlightbackground="blue", bg="black")

        # add a motion command so that when you hold down mouse button 1 it will draw
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.grid(row=0)

        # The string value of result
        self.result = tk.StringVar()
        self.result.set("Empty")

        # label to display the prediction
        self.label = tk.Label(self.root, textvariable=self.result).grid(row=1)

        # predict Button
        self.predictB = tk.Button(self.root, text="Predict", width=25, bg="yellow", command=self.predictDigit).grid(row=2)

        # clear Button, clear the canvas for new drawing
        self.clearB = tk.Button(self.root, text="Clear", width=25, bg="white", command=self.delete).grid(row=3)

        # A new image that will be drawn
        self.image = Image.new("LA",(400,400))
        self.draw=ImageDraw.Draw(self.image)

        # load our classifer model
        self.model = load('KNN_model.joblib')

        # To run the GUI
        self.root.mainloop()

    def imgprocess(self):
        # need to resize image to 8x8
        tempimg = np.array(self.image)
        newimg = resize(tempimg, (8,8))

        # rescale image from value of 0-255 to value 0-16
        newimg = rescale_intensity(newimg, out_range=(0,16))

        imgdata = np.array(newimg)
        imgdata = imgdata.transpose(2,0,1)
        imgdata = imgdata[0].reshape(1,-1)

        return imgdata

    def predictDigit(self):
        # resize image and save as a png
        file='test.png'
        self.image.save(file)
        testdata = self.imgprocess()
        res = self.model.predict(testdata)

        self.result.set(str(res[0]))

    def delete(self):
        self.image=Image.new("LA",(400,400))
        self.draw=ImageDraw.Draw(self.image)
        self.canvas.delete('all')
        self.result.set("empty")

    def paint(self, event):
        inkwidth=10
        color = 'white'
        x1, y1 = (event.x-1), (event.y-1)
        x2, y2 = (event.x+1), (event.y+1)
        self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color, width=inkwidth)

        self.draw.point([x1,y1,x2,y2], fill=color)

if __name__ == "__main__":  
    DigitRecognition()
