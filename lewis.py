from PIL import Image, ImageDraw, ImageFont

prefix = "[Lewis.Diagramz]: "

lewis_dot_possible = True
atomicnum = 1
group = 1
valence = 0
element = input("Please input the symbol of your element:\n")

print()

im = Image.new('RGBA', (500, 500), (0, 0, 0, 0))
draw = ImageDraw.Draw(im)

with open("./periodic_table.txt", "r") as pt:
    
    table = pt.read().replace("\n", "")
    
    
    
    # Get group, atomic number and valence electrons
    if element in table:
        atomicnum = table.replace("/// ", "").replace("\r", "").index(element) / 4 + 1
        group = 1
        if atomicnum > 55:
            atomicnum += 15
        if atomicnum > 88:
            atomicnum += 15
        
        current_group = 1
        isElement = False
        i = 0
        
        if element == "Uuo":
            group = 18
            isElement = True
        
        while not isElement:
            
            if i + 4 > len(table) - 1:
                break
            current = table[i:i+4]
            
            if current_group > 18:
                current_group = 1
            if element.ljust(4, " ") == current:
                group = current_group
                isElement = True
                break
            
            i += 4
            current_group += 1
        
        if group > 2 and group < 13:
            print(prefix + "Could not find valence electrons.")
            lewis_dot_possible = False
        elif group > 12:
            valence = group - 10
            if element == "He":
                valence = 2
        else:
            valence = group

# Prepare for image creation
font = ImageFont.truetype("./Merriweather-Regular.ttf", 250)
dots = [
    (175, 75, 225, 125),
    (425, 175, 475, 225),
    (175, 400, 225, 450),
    (50, 275, 100, 325),
    (275, 75, 325, 125),
    (425, 275, 475, 325),
    (275, 400, 325, 450),
    (50, 175, 100, 225),
       ]

# Create image
if lewis_dot_possible:
    if len(element) == 1:
        draw.text((150,100), element, (0, 0, 0), font=font)
    else:
        draw.text((100,100), element, (0, 0, 0), font=font)
    for i in range(valence):
        draw.ellipse(dots[i], fill=(0,0,0))
    im.save("./exports/" + element + ".png")
    print(prefix + "Image saved as '" + element + ".png' in the exports folder.")