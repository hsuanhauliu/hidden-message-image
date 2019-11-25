# Hidden Message Image

A simple program that allows you to hide messages in images.
>A picture is worth a thousand words.

## Getting started

Follow the instructions below to get started.

### Prerequisites

- Python >= 3.6
- [Pillow](https://github.com/python-pillow/Pillow) >= 5.3

### Installation

```
git clone https://github.com/hsuanhauliu/hidden-message-image.git
cd hidden-message-image
pip install .
```

### Usage

#### CLI

Follow the commands below to run the program.

```
hmi <encrypt/decrypt>
```

#### Import As Python Package

You can also import the package in your code. See the [iPython notebook](https://github.com/hsuanhauliu/hidden-message-image/blob/master/demo.ipynb) for a demo usage.

## Limitations

- Small pictures don't work well since it's "easier" to see the pixel changes. A ordinary photo would work perfectly.
- Since each character is encoded into each pixel, images whose dimension is smaller than the number of characters in the message won't be able to fit the entire message in the picture.
- Super white pixel color (RGB code (255, 255, 255)) is undesirable and will be skipped during encoding process.