class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        self.pet_type = pet_type

        self._owner = None
        if owner:
            self.owner = owner

        Pet.all.append(self)

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        from owner_pet import Owner  # avoid circular import at top
        if not isinstance(value, Owner):
            raise Exception("Owner must be an instance of Owner class")
        self._owner = value

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        from owner_pet import Pet
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        from owner_pet import Pet
        if not isinstance(pet, Pet):
            raise Exception("Argument must be an instance of Pet")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)




