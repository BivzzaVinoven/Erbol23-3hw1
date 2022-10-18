class Human:
    instance = None

    def __new__(cls, name, age, growth):
        cls.instance = super().__new__(cls)

        cls.instance.name = name
        cls.instance.age = age
        cls.instance.growth = growth

        return cls.instance


q = Human("Adam", 23, 175)
print(q.name, q.age, q.growth)
