from PIL import Image, ImageFilter

img = Image.open("./Backgrounds/background1.jpeg")
blurred_img = img.filter(ImageFilter.BLUR)
blurred_img.save("blur.png")

resize_img = img.resize((100, 100))
resize_img.save("resized.png")

rotate_img = img.rotate(90)
rotate_img.thumbnail((100, 100))
rotate_img.save("thumbnail.png")