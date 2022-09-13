class Cellphone:
    def __init__(self, manufact: str, model: str, retail_price: int) -> None:
        self._manufact = manufact
        self._model = model
        self._retail_price = retail_price

    def set_manufact(self, manufact):
        self._manufact = manufact

    def set_model(self, model):
        self._model = model

    def set_retail_price(self, retail_price):
        self._retail_price = retail_price

    def get_manufact(self):
        return self._manufact

    def get_model(self):
        return self._model

    def get_retail_price(self):
        return self._retail_price

    def __str__(self):
        return f'{self._manufact} {self._model} {self._retail_price}'


def main():
    cell_1 = Cellphone('Nokia', '3010', 1200)
    l_cells = [Cellphone('Nokia' + str(x), x**2, x**3) for x in range(5)]
    for k in l_cells:
        print(k)


if __name__ == '__main__':
    main()
