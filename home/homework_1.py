class Hero:
    def __init__(self, name, nickname, hp, damage):
        self.name = name
        self.nickname = nickname
        self.hp = hp
        self.damage = damage


class Immorral(Hero):
    def __init__(self, name, nickname, hp, damage):
        super().__init__(name, nickname, hp, damage)

    def heal(self):
        return self.hp + 100

    def __str__(self):
        return f'{self.name}, {self.nickname}, {self.hp}, {self.damage}'


class Infested_Admiral(Hero):
    def __init__(self, name, nickname, hp, damage):
        super().__init__(name, nickname, hp, damage)

    def brand_phrase(self):
        print('good will win')

    def __str__(self):
        return f'{self.name}, {self.nickname}, {self.hp}, {self.damage}'


class Raynor(Hero):
    def __init__(self, name, nickname, hp, damage):
        super().__init__(name, nickname, hp, damage)

    def greetings(self):
        print(f'my name is {self.name}')

    def __str__(self):
        return f'{self.name}, {self.nickname}, {self.hp}, {self.damage}'


class Void_ray(Hero):
    def __init__(self, name, nickname, hp, damage):
        super().__init__(name, nickname, hp, damage)

    def two_damage(self):
        return self.damage * 2

    def __str__(self):
        return f'{self.name}, {self.nickname}, {self.hp}, {self.damage}'



h1 = Immorral(name='Taldaris', nickname='immortal', hp=200, damage=50)
h2 = Infested_Admiral(name='Aleksei', nickname='Stukov', hp=30, damage=5)
h3 = Raynor(name='Raynor', nickname='lider_resistens', hp=150, damage=6)
h4 = Void_ray(name='Void_ray', nickname='грелка', hp=150, damage=18)

print(h1)
print(h2)
print(h3)
print(h4)