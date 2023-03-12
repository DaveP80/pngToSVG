from PIL import Image
#convert png image to ico
logo = Image.open("C:\\Users\\example\\Downloads\\example.png")
 
logo.save("C:\\Users\\example\\Downloads\\example.ico", format='ICO',
          sizes=[(40, 40)])