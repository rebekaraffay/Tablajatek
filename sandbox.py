from Fas_esetek import nodes



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
    nodes()
    nodes()
    nodes()


if __name__ == "__main__":
    main()
