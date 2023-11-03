class SmoothieSet:
    ingredients = ["fruits", "yoghurt", "ice"]
    appliance = "blender"

class MakeADrink(SmoothieSet):
    drink_type = "juice"
    
    def create(self):
        print("making a", drink_type,"using", appliance, "with", ingredients,".")
    """print(f"Making a {self.drink_type} using {self.appliance} with {', '.join(self.ingredients)}")"""



my_drink = MakeADrink()
my_drink.create()