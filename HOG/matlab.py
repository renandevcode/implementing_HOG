import cv2
import matplotlib.pyplot as plt
from skimage.feature import hog
from skimage import exposure

img = cv2.imread('imagem_hog.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

hog_fv, hog_image = hog(
    gray,
    orientations=9,
    pixels_per_cell=(8,8),
    cells_per_block=(2, 2),
    visualize=True,
    feature_vector=True
)

hog_image_rescaled = exposure.rescale_intensity(
    hog_image, in_range=(0, 5)
)

plt.imshow(hog_image_rescaled, cmap='gray')
plt.axis('off')
plt.show()
print(hog_fv)

