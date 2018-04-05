# image-hidden-message
This is a simple program that allows you to hide messages in an image.

Open source library [Pillow](https://github.com/python-pillow/Pillow) is needed.

Note:
- It's better to use an ordinary picture like a photo for this, since there are instances where this program may fail (need further improvement).
- Since each character is encoded into each pixel, images whose dimension is too small won't be able to fit every character in them.
- Super white pixel color (RGB code (255, 255, 255)) is undesirable and will be skipped during encoding process.

