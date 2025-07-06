import datetime

class Product():
    def __init__ (self, company: str, name: str, category: (str|None) = None, stock: (int|None) = None, id: str = "", description: str = ""):
        self.company = company
        self.name = name
        self.category = category
        self.stock = stock
        self.id = id
        self.description = description

class Price():
    def __init__ (self, current: float, currency: str, original: (float|None) = None):
        self.current = current
        self.currency = currency
        self.original = original

class RegisterMetadata():
    def __init__(self, engine: str, origin: str, fetch_response: int = 200, date_checked: (datetime.date|None) = None):
        self.engine = engine
        self.origin = origin
        self.fetch_response = fetch_response
        self.date_checked = datetime.datetime.now() if date_checked is None else date_checked

class Register():
    def __init__(self, product: Product, price: Price, meta: RegisterMetadata):
        self.product = product
        self.price = price
        self.meta = meta
