import pytesseract
from PIL import Image

image=Image.open('D:\myproject\EAS_auto\EASauto\chinese\open.png')
code=pytesseract.image_to_string(image)
print(code)