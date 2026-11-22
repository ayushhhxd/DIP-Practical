
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image.jpg", 0)

mean = cv2.blur(img, (5, 5))
gaussian = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 5)

images = [img, mean, gaussian, median]
titles = ["Original", "Mean Filter", "Gaussian Filter", "Median Filter"]

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
