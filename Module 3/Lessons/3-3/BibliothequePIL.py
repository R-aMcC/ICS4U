from PIL import Image

def main():
    size = 20
    img = Image.open("sssss.jpg")
    img.show()

    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(size):
            pixels[i, j] = (0,0,0)

        for j in range(img.size[1]-size, img.size[1]):
            pixels[i, j] = (0,0,0)

    for j in range(img.size[1]):
        for i in range(size):
            pixels[i, j] = (0,0,0)

        for i in range(img.size[0]-size, img.size[0]):
            pixels[i, j] = (0,0,0)

    img.show()
    
    
if __name__ == "__main__":

    main()    
