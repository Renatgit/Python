class Rectangle:
    def __init__(self, width, height):
        self.width=width
        self.height=height
    def square(self):
        s=self.width*self.height
        print(f"Площадь вашего прямоугольника равна: {s}")

while True:
    w=int(input("Введите ширину вашего прямоугольника: "))
    if w>0:
        while True:
            h=int(input("Введите высоту вашего прямоугольника: "))
            if h>0:
                break
            elif h==0:
                print(f"Высота треугольника не может быть равна нулю\n")
            else:
                print(f"Высота прямоугольника не может быть отрицательной!\n")
        break
    elif w==0:
        print(f"Щирина треугольника не может быть равна нулю\n")
    else:
        print(f"Ширина прямоугольника не может быть отрицательной!\n")
rec=Rectangle(w, h)
rec.square()
