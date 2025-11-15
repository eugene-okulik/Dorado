class Flower:
    def __init__(self, name, color, stem_length, lifetime, price):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.lifetime = lifetime
        self.price = price

    def __str__(self):
        return (f"Flower with description: "
                f"{self.color} {self.name} "
                f"for the price €{self.price}, "
                f"{self.lifetime} days of lifespan, "
                f"{self.stem_length} cm of stem length")

    def __repr__(self):
        return (f"Flower with description: "
                f"{self.color} {self.name} "
                f"for the price €{self.price}, "
                f"{self.lifetime} days of lifespan, "
                f"{self.stem_length} cm of stem length")


class Rose(Flower):
    def __init__(self, color="Red", stem_length=30, lifetime=7, price=20):
        super().__init__(
        name = "Rose",
        color = color,
        stem_length = stem_length,
        lifetime= lifetime,
        price = price
        )


class CallaLily(Flower):
    def __init__(self, color="White", stem_length=60, lifetime=10, price=15):
        super().__init__(
        name = "Calla Lily",
        color = color,
        stem_length = stem_length,
        lifetime= lifetime,
        price = price
        )


class Tulip(Flower):
    def __init__(self, color="Yellow", stem_length=15, lifetime=5, price=10):
        super().__init__(
        name = "Tulip",
        color = color,
        stem_length = stem_length,
        lifetime= lifetime,
        price = price
        )


class Bouquet:
    def __init__(self):
        self.flowers = []

    def __str__(self):
        return (f"Bouquet: {len(self.flowers)} flowers, "
                f"€{self.total_price()}, {round(self.lifetime())} days")

    def __repr__(self):
        return (f"Bouquet: {len(self.flowers)} flowers, "
                f"€{self.total_price()}, {round(self.lifetime())} days")

    def add_flower(self, flower):
        self.flowers.append(flower)

    def total_price(self):
        return sum(flower.price for flower in self.flowers)

    def lifetime(self):
        if not self.flowers:
            return None
        return sum(flower.lifetime for flower in self.flowers) / len(self.flowers)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda flower: flower.lifetime)

    def sort_by_color(self):
        self.flowers.sort(key=lambda flower: flower.color)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda flower: flower.stem_length)

    def sort_by_price(self):
        self.flowers.sort(key=lambda flower: flower.price)

    def find_by_lifetime(self, min_days, max_days):
        return [flower for flower in self.flowers
                if min_days <= flower.lifetime <= max_days]

    def find_by_price(self, min_price, max_price):
        return [flower for flower in self.flowers
                if min_price <= flower.price <= max_price]


rose1 = Rose()
rose2 = Rose(price=18)
rose3 = Rose(lifetime=6, price=18)
rose4 = Rose(color="White", stem_length=28, lifetime=8, price=22)
rose5 = Rose(color="White", stem_length=25, lifetime=6, price=18)

calla_lily1 = CallaLily()
calla_lily2 = CallaLily(color="Black", stem_length=65, lifetime=13, price=16)
calla_lily3 = CallaLily(color="Black", stem_length=65, lifetime=15, price=17)

tulip1 = Tulip()
tulip2 = Tulip(color="Red", stem_length=16, lifetime=6, price=11)
tulip3 = Tulip(color="Red", stem_length=18, lifetime=6, price=11)

bouquet = Bouquet()

bouquet.add_flower(rose1)
bouquet.add_flower(rose2)
bouquet.add_flower(rose1)
bouquet.add_flower(calla_lily1)
bouquet.add_flower(calla_lily2)
bouquet.add_flower(calla_lily1)
bouquet.add_flower(tulip1)
bouquet.add_flower(tulip2)
bouquet.add_flower(tulip1)
