import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
from sklearn.datasets import load_digits
from skimage.io import imread
from skimage.exposure import rescale_intensity
from skimage.transform import resize
from PIL import Image

digits = load_digits()
print(digits.data[:1])
model = KMeans(n_clusters=10, random_state=0)
model.fit(digits.data)

print('---------------------------')
print('---------------------------')
print('---------------------------')

img = resize(imread("test.png"), (8,8))
img = rescale_intensity(img, out_range=(0,16))
x_test = np.array(img)
print(x_test)

print('---------------------------')
print('---------------------------')
print('---------------------------')
x_test = x_test.transpose(2,0,1)
x_test = x_test[0].reshape(1,-1)

print(x_test)
prediction = model.predict(x_test)
print(prediction)
