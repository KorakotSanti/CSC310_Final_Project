import tkinter as tk
from PIL import Image, ImageDraw

class DigitRecognition:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Image Recognition")
        self.canvas = tk.Canvas(self.root,width=500, height=350,highlightthickness=1, highlightbackground="black", bg="white")
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<Button-3>', self.delete)
        self.canvas.grid(row=0)
        self.predictB = tk.Button(self.root, text="Predict", width=25, bg="yellow", command=self.changeText).grid(row=1)
        self.result = tk.StringVar()
        self.result.set("Empty")
        self.label = tk.Label(self.root, textvariable=self.result).grid(row=2)
        self.image=Image.new("LA",(500,350),(255,255))
        self.draw=ImageDraw.Draw(self.image)
        self.root.mainloop()

    def changeText(self):
        # resize image and save as a png
        file='test.png'
        img = self.image.resize((8,8))
        img.save(file)

        self.image=Image.new("LA",(500,350),(255,255))
        self.draw=ImageDraw.Draw(self.image)
        self.result.set("yes")

    def delete(self, event):
        self.canvas.delete('all')

    def paint(self, event):
        color = 'black'
        x1, y1 = (event.x-1), (event.y-1)
        x2, y2 = (event.x+1), (event.y+1)
        self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color, width=40)
        self.draw.line([x1,y1,x2,y2], fill=color, width=40)
if __name__ == "__main__":  
    DigitRecognition()
