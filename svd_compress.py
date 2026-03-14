import numpy as np

def svd_decompose(A):
    """
    Compute SVD of matrix A
    """
    U, S, Vt = np.linalg.svd(A, full_matrices=False)
    return U, S, Vt


def reconstruct_matrix(U, S, Vt, k):
    """
    Reconstruct matrix using top k singular values
    """
    return U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]


def compress_grayscale(A, k):
    """
    Compress grayscale image using SVD
    """
    U, S, Vt = svd_decompose(A)
    return reconstruct_matrix(U, S, Vt, k)


def compress_color(A, k):
    """
    Compress RGB image using SVD (channel-wise)
    """
    channels = []

    for i in range(3):
        channel = A[:, :, i]
        U, S, Vt = svd_decompose(channel)
        compressed_channel = reconstruct_matrix(U, S, Vt, k)
        channels.append(compressed_channel)

    compressed = np.stack(channels, axis=2)

    return np.clip(compressed, 0, 255).astype(np.uint8)