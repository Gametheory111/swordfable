"""Describes the items in the game."""
__author__ = 'Benjamin Calloway'


class Item():
	"""The base class for all items"""
	def __init__(self, name, description, value):
		self.name = name
		self.description = description
		self.value = value

	def __str__(self):
		return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Weapon(Item):
	def __init__(self, name, description, value, damage):
		self.damage = damage
		super().__init__(name, description, value)

	def __str__(self):
		return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class ShortSword(Weapon):
	def __init__(self):
		super().__init__(name="Short Sword",
						 description="A small sword used as a defensive weapon.",
						 value=18,
						 damage=14)


class Dagger(Weapon):
	def __init__(self):
		super().__init__(name="Dagger",
						 description="A small dagger with some rust. Somewhat more dangerous than a rock.",
						 value=10,
						 damage=10)


class Sting(Weapon):
	def __init__(self):
		super().__init__(name="Sting",
						 description="An elvish dagger wielded by Bilbo Baggins.",
						 value=45,
						 damage=15)


class SauronMace(Weapon):
	def __init__(self):
		super().__init__(name="Sauron\'s Mace",
						 description="A large mace forged for the dark lord Sauron.",
						 value=90,
						 damage=42)


class Gold(Item):
	def __init__(self, amt):
		self.amt = amt
		super().__init__(name="Gold",
						 description="{} small coins made of solid gold.".format(str(self.amt)),
						 value=self.amt)
