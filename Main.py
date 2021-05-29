from PIL import Image, ImageDraw #Подключим необходимые библиотеки.

image = Image.open("go.png") #Открываем изображение.
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования.
width = image.size[0] #Определяем ширину.
height = image.size[1] #Определяем высоту.
pix = image.load() #Выгружаем значения пикселей.

x = ''

for i in range(300):
	for j in range(1):
		if(pix[i, j][3] == 255):
			x += '0'
		else:
			x += '1'

print(x)
