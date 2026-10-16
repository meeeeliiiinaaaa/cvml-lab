
import cv2
import numpy as np


def apply_gaussian_blur(frame, kernel_size, sigma):
    k = max(1, int(kernel_size))
    if k % 2 == 0:          # kernel size must be odd
        k += 1
    return cv2.GaussianBlur(frame, (k, k), sigma)              # only horizontal bluring: cv2.GaussianBlur(frame, (k, 1), sigmaX=sigma, sigmaY=0)
                                                               # OpenCV calculate it from sigma: cv2.GaussianBlur(frame, (0, 0), sigmaX=sigma)
                                                               # cv2.GaussianBlur(frame, (k, k), sigmaX=sigma_x, sigmaY=sigma_y)


def apply_averaging_blur(frame, kernel_size):
    k = max(1, int(kernel_size))
    kernel = np.ones((k, k), dtype=np.float32) / (k * k)   # weights sum to 1
    return cv2.filter2D(frame, -1, kernel)                 # Use ddepth=-1 to keep the same depth as the input
                                                           # for zero padding: cv2.filter2D(frame, -1, kernel, borderType=cv2.BORDER_CONSTANT)


def apply_sobel_edge(frame, threshold):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) if len(frame.shape) == 3 else frame
    # if input is noisy: 
    # gray = cv2.GaussianBlur(gray, (5, 5), 0)
    gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    magnitude = np.sqrt(gx ** 2 + gy ** 2)
    magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    _, edges = cv2.threshold(magnitude, threshold, 255, cv2.THRESH_BINARY)
    return edges


def apply_canny_edge(frame, threshold):
    """
    Canny Edge Detection (Already Implemented).
    Uses the provided parameter as the lower bound and scales it for the upper bound.
    """
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) if len(frame.shape) == 3 else frame
    lower_bound = threshold
    upper_bound = threshold * 3
    return cv2.Canny(img, lower_bound, upper_bound)