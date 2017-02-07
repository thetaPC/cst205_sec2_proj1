#proj1.py
#name, abstract like software design

from PIL import Image


def medianOdd(myList):
    # Store list length in the variable listLength
    listLength = len(myList)
    # Sort the list
    sortedValues = sorted(myList)
    # Location of middle value. Subtract one because of zero index
    middleIndex = ((listLength + 1)/2) - 1
    # Return the object located at that index
    return sortedValues[middleIndex]


# create the list that will store all the images that need comparing
imageList = []

# adds all the images in folder Project1Images into the imageList
for i in range(0, 9):
    imageList.append(Image.open("Project1Images/" + str(i + 1) + ".png"))
    
# gets the size of an image from imageList since they're all the same size
imgWidth, imgHeight = imageList[0].size

# creates the lists for RGB
redPixelList = []
greenPixelList = []
bluePixelList = []

# for img in imageList:
#     print img
#     print "images above"


# creates the new image that will be used to input the median RGB 
newImg = Image.new("RGB", (imgWidth, imgHeight))

# loops pixel by pixel to save the individual RBG for each image (9)
for x in range(0, imgWidth):
    for y in range(0, imgHeight):
        for currImg in imageList:
            red, green, blue = currImg.getpixel((x,y))
            # saves individual RGB into appropriate lists
            redPixelList.append(red)
            greenPixelList.append(green)
            bluePixelList.append(blue)
            
        # median for each list are returned for RGB
        medRed = medianOdd(redPixelList)
        medGreen = medianOdd(greenPixelList)
        medBlue = medianOdd(bluePixelList)
        
        # must clear the RBG list else it will not have individual pixel info
        redPixelList = []
        greenPixelList = []
        bluePixelList = []
        
        # grabs the median RGB and places it in the new image of the current pixel
        newImg.putpixel((x,y), (medRed, medGreen, medRed))
 
# saves the image in the current directory   
newImg.save("noNoise.png", "PNG")        
        
        
print "done"


#.save