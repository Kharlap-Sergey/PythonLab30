class Address(object):
    """description of class"""
    def __init__(self, city, street):
        self.city = city
        self.street = street

    def __str__(self):
        return f"address is {self.city}, {self.street}"


