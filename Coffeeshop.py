from abc import ABC, abstractmethod


class AbstractCoffee(ABC):  # Classe abstrata que define a funcionalidade do Coffee implementada pelo decorador
    @abstractmethod
    def get_cost(self):  # Método abstrato que retorna o custo do café
        pass

    @abstractmethod
    def get_ingredients(self):  # Método abstrato que retorna os ingredientes do café
        pass


class ConcreteCoffee(AbstractCoffee):  # Classe de um café simples sem nenhum ingrediente extra

    def get_cost(self):
        return 1.00

    def get_ingredients(self):
        return 'coffee'


class AbstractCoffeeDecorator(ABC):  # Classe decoradora abstrata - observe que ela implementa AbstractCoffee
    @abstractmethod
    def __init__(self, decorated_coffee):
        self.decorated_coffee = decorated_coffee

    # Implementação dos métodos de AbstractCoffee
    @abstractmethod
    def get_cost(self):
        return self.decorated_coffee.get_cost()

    @abstractmethod
    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients()


class Sugar(AbstractCoffeeDecorator):  # Decorator Sugar mistura açúcar com café. Observe que estende AbstractCoffeeDecorator
    # Implementação dos métodos de AbstractCoffeeDecorator
    def __init__(self, decorated_coffee):
        AbstractCoffeeDecorator.__init__(self, decorated_coffee)

    def get_cost(self):
        return self.decorated_coffee.get_cost()

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ', sugar'


class Milk(AbstractCoffeeDecorator):  # Decorator Milk mistura leite com café

    def __init__(self, decorated_coffee):
        AbstractCoffeeDecorator.__init__(self, decorated_coffee)

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 0.25

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ', milk'


class Chocolate(AbstractCoffeeDecorator):  # Decorator Chocolate mistura chocolate com café

    def __init__(self, decorated_coffee):
        AbstractCoffeeDecorator.__init__(self, decorated_coffee)

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 0.75

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ', chocolate'
