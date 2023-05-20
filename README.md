# ChgImgColor

Changing colors in images

# Date-released 

2023-01-09

# Version

1.0


# Requirements

```shell
# pip install Pillow 
```

## Installation

```python
import pytesseract
from PIL import Image, ImageDraw
from PIL import Image 
```
# Usage Examples

```python
target_color = (254, 26, 25)
image_path = "/home/varona/PycharmProjects/delAllLabels/test.png"
output_path = "/home/varona/PycharmProjects/delAllLabels/new_test.png"

start_color = (168, 16, 16)
end_color = (218, 21, 21)
replacement_color = (0, 255, 0)

replace_color_with_transparency(image_path, output_path, target_color)

substitute_color(image_path, output_path, target_color, replacement_color)

substitute_color_range(image_path, output_path, start_color, end_color, replacement_color)

substitute_color_range_with_transparency(image_path, output_path, start_color, end_color)

replace_gray_with_transparency(image_path, output_path)

replace_red_with_transparency(image_path, output_path)

replace_green_with_transparency(image_path, output_path)

replace_blue_with_transparency(image_path, output_path)

replace_yellow_with_transparency(image_path, output_path)

replace_black_and_seismic_with_transparency(image_path, output_path)

replacement_color_with_opacity = (255, 0, 0, 255) 

replace_black_and_seismic_with_color(image_path, output_path, replacement_color_with_opacity)   
```


