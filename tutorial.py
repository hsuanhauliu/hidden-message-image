import HMI

# User inputs
inputFile = "pics/test1.jpg"
inputStr = "You can't see me"

# Create a IHM class to start
hmi = HMI.HMI()

# Encrypt the message by inputting a image and a string
hmi.encrypt(inputStr, inputFile)

# Use the original image and encrypted version to see the hidden message
hmi.decrypt(inputFile, "output.png")

# Note that the order of inputs doesn't matter
hmi.decrypt("output.png", inputFile)
