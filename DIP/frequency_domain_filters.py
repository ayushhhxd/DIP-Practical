
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image.jpg", 0)

rows, cols = img.shape
crow, ccol = rows//2, cols//2

fft = np.fft.fft2(img)
shift = np.fft.fftshift(fft)

mask = np.zeros((rows, cols), np.uint8)
cv2.circle(mask, (ccol, crow), 30, 1, -1)

low_pass = shift * mask
high_pass = shift * (1 - mask)

low = np.abs(np.fft.ifft2(np.fft.ifftshift(low_pass)))
high = np.abs(np.fft.ifft2(np.fft.ifftshift(high_pass)))

images = [img, np.log1p(np.abs(shift)), low, high]
titles = ["Original", "Frequency Spectrum", "Low Pass Filter", "High Pass Filter"]

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
