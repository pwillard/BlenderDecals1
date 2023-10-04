#-------------------------------------------------------------------------------
# Name:        Generate NS MOW Gondola Reporting Marks
# Purpose:      For use with Blender 3.6 and OpenRails
#
# Author:      Pete willard
#
# Created:     04/10/2023
# Copyright:   (c) willard 2023
# Licence:     CC BY-SA 4.0 DEED
#
# Not the best written code...  but I cobbled it together in an afternoon
# and it does what I want.
#-------------------------------------------------------------------------------

from PIL import Image, ImageDraw, ImageFont

# Side numbering with space for ribs
text_lines = ["998 027","998 328","998 202","998 320","998 286","998 077","998 135","998 165","998 377","998 375"]

#end reporting marks
end_lines = ["NS998027","NS998328","NS998202","NS998320","NS998286","NS998077","NS998135","NS998165","NS998377","NS998375"]

# Generate the blank transparent image file as a starting image
# We might want it later as well
image = Image.new('RGBA', (1024, 1024), (0,0,0,0))
image.save('decal.tga', 'tga',transparency=0)
image.close()

# I could have started with a transparent image from a Bitmap tool...
# but I can also create one on-the-fly


# Open the blank file we created to use as a starting image
image_path = "decal.tga"
image = Image.open(image_path)

# Create a drawing context for the final image
draw = ImageDraw.Draw(image)

# Set text properties for car sides
font_color = (255, 255, 255)    # White color
font_path = 'nslogo.ttf'        # This ttf file is in the same folder
font_size = 64                  # Lettering Size
font = ImageFont.truetype(font_path, font_size)
text_x = 5                      # starting point for text
text_y = 5
line_spacing = 10


# Add each line of the SIDE text to the image
for line in text_lines:
    text_position = (text_x, text_y)

    draw.text(text_position, line, font=font, fill=font_color)

    # Get coordinates of text location.
    bbox = draw.textbbox(text_position,line , font=font)
    #draw.rectangle(bbox, outline="red") # If you like
    print ("Line ",line,bbox)  #print out the text coords

    # Move the Y coordinate down for the next line of text
    text_y += font_size + line_spacing


# The car ends have smaller text shuifted to the right
font_size = 32
text_x = 500                  # Back at the top again
text_y = 5                    # starting point for text
line_spacing = 20
font = ImageFont.truetype(font_path, font_size)


# Add the text to the image for the car ends
for line in end_lines:
    text_position = (text_x, text_y)

    draw.text(text_position, line, font=font, fill=font_color)
    #Get Text Coordinates
    bbox = draw.textbbox(text_position,line , font=font)
    print ("Line ",line,bbox)  #print text coords

    # Move the Y coordinate down for the next line of text
    text_y += font_size + line_spacing



# Save the resulting image with text on a transparent background
output_path = "decalresult.png"
image.save(output_path)

# Close the image
image.close()

print(f"Work Complete")
