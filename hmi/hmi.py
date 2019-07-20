"""
    Author:   Hsuan-Hau Liu
    Date:     04/05/2018
    File:     HMI.py
    Descryption:  This is a module that allows user to hide message in an image.
    TODO: 1. right now, the first indicator has to be the first pixel,
             and the last idicator has to be right after the last char of message.
             Need to figure out a way to go around that.
          2. If the number exceeds 255, it skips that pixel. Might be able to
             subtract the number from RGB code to encode as well.
          3. Can possibly add another encryption function for more secure message.
"""


from PIL import Image


def encrypt(message, input_file, output_file="output.png"):
    """ Encrypt input message in the input image """
    img = Image.open(input_file)

    # check if the image is big enough to hide the message
    if (len(message) + 2) > (img.size[0] * img.size[1]):
        raise AttributeError("Image is too small to store the message")

    pixels = img.load()

    # add an indicator for beginning of message
    pixels[0, 0] = (pixels[0, 0][0] + 4, pixels[0, 0][1], pixels[0, 0][2])

    # ecrypt message into the image
    characters = decode_str(message)
    row, col = 0, 1
    for tu in characters:
        temp = pixels[col, row]
        new_tu = (temp[0] + tu[0], temp[1] + tu[1], temp[2] + tu[2])

        # if the number goes out of range, skip the pixel
        while (new_tu[0] > 255 or new_tu[1] > 255 or new_tu[2] > 255):
            col += 1
            if col == img.size[0]:
                col = 0     # reset col counter
                row += 1    # move to next row
                if row == img.size[1]:
                    raise AttributeError("Image is too small to store the message")

            temp = pixels[col, row]
            new_tu = (temp[0] + tu[0], temp[1] + tu[1], temp[2] + tu[2])

        pixels[col, row] = new_tu
        col += 1
        if col == img.size[0]:
            col = 0     # reset col counter
            row += 1    # move to next row
            if row == img.size[1]:
                raise AttributeError("Image is too small to store the message")

    # add another indicator for end of message
    pixels[col, row] = (pixels[col, row][0] + 4, pixels[col, row][1], pixels[col, row][2])
    img.save(output_file)
    print('New image created.')


def decode_str(message):
    """ Decode message to tuples to add to image pixels """
    res = [] # list of tuples containing decoded numbers
    for char in message:
        c = ord(char)           # ASCII code of this character
        t_1 = c >> 5            # shift it to the right by 5 bits
        t_2 = (c & 0x1F) >> 3   # only care about 4th and 5th bits from the right
        t_3 = c & 0x07          # only care about the last three bits
        res.append((t_1, t_2, t_3))

    return res


def decrypt(img_file_1, img_file_2):
    """ Decrypt the images to get the hidden message """
    img_1, img_2 = Image.open(img_file_1), Image.open(img_file_2)

    if img_1.size != img_2.size:
        raise AttributeError("Image sizes don't match.")

    pix_1, pix_2 = img_1.load(), img_2.load()

    # check the order of the inputs
    if pix_1[0, 0][0] - pix_2[0, 0][0] != 4:
        # swap if pix1 is the original image
        if pix_1[0, 0][0] - pix_2[0, 0][0] == -4:
            pix_1, pix_2 = pix_2, pix_1
        else:
            raise AttributeError("Image sizes don't match.")

    message = ""
    for row in range(img_1.size[1]):
        start = 0
        # ignore the first indicator
        if row == 0:
            start = 1

        for col in range(start, img_1.size[0]):
            # extracts the pixels
            p_1, p_2 = pix_1[col, row], pix_2[col, row]

            # obtain differences
            t_1, t_2, t_3 = p_1[0] - p_2[0], p_1[1] - p_2[1], p_1[2] - p_2[2]

            # if there is no difference, skip it
            if t_1 + t_2 + t_3 != 0:
                # check for end indicator
                if t_1 == 4:
                    return message

                # computer the ASCII code
                num = (t_1 << 5) + (t_2 << 3) + t_3
                message += chr(num)

    return message
