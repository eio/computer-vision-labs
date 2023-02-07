# Data

## Training

Training data is stored in `data/train/`

It consists of 24 RGBA images that are 100x100 pixels.

The first 12 contain a CubeSat frame, and the second 12 do not.

## Testing

Testing data is stored in `data/test/`

It consists of 6 RGBA images that are 100x100 pixels.

The first 3 contain a CubeSat frame, and the second 3 do not.

# Code

## Python Notebook

`Labs_5-6.ipynb`

This file is meant to be run one block at a time, and contains the original lab instructions.

## Adapted Python Notebook for Raspberry Pi Deployment

`train_test_model.py`

This file contains an adaptation of the `.ipynb` code which enables it to both train on the original dataset and test single input images.

This file requires a single command-line input, and supports two modes.

### Mode 1: Model Training

`python3 train_test_model.py train`

Running in "train" mode will output the trained weights and bias in two output files.

Weights are saved to `learned_weights.txt` and bias saved to `learned_bias.txt`.

### Mode 2: Test Model on Single Input Image using Loaded Weights and Bias

`python3 train_test_model.py image_to_test.jpg`

Running in the second mode will result in the script first loading `learned_weights.txt` and `learned_bias.txt`.

The script will then load the image with the specified filename and test it against the trained model.

If the model successfully detects a satellite in the input image, it will output: `Model predicted: [1]`

If the model does not detect a satellite in the input image, it will output: `Model predicted: [0]`

## Shell Script for Raspberry Pi Integration

`raspberry_pi_classifier.sh`

This script initiates an infinite loop that captures an image with the Raspberry Pi camera every 2 seconds, and tests it against the trained classifier with `python3 train_test_model.py captured_image.jpg`, printing the classification result as described above.

Captured image filenames use the timestamp at which the image was captured, and are stored in `data/pix/`.

Given the minimal time required to capture and test an image, the timer interval of 2 seconds could be reduced if desired by the user.


