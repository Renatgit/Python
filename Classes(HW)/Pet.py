class Pet:
    def info(self):
        print(f'\t\t\t\tMY ANIMAL\nKind of animal: {self.kind_of_animal}\nPet`s name: {self.name}\nPet`s color: {self.color}\nUnder the form of the an animal: {self.under_the_form_of_an_animal}\nYear of birth: {self.year_of_birth}')
    def history(self):
        print(f'History:\n{self.hstr}')


pet=Pet()
pet.kind_of_animal='dog'
pet.name='Archi'
pet.color='black-brown'
pet.under_the_form_of_an_animal='spaniel'
pet.year_of_birth='2017'

pet.hstr=f'Четыре гоода назад, я мечтал о собаке. И родители решили сделать сюрприз. Как вы узнали више у моеё собаки темно-коричневый цвет. Когда она ехала уже нам, после покупки, мама сказала: `Любите шоколад? Сейчас приедет большая шоколадка!`. Я не мог даже представить, что это будет собака) Она живет с нами уже 4 года!'

pet.info()
pet.history()
