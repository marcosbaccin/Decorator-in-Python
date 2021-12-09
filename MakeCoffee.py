import Coffeeshop

if __name__ == '__main__':

    myCoffee = Coffeeshop.ConcreteCoffee()
    print('Ingredients: ' + myCoffee.get_ingredients() + '; Cost: $' + str(myCoffee.get_cost()))

    myCoffee = Coffeeshop.Milk(myCoffee)
    print('Ingredients: ' + myCoffee.get_ingredients() + '; Cost: $' + str(myCoffee.get_cost()))

    myCoffee = Coffeeshop.Chocolate(myCoffee)
    print('Ingredients: ' + myCoffee.get_ingredients() + '; Cost: $' + str(myCoffee.get_cost()))

    myCoffee = Coffeeshop.Sugar(myCoffee)
    print('Ingredients: ' + myCoffee.get_ingredients() + '; Cost: $' + str(myCoffee.get_cost()))
