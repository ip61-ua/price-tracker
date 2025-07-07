import datetime


class Product:
    def __init__(self, company: str, name: str, category: (str | None) = None, stock: (int | None) = None, id: str = "",
                 description: str = ""):
        self.company = company
        self.name = name
        self.category = category
        self.stock = stock
        self.id = id
        self.description = description


class Price:
    def __init__(self, current: float, currency: str, original: (float | None) = None):
        self.current = current
        self.currency = currency
        self.original = original


class RegisterMetadata:
    def __init__(self, engine: str, origin: str, fetch_response: int = 200,
                 date_checked: (datetime.date | None) = None):
        self.engine = engine
        self.origin = origin
        self.fetch_response = fetch_response
        self.date_checked = datetime.datetime.now() if date_checked is None else date_checked


class Register:
    div = '\t'

    def __init__(self, product: Product, price: Price, meta: RegisterMetadata):
        self.product = product
        self.price = price
        self.meta = meta

    def __str__(self):
        r1 = f"{self.meta.engine}{self.div}{self.meta.origin}{self.div}{self.meta.date_checked}{self.div}"
        r2 = f"{self.meta.fetch_response}{self.div}{self.price.current}{self.div}{self.price.currency}{self.div}"
        r3 = f"{self.price.original}{self.div}{self.product.id}{self.div}{self.product.name}{self.div}"
        r4 = f"{self.product.stock}{self.div}{self.product.company}{self.div}{self.product.category}{self.div}"
        r5 = f"{self.product.description}"

        return r1 + r2 + r3 + r4 + r5

