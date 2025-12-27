import cv2
import matplotlib.pyplot as plt
from skimage.feature import hog
from skimage import exposure

img=cv2.imread('128x64.jpeg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

CS=8
hog_features, hog_image=hog(
    gray,
    orientations=9,
    pixels_per_cell=(CS, CS),
    cells_per_block=(2, 2),
    block_norm='L2-Hys',
    visualize=True,
    feature_vector=True
)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(gray, cmap='gray')
plt.title('Input Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(hog_image, cmap='gray')
plt.title('HOG Features')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(gray, cmap='gray')
plt.imshow(hog_image, cmap='hot', alpha=0.5)
plt.title('Image + HOG')
plt.axis('off')

plt.tight_layout()
plt.imshow(gray,cmap='gray')

print(len(hog_features)) 