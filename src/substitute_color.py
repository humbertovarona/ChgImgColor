def substitute_color(image_path, output_path, target_color, replacement_color):
    image = Image.open(image_path)
    image = image.convert("RGBA")
    pixel_data = image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixel = pixel_data[x, y]
            if pixel[:3] == target_color:
                pixel_data[x, y] = (*replacement_color, pixel[3])
    image.save(output_path, format=image.format)
