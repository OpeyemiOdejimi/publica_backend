class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    
    def display_info(self):
        print(f'The Pet name is: {self.name}')
        print(f'The Pet specie is: {self.species}')
        print(f'The Pet age is: {self.age}')

    
    def celebrate_birthday(self):
        self.age +=1
        print(f'Congratulations, {self.name}!\n You are now {self.age} years old.')


my_pet = Pet("Bobby", "Dog", 10)


my_pet.display_info()
my_pet.celebrate_birthday()
my_pet.display_info()