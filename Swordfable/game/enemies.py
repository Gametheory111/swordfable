import random

"""Defines the enemies in the game"""
__author__ = 'Benjamin Calloway'


class Enemy:
	"""A base class for all enemies"""
	def __init__(self, name, hp, damage):
		"""Creates a new enemy

		:param name: the name of the enemy
		:param hp: the hit points of the enemy
		:param damage: the damage the enemy does with each attack
		"""
		self.name = name
		self.hp = hp
		self.damage = damage

	def is_alive(self):
		return self.hp > 0


class GiantSpider(Enemy):
	def __init__(self):
		super().__init__(name="Giant Spider", hp=10, damage=2)


class Wolf(Enemy):
	def __init__(self):
		super().__init__(name="Wolf", hp=10, damage=5)


class Warg(Enemy):
	def __init__(self):
		super().__init__(name="Warg", hp=20, damage=8)


class Goblin(Enemy):
	def __init__(self):
		super().__init__(name="Goblin", hp=18, damage=5)


class Guard(Enemy):
	def __init__(self):
		super().__init__(name="Guard", hp=25, damage=6)


class Orc(Enemy):
	def __init__(self):
		super().__init__(name="Orc", hp=30, damage=8)


class Knight(Enemy):
	def __init__(self):
		super().__init__(name="Knight", hp=40, damage=9)


class WolfPack(Enemy):
	def __init__(self):
		super().__init__(name="Wolf Pack", hp=40, damage=13)


class Troll(Enemy):
	def __init__(self):
		super().__init__(name="Troll", hp=60, damage=13)





