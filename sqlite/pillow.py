from PIL import Image

image = Image.open("/Users/ferdaozturk/Desktop/humans.jpg")

image.save("hujmans2.jpg")

image.rotate(180).save("humans3.jpg")

image.convert(mode="L").save("humans4.jpg")

degistir = (960,600)

image.thumbnail(degistir)
image.save("humans5.jpg")

#image.filter(ImageFilter.GaussianBlur(10).save("kus7.jpg"))

kirpilacak_alan= (340,0,950,600)

image.crop(kirpilacak_alan).save("humans6.jpg")