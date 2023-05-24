class Restaurant:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe_restaurant(self):
        print(self.name)

    def describe_age(self):
        print(self.age)


class RestOne(Restaurant):

    def __init__(self, name, age, sex):
        super().__init__(name, age)
        sex = sex


if __name__ == '__main__':
    r = RestOne('a', 'b', 'c')
    print(r)
