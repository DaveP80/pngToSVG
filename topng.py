import cairosvg
from PIL import Image
from io import BytesIO

def convert_svg_to_png(input_file, output_file):
    # Convert SVG to PNG using cairosvg
    with open(input_file, 'rb') as svg_file:
        svg_content = svg_file.read()
        png_content = cairosvg.svg2png(bytestring=svg_content)

    # Create an Image object from the PNG content
    png_image = Image.open(BytesIO(png_content))

    # Save the Image object as PNG
    png_image.save(output_file, format='PNG')

input_svg ='example.svg'
output_png = 'example.png'
convert_svg_to_png(input_svg, output_png)
