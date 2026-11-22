
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image.jpg", 0)

laplacian = cv2.Laplacian(img, cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)

kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

sharp = cv2.filter2D(img, -1, kernel)

blur = cv2.GaussianBlur(img, (5, 5), 0)
unsharp = cv2.addWeighted(img, 1.5, blur, -0.5, 0)

images = [img, laplacian, sharp, unsharp]
titles = ["Original", "Laplacian", "Sharpening Kernel", "Unsharp Masking"]

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
