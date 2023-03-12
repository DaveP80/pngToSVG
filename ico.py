from PIL import Image
 
logo = Image.open("C:\\Users\\example\\Downloads\\example.png")
 
logo.save("C:\\Users\\example\\Downloads\\example.ico", format='ICO',
          sizes=[(40, 40)])