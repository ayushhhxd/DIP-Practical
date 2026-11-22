import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the sample image in grayscale
img = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    raise FileNotFoundError(
        "image.jpg not found. Keep it in the same folder as this program."
    )

# Define image-processing kernels
kernels = {
    "Original": np.array([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]),
    "Blur": np.ones((3, 3), np.float32) / 9,
    "Sharpen": np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ]),
    "Edge Detection": np.array([
        [-1, -1, -1],
        [-1, 8, -1],
        [-1, -1, -1]
    ]),
    "Emboss": np.array([
        [-2, -1, 0],
        [-1, 1, 1],
        [0, 1, 2]
    ]),
    "Sobel X": np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ]),
    "Sobel Y": np.array([
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ])
}

# Apply each kernel and display the results
plt.figure(figsize=(12, 9))

for i, (name, kernel) in enumerate(kernels.items(), start=1):
    if name == "Original":
        result = img
    else:
        result = cv2.filter2D(img, -1, kernel)

    plt.subplot(3, 3, i)
    plt.imshow(result, cmap="gray")
    plt.title(name)
    plt.axis("off")

    output_name = name.lower().replace(" ", "_") + ".jpg"
    cv2.imwrite(output_name, result)

plt.tight_layout()
plt.savefig("filter_results.png")
plt.show()

print("All filters applied. Output images have been saved.")
