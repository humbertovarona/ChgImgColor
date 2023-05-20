def replace_green_with_transparency(image_path, output_path):
    image = Image.open(image_path)
    image = image.convert("RGBA")
    pixel_data = image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixel = pixel_data[x, y]
            if pixel[1] > pixel[0] and pixel[1] > pixel[2]:
                pixel_data[x, y] = (0, 0, 0, 0)
    image.save(output_path, format=image.format)
