# Hidden Message Image
A simple program that allows you to hide messages in an image.
>If they don't know that it's there, they can't hack it right? :L

## Getting started
Follow the instructions below to get started.
### Prerequisite
Open source library [Pillow](https://github.com/python-pillow/Pillow) is needed.
- Make sure you install the library in the correct library folder (depend on which version of python you are using).

### Installing
```
git clone https://github.com/hsuanhauliu/hidden-message-image.git
```

## Notes
- Small pictures don't work well since it's "easier" to see the pixel changes. A ordinary photo would work perfectly.
- Since each character is encoded into each pixel, images whose dimension is smaller than the number of characters in the message won't be able to fit the entire message in the picture.
- Super white pixel color (RGB code (255, 255, 255)) is undesirable and will be skipped during encoding process.

## My blog post
Read [here](https://howardliusite.wordpress.com/2018/04/06/image-hidden-message-ihm/) to find out more!
