# Author:   Hsuan-Hau Liu
# Date:     04/05/2018
# File:     IHM.py
# Descryption:  This is a module that allows user to hide message in an image.
# TODO: 1. right now, the first indicator has to be the first pixel,
#          and the last idicator has to be right after the last char of message.
#          Need to figure out a way to go around that.
#       2. If the number exceeds 255, it skips that pixel. Might be able to
#          subtract the number from RGB code to encode as well.
#       3. Can possibly add another encryption function for more secure message.

# open source library Pillow
from PIL import Image

class HMI:
    """ Image Hidden Message class """

    def encrypt(self, myStr, inFile, outFile = "output.png"):
        im = Image.open(inFile)

        # check if the image is big enough to hide the message
        if (len(myStr) + 2) > (im.size[0] * im.size[1]):
            print "Image is too small to store the message"
            return

        pixels = im.load()
        #im.show() # original image

        # add an indicator for beginning of message
        pixels[0, 0] = (pixels[0, 0][0] + 4, pixels[0, 0][1], pixels[0, 0][2])

        # ecrypt message into the image
        myList = self.decode_str(myStr)
        col = 1
        row = 0
        for tu in myList:
            temp = pixels[col, row]
            new_tu = (temp[0] + tu[0], temp[1] + tu[1], temp[2] + tu[2])

            # if the number goes out of range, skip the pixel
            while (new_tu[0] > 255 or new_tu[1] > 255 or new_tu[2] > 255):
                col += 1
                if col == im.size[0]:
                    col = 0     # reset col counter
                    row += 1    # move to next row

                    if row == im.size[1]:
                        print "Image is too small to store the message"
                        return

                temp = pixels[col, row]
                new_tu = (temp[0] + tu[0], temp[1] + tu[1], temp[2] + tu[2])

            pixels[col, row] = new_tu
            print temp, tu, pixels[col, row]
            col += 1
            if col == im.size[0]:
                col = 0     # reset col counter
                row += 1    # move to next row

                if row == im.size[1]:
                    print "Image is too small to store the message"
                    return

        # add another indicator for end of message
        pixels[col, row] = (pixels[col, row][0] + 4, pixels[col, row][1], pixels[col, row][2])

        #im.show()
        im.save(outFile)
        return

    def decrypt(self, file_1, file_2):
        im1 = Image.open(file_1)
        im2 = Image.open(file_2)

        if im1.size != im2.size:
            print "Incorrect inputs. These images don't match."
            return

        pix1 = im1.load()
        pix2 = im2.load()

        # check the order of the inputs
        if pix1[0, 0][0] - pix2[0, 0][0] != 4:
            # swap if pix1 is the original image
            if pix1[0, 0][0] - pix2[0, 0][0] == -4:
                temp = pix1
                pix1 = pix2
                pix2 = temp
            else:
                print "Incorrect inputs. These images don't match."
                return

        message = ""
        for row in range( im1.size[1] ):
            start = 0
            # ignore the first indicator
            if row == 0:
                start = 1

            for col in range( start, im1.size[0] ):
                # extracts the pixels
                p1 = pix1[col, row]
                p2 = pix2[col, row]

                # obtain differences
                t1 = p1[0] - p2[0]
                t2 = p1[1] - p2[1]
                t3 = p1[2] - p2[2]

                # if there is no difference, skip it
                if t1 + t2 + t3 == 0:
                    continue

                # check for indicator
                if t1 == 4:
                    print message
                    return

                # computer the ASCII code
                num = (t1 << 5) + (t2 << 3) + t3
                message += chr(num)

        print message
        return

    def decode_str(self, myStr):
        myList = [] # list of tuples containing decoded numbers
        for i in range( len(myStr) ):
            c = ord(myStr[i])   # ASCII code of this character
            t1 = c >> 5         # shift it to the right by 5 bits
            t2 = (c & 0x1F) >> 3    # only care about 4th and 5th bits from the right
            t3 = c & 0x07       # only care about the last three bits
            myList.append( (t1, t2, t3) )

        return myList
