import PIL
import PIL.Image

def main():
    img = PIL.Image.new("RGB", (255, 255), "red")

    pixels = img.load()
    img.show()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels[i, j] = (i, j, 150)

    img.show()


if __name__ == "__main__":
    main()

