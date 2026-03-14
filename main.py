import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from svd_compress import compress_grayscale, compress_color


# ---- USER CHOICE ----
mode = input("Choose compression type (grayscale/color): ").strip().lower()     # choose: "color" or "grayscale"
image_path = "mustang.jpeg"

img = Image.open(image_path)

if mode == "grayscale":
    img = img.convert("L")

A = np.array(img)

k_values = [5, 20, 50, 100]

plt.figure(figsize=(10,8))

plt.subplot(2,3,1)
plt.title("Original")
plt.imshow(A, cmap="gray" if mode=="grayscale" else None)
plt.axis("off")


for i, k in enumerate(k_values):

    plt.subplot(2,3,i+2)

    if mode == "grayscale":
        Ak = compress_grayscale(A, k)
        plt.imshow(Ak, cmap="gray")

    else:
        Ak = compress_color(A, k)
        plt.imshow(Ak)

    plt.title(f"k={k}")
    plt.axis("off")


plt.tight_layout()
plt.show()
