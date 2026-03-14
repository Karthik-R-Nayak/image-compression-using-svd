import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
img = Image.open("mustang.jpeg").convert("L")
A = np.array(img)
m, n = A.shape
original_size = m * n
print("Original storage:", original_size, "values")
U, S, Vt = np.linalg.svd(A, full_matrices=False) #calculating svd values 
k_values = [5, 20, 50, 100]# Choose number of singular values
plt.figure(figsize=(10,8))

# Original Image
plt.subplot(2,3,1)
plt.title("Original")
plt.imshow(A, cmap="gray")
plt.axis("off")


for i,k in enumerate(k_values): #calculatingvalues of compresed images
    Ak = U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]
    compressed_size = k * (m + n + 1)
    reduction = 100 * (1 - compressed_size / original_size)
    print(f"k={k} -> compressed storage = {compressed_size} values ({reduction:.2f}% reduction)")
    plt.subplot(2,3,i+2)
    plt.title(f"k={k}")
    plt.imshow(Ak, cmap="gray")#  showing  compressed images
    plt.axis("off")

plt.tight_layout()
plt.show()
