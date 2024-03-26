from PIL import Image

#1
obrazek = Image.open("blesk.jpg")
sirka, vyska = obrazek.size

for x in range(sirka):
    for y in range(vyska):
        r, g, b = obrazek.getpixel((x,y))

        R = int(min((0.393 * r) + (0.769 * g) + (0.189 * b), 255))
        G = int(min((0.349 * r) + (0.686 * g) + (0.168 * b), 255))
        B = int(min((0.272 * r) + (0.534 * g) + (0.131 * b), 255))

        obrazek.putpixel((x,y), (R, G, B))

obrazek.show()
