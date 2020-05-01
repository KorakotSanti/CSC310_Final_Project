import tkinter as tk
from PIL import Image, ImageDraw, ImageGrab
from skimage.io import imread
from skimage.exposure import rescale_intensity
from skimage.transform import resize

class DigitRecognition:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Image Recognition")
        self.canvas = tk.Canvas(self.root,width=500, height=350,highlightthickness=1, highlightbackground="blue", bg="black")
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.grid(row=0)
        self.result = tk.StringVar()
        self.result.set("Empty")
        self.label = tk.Label(self.root, textvariable=self.result).grid(row=1)
        self.predictB = tk.Button(self.root, text="Predict", width=25, bg="yellow", command=self.predictDigit).grid(row=2)
        self.clearB = tk.Button(self.root, text="Clear", width=25, bg="white", command=self.delete).grid(row=3)
        self.image=Image.new("LA",(500,350))
        self.draw=ImageDraw.Draw(self.image)
        self.root.mainloop()

    def predictDigit(self):
        # resize image and save as a png
        file='test.png'
        img = self.image.resize((500,350))
        img.save(file)
        self.result.set("yes")

    def delete(self):
        self.image=Image.new("LA",(500,350))
        self.draw=ImageDraw.Draw(self.image)
        self.canvas.delete('all')

    def paint(self, event):
        inkwidth=10
        color = 'white'
        x1, y1 = (event.x-1), (event.y-1)
        x2, y2 = (event.x+1), (event.y+1)
        self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color, width=inkwidth)

        self.draw.point([x1,y1,x2,y2], fill=color)

if __name__ == "__main__":  
    DigitRecognition()
