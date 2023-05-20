def replace_black_and_seismic_with_transparency(image_path, output_path):
    image = Image.open(image_path)
    image = image.convert("RGBA")
    pixel_data = image.load()
    threshold = 50
    for y in range(image.height):
        for x in range(image.width):
            pixel = pixel_data[x, y]
            if pixel[0] <= threshold and pixel[1] <= threshold and pixel[2] <= threshold:
                pixel_data[x, y] = (0, 0, 0, 0)
    image.save(output_path, format=image.format) 
