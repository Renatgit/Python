class Caps:
    def __init__(self, txt):
        self.txt=txt
    def caps_up(self):
        x = self.txt.upper()
        print(x)

txt=str(input("Введите любой текст и он будет написан капсом: "))
caps_txt=Caps(txt)
caps_txt.caps_up()
