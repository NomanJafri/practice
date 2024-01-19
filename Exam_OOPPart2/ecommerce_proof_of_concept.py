# Write your proof-of-concept code in Python below this line.
class Product:
    """
    This class is used to make products 
    for ecommerce database.
    """
    def __init__(self, name: str, description: str, price: float, weight_in_grams: float) -> None:
        """
        This constructor function makes Product's Objects 
        for ecommerce database.
        
        Args:
            name -> str, 
            description -> str, 
            price -> float, and 
            weight -> float
        
        Return:
            None
        
        Raises:
            None
        
        """
        self._name = name
        self._description = description
        self._price = price
        self._weight_in_grams = weight_in_grams
    
    @property    
    def name(self):
        """ 
        getter method for private property self._name
        
        """
        return self._name
        
    @name.setter    
    def name(self, new_name):
        """
        Setter method for private property self._name
        Args:
            new_name: string
        Return:
            None
        Raises:
            ValueError if not string
        """
        if isinstance(new_name, str):
            self._name = new_name
        else:
            raise ValueError('Please enter a string based name')
            
    @property    
    def description(self):
        """ 
        getter method for 
        private property self._description
        
        """
        return self._description
        
    @description.setter    
    def description(self, new_description):
        """
        Setter method for 
        private property self._description
        Args:
            new_description: string
        Return:
            None
        Raises:
            ValueError if not string
        """
        if isinstance(new_description, str):
            self._description = new_description
        else:
            raise ValueError('Please enter a string based description')
            
    @property    
    def price(self):
        """ 
        getter method for private property self._price
        
        """
        return self._price
        
    @price.setter    
    def price(self, new_price):
        """
        Setter method for private property self._price
        Args:
            new_price: float
        Return:
            None
        Raises:
            ValueError if not a float
        """
        if isinstance(new_price, float):
            self._price = new_price
        else:
            raise ValueError('Please enter a floating point number')
    
    @property    
    def weight_in_grams(self):
        """ 
        getter method for 
        private property self._weight_in_grams
        
        """
        return self._weight_in_grams
        
    @weight_in_grams.setter    
    def weight_in_grams(self, new_weight_in_grams):
        """
        Setter method for 
        private property self._weight_in_grams
        Args:
            new_weight_in_grams: float
        Return:
            None
        Raises:
            ValueError if not floating point number
        """
        if isinstance(new_weight_in_grams, float):
            self._weight_in_grams = new_weight_in_grams
        else:
            raise ValueError('Please enter a floating point number')
            
    def calculate_shipping(self):
        """
        Calculate shipping cost for the Product 
        according to it's weight
        
        Args: None
        Return: 5,8, or 100 according to the algorithm
        Raise: None
        """
        if self.weight_in_grams <= 1000.0:
            return 5
        elif self.weight_in_grams > 1000.0 and self.weight_in_grams < 5000.0:
            return 8
        elif self.weight_in_grams >= 5000:
            return 10


""" 
+++++++++++++++++++++++++++++++++++++++++++++++++++
Below this is the testing Area for Product class
+++++++++++++++++++++++++++++++++++++++++++++++++++
"""

# creating instance for Product class to test            
hand_cream = Product('Nivea', 'Lotion and Creams', 3.5, 50.0)

"""Testing name property ====================="""
#getting name from getter method
print(hand_cream.name)
# using setter method to set new name
hand_cream.name = 'Ponds'
print(hand_cream.name)
#using setter method to test valueError
try:
    hand_cream.name = 123
except ValueError as err:
    print('name:', err)
"""Testing description property ====================="""
# getting description from getter method
print(hand_cream.description)
# using setter method to set new description
hand_cream.description = 'Hand Cream'
print(hand_cream.description)
#using setter method to test valueError
try:
    hand_cream.description = 123
except ValueError as err:
    print('description:', err)

"""Testing price property ====================="""
# getting price using getter method
print(hand_cream.price)
# using setter method to set new price
hand_cream.price = 2.0
print(hand_cream.price)
#using setter method to test valueError
try:
    hand_cream.price = 123
except ValueError as err:
    print('price:', err)

"""Testing weight_in_grams property ================"""
# getting weight_in_grams using getter method
print(hand_cream.weight_in_grams)
# using setter method to set new weight_in_grams
hand_cream.weight_in_grams = 2000.0
print(hand_cream.weight_in_grams)
#using setter method to test valueError
try:
    hand_cream.weight_in_grams = 123
except ValueError as err:
    print('weight_in_grams:', err)

"""Testing calculate shipping method ================"""
#testing calculate shipping method
print(hand_cream.calculate_shipping())


"""sub class Book starting here """

class Book(Product):
    """
    Book sub class to make objects with additional info in addition to the Product class with calculating shipping cost based on special algorithm design for books based on paper or hardback 
    """
    def __init__(self, name, description, price, weight, isb_number, hardback):
        """
        constructor to instantiate Book class with Parents properties as well by calling parent class constructor.
        Calling: 
            Parent class constructor super().__init__()
        Args: 
            isb_number: integer
            hardback: boolean
        Return: None
        Raise: None
        """
        super().__init__(name, description, price, weight)
        self._isb_number = isb_number
        self._hardback = hardback
    
    @property
    def isb_number(self):
        """
        Getter for private property self._isb_number
        """
        return self._isb_number
        
    @isb_number.setter
    def isb_number(self, new_isb_number):
        """
        Setter for private property self._isb_number
        Args: 
            new_isb_number: integer
        Return: None
        Raise: Value error incase new_isb-number is not integer
        """
        if isinstance(new_isb_number, int):
            self._isb_number = new_isb_number
        else:
            raise ValueError('Please enter a valid integer')
            
    @property
    def hardback(self):
        """
        Getter for private property self._hardback
        """
        return self._hardback
        
    @hardback.setter
    def hardback(self, new_hardback):
        """
        Setter for private property self._hardback
        Args:
            new_hardback: boolean (True or False)
        Return: None
        Raise: Value error if new value is not boolean
        """
        if isinstance(new_hardback, bool):
            self._hardback = new_hardback
        else:
            raise ValueError('Please enter a valid boolean')
        
    
    def calculate_shipping(self):
        """
        polymorphic Method to calculate shipping specially for books on bases of if the book is hardback or paperback
        Args: None
        Return: shipping cost for book integer
        Raise: None
        """
        if self.hardback:
            return 4
        return 3

""" 
+++++++++++++++++++++++++++++++++++++++++++++++++++
Below this is the testing Area for Book class
+++++++++++++++++++++++++++++++++++++++++++++++++++
"""

# creating instance for Product class to test            
harry_potter = Book('Harry Porter', 'fantasy books', 50, 1600, 987654, True)

"""Testing isb_number property ====================="""
#getting name from getter method
print(harry_potter.isb_number)
# using setter method to set new isb_number
harry_potter.isb_number = 123456
print(harry_potter.isb_number)
#using setter method to test valueError
try:
    harry_potter.isb_number = 123.000
except ValueError as err:
    print('isb_number:', err)
    
"""Testing hardback property ====================="""
# getting hardback value from getter method
print(harry_potter.hardback)
# using setter method to set new description
harry_potter.hardback = False
print(harry_potter.hardback)
#using setter method to test valueError
try:
    harry_potter.hardback = 123
except ValueError as err:
    print('hardback:', err)
    
"""Testing calculate shipping method ================"""
#testing calculate shipping method
print( harry_potter.calculate_shipping())
harry_potter.hardback = True
print( harry_potter.calculate_shipping())
