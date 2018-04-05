import IHM

# User inputs
inputFile = "pics/test1.jpg"
inputStr = "You can't see me"

# Create a IHM class to start
ihm = IHM.IHM()

# Encrypt the message by inputting a image and a string
ihm.encrypt(inputStr, inputFile)

# Use the original image and encrypted version to see the hidden message
ihm.decrypt(inputFile, "output.png")

# Note that the order of inputs doesn't matter
ihm.decrypt("output.png", inputFile)
