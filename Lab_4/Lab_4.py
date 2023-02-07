# Interdisciplinary Space Master: CVIA
# Authors: Elliott Wobler and Patrick Teyssier
# Winter 2022
from PIL import Image, ImageOps, ImageFilter
import numpy as np


def save_results(img, filename):
    output = "output/{}.jpg".format(filename)
    print("Storing results to {}...".format(output))
    img.save(output)


# 4. Read the image from the stored folder.
# Convert RGB image into grayscale (I_gray)
# Store the results for the report

I = Image.open("cubesat.jpg")
save_results(I, "I")
# Convert to grayscale (could also use `img.convert("L")`)
I_gray = ImageOps.grayscale(I)
# Store the results
save_results(I_gray, "I_gray")

# 5. Use Gaussian kernel to obtain the smoothened image I_blur.
# Use different radii and note the difference.
# Store the results for the report.


def gaussian_blur(img, radius):
    # Create Gaussian filter
    gauss_filter = ImageFilter.GaussianBlur(radius=radius)
    # Apply the Gaussian filter to blur the image
    img = img.filter(gauss_filter)
    return img


# Apply Gaussian blur to image
radius = 2
I_blur = gaussian_blur(I_gray, radius)
save_results(I_blur, "I_blur_rad{}".format(radius))
# Apply Gaussian blur to image with larger radius
radius = 4
I_blur_more = gaussian_blur(I_gray, radius)
save_results(I_blur_more, "I_blur_rad{}".format(radius))


# 6. Compute image gradients along x-direction (Gx) using the horizontal Sobel filter.
# Store the results for the report.


def sobel_filter(img, kernel):
    # `ImageFilter.Kernel` creates a convolution kernel.
    # The current version only supports 3x3 and 5x5 integer and floating point kernels.
    size = (3, 3)  # (width, height)
    offset = 0
    scale = 1
    # Create the filter
    filter = ImageFilter.Kernel(size, kernel, scale, offset)
    # Apply the filter to the base image
    img = img.filter(filter)
    return img


# Create horizontal Sobel filter
sobel_horizontal = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]).flatten()
# Apply the horizontal Sobel filter to the base image
Gx = sobel_filter(I_blur, sobel_horizontal)
# Store the results
save_results(Gx, "Gx")

# 7. Compute image gradients along y-direction (Gy) using vertical Sobel filter.
# Store the results for the report.

# Create vertical Sobel filter
sobel_vertical = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]]).flatten()
# Apply the vertical Sobel filter to the base image
Gy = sobel_filter(I_blur, sobel_vertical)
# Store the results
save_results(Gy, "Gy")

# 8. Finally compute the gradient amplitude image (Gamp).
# Store the results for the report.
# Convert images into numpy arrays for calculation.
# Report all the obtain results (I, I_gray, I_blur, Gx, Gy, Gamp) and the code.
# Also, describe briefly how calculating gradients using Sobel filters can detect edges.

# By calculating X and Y gradients, we determine the change in pixel intensity in each direction.
# A significant change in either direction indicates an edge.
# A significant change in both directions indicates a corner.


def output_Gamp(Gamp, filename):
    # Normalize
    Gamp = Gamp / Gamp.max() * 255
    # Convert to correct data type
    Gamp = Gamp.astype(np.int8)
    # Convert back to grayscale PIL image from Numpy array
    Gamp = Image.fromarray(Gamp, "L")
    # Store the results
    save_results(Gamp, filename)


# Convert images to Numpy arrays
Gx = np.array(Gx)
Gy = np.array(Gy)
# Square the terms element-wise
dx2 = np.square(Gx)
dy2 = np.square(Gy)
# Perform the square root
Gamp = np.sqrt(dx2 + dy2)
output_Gamp(Gamp, "Gamp_full")
# Use the simplified method (no squares or roots)
Gamp = Gx + Gy
output_Gamp(Gamp, "Gamp_simple")
