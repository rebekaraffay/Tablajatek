class A:
    def __init__(self, name):
        self._name = name
        self._age = -1
        self._lista = None

    def set_age(self, age):
        self._age = age

    def set_lista(self):
        self._lista = []
        print("set lista", self._lista)

    def greeting(self):
        print(f"hi, my name is {self._name}")
        if self._age > -1:
            print(f"and my age is {self._age}")


def main():
    a = A("Dorka")
    a.greeting()
    a.set_age(20)
    a.greeting()
    print(a._lista)
    a.set_lista()
    print(a._lista)


if __name__ == "__main__":
    main()
