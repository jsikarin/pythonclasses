# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class Food(object):
    def __init__(self, name):
        self.name = name
        
    def print_food(self):
        print ("This is delicious {}".format(self.name))
        
class Fruit(Food):
    def __init__(self, name, seeds):
        super(Fruit, self).__init__(name)
        self.seeds = seeds
        
    def print_fruit(self):
        super(Fruit, self).print_food()
        print("It has {}".format(self.seeds),"seed(s)")
        
avacado = Fruit('avacado', 1)
avacado.print_fruit()

    