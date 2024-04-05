from PIL import Image
# Convert webp image to png
im = Image.open("/example/full/path.webp").convert("RGB")
im.save("/example/full/path/filename.png")
