############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.name = name
        self.is_bestseller = is_bestseller

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        
        self.pairings.append(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType('musk', '1998', 'green', True, True, 'Muskmelon')
    muskmelon.add_pairing("mint")
    all_melon_types.append(muskmelon)

    casaba = MelonType('cas', '2003', 'orange', True, False, "Casaba")
    casaba.add_pairing(["strawberries", "mint"])
    all_melon_types.append(casaba)
    
    crenshaw = MelonType('cren', '1996', 'green', False, False, "Crenshaw")
    crenshaw.add_pairing('prosciutto')
    all_melon_types.append(crenshaw)

    yellowmelon = MelonType('yw', '2013','yellow',True, True, 'Yellow Watermelon')
    yellowmelon.add_pairing('ice cream')
    all_melon_types.append(yellowmelon)

    
    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f'{melon.name} pairs with')
        for pairing in melon.pairings:
            print(f'- {pairing}')
    
    return None


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_code = {}

    for melon in melon_types:
        melon_code[melon.code] = melon 
    return melon_code

# make_melon_types()
# print_pairing_info(melon_types)


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, type, shape_rating, color_rating, field, harvested):
        self.type = type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvested = harvested 
        
    def is_sellable(self):
        if self.shape_rating + self.color_rating > 10 and self.field != 3:
            return True
        else:
            return False

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    code_lookup = make_melon_type_lookup(melon_types)

    melon_1 = Melon(code_lookup['yw'],8,7,2,'Sheila')
    melon_2 = Melon(code_lookup['yw'],3,4,2,"Sheila")
    melon_3 = Melon(code_lookup['yw'],9,8,3,"Sheila")
    melon_4 = Melon(code_lookup['cas'],10,6,35,"Sheila")
    melon_5 = Melon(code_lookup['cren'] ,8,9,35,"Michael")
    melon_6 = Melon(code_lookup['cren'],8,2,35, "Michael")
    melon_7 = Melon(code_lookup['cren'] ,2,3,4,"Michael")
    melon_8 = Melon(code_lookup['musk'] ,6,7,4,"Michael")
    melon_9 = Melon(code_lookup['yw'],7,10,3, "Sheila")

    list_of_melons = [melon_1, melon_2, melon_3,
                       melon_4, melon_5, melon_6,
                       melon_7, melon_8, melon_9]

    return list_of_melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable():
            sellability = "(CAN BE SOLD)"
        else:
            sellability = "(NOT SELLABLE)"
        print(f'Harvested by {melon.harvested} from Field {melon.field}. {sellability}')

all_melon_types = make_melon_types()
make_melon_type_lookup(all_melon_types)
list_of_melons = make_melons(all_melon_types)
get_sellability_report(list_of_melons)
