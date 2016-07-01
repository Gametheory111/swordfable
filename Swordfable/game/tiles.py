import random


"""Describes the tiles in the world space."""
__author__ = 'Benjamin Calloway'

import items, enemies, actions, world


class MapTile:
	"""The base class for a tile within the world space"""
	def __init__(self, x, y):
		"""Creates a new tile.

		:param x: the x-coordinate of the tile
		:param y: the y-coordinate of the tile
		"""
		self.x = x
		self.y = y

	def intro_text(self):
		"""Information to be displayed when the player moves into this tile."""
		raise NotImplementedError()

	def modify_player(self, the_player):
		"""Process actions that change the state of the player."""
		raise NotImplementedError()

	def adjacent_moves(self):
		"""Returns all move actions for adjacent tiles."""
		moves = []
		if world.tile_exists(self.x + 1, self.y):
			moves.append(actions.MoveEast())
		if world.tile_exists(self.x - 1, self.y):
			moves.append(actions.MoveWest())
		if world.tile_exists(self.x, self.y - 1):
			moves.append(actions.MoveNorth())
		if world.tile_exists(self.x, self.y + 1):
			moves.append(actions.MoveSouth())
		return moves

	def available_actions(self):
		"""Returns all of the available actions in this room."""
		moves = self.adjacent_moves()
		moves.append(actions.ViewInventory())

		return moves


class StartingRoom(MapTile):
	def intro_text(self):
		return """
		You find yourself lying on a pile of straw in a dark room. 
		It appears to be a jail cell.
		The door is ajar, and there seems to be nobody around.
		"""

	def modify_player(self, the_player):
		#Room has no action on player
		pass


class EnterHall(MapTile):
	def intro_text(self):
		return """
		You are now in a hallway. 
		There are red banners hanging on the walls.
		"""

	def modify_player(self, the_player):
		#Room has no action on player
		pass


class EnterRoom(MapTile):
	def intro_text(self):
		return """
		You are now in a room. 
		A candle sitting on a table illuminates it.
		"""

	def modify_player(self, the_player):
		#Room has no action on player
		pass


class VictoryRoom(MapTile):
	def intro_text(self):
		return """
		You have vanquished all evil!

		Victory is yours!
		"""

	def modify_player(self, player):
		player.victory = True


class EmptyCavePath(MapTile):
	def intro_text(self):
		return """
		Another unremarkable part of the cave. 
		You must forge onwards.
		"""

	def modify_player(self, the_player):
		#Room has no action on player
		pass


class MultiLootRoom(MapTile):
	"""A room that adds something to the player's inventory several times"""
	def __init__(self, x, y, *argv):  # https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/
		super().__init__(x, y)
		self.items = []
		for item in argv:
			self.items.append(item)  # https://docs.python.org/2/tutorial/datastructures.html

	def modify_player(self, the_player):
		self.add_loot(the_player)

	def add_loot(self, the_player):
		the_player.inventory.extend(self.items)
		self.items = []

	def intro_text(self):
		if self.items:
			stuff_here = "You see:\n"
			for item in self.items:
				stuff_here += '- ' + item.description + '\n'
			stuff_here += 'You pick them up.\n'

		else:
			stuff_here = 'There\'s nothing here anymore.'

		return stuff_here


class GoldRoomS(MultiLootRoom):
	def __init__(self, x, y):
		self.randGold = 1 + random.randrange(0, 10)        
		super().__init__(x, y, items.Gold(self.randGold))


class GoldRoomM(MultiLootRoom):
	def __init__(self, x, y):
		self.randGold = 10 + random.randrange(0, 16)        
		super().__init__(x, y, items.Gold(self.randGold))


class GoldRoomL(MultiLootRoom):
	def __init__(self, x, y):
		self.randGold = 20 + random.randrange(0, 21)        
		super().__init__(x, y, items.Gold(self.randGold))


class FindDaggerRoom(MultiLootRoom):
	def __init__(self, x, y):      
		super().__init__(x, y, items.Dagger())


class FindShortSwordRoom(MultiLootRoom):
	def __init__(self, x, y):      
		super().__init__(x, y, items.ShortSword())


class EnemyRoom(MapTile):
	def __init__(self, x, y, enemy):
		self.enemy = enemy
		super().__init__(x, y)

	def modify_player(self, the_player):
		if self.enemy.is_alive():
			currentDmg = self.enemy.damage + random.randrange(-1, 2)
			the_player.hp -= currentDmg
			print("{} does {} damage. You have {} HP remaining.\n".format(self.enemy.name, currentDmg, the_player.hp))

	def available_actions(self):
		if self.enemy.is_alive():
			return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
		else:
			return self.adjacent_moves()


class GiantSpiderRoom(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, enemies.GiantSpider())

	def intro_text(self):
		if self.enemy.is_alive():
			return """
			A giant spider jumps down from its web in front of you!
			"""
		else:
			return """
			The corpse of a dead spider rots on the ground.
			"""


class TrollRoom(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, enemies.Troll())

	def intro_text(self):
		if self.enemy.is_alive():
			return """
			A giant troll is blocking your path!
			"""
		else:
			return """
			A dead troll reminds you of your triumph.
			"""


class CastleHall(MapTile):
	def intro_text(self):
		return """
		An empty castle hallway. 
		A lit torch sits in a sconce on the wall.
		"""

	def modify_player(self, the_player):
		#Room has no action on player
		pass


class CastleRoom(MapTile):
	def intro_text(self):
		return """
		An empty part of the room. It's rather cold in here.
		"""

	def modify_player(self, the_player):
		#Room has no action on player
		pass


class GuardRoom(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, enemies.Guard())

	def intro_text(self):
		if self.enemy.is_alive():
			return """
			A guard is on duty! He doesn't look happy to see you.
			"""
		else:
			return """
			A dead guard lies here.
			"""


class KnightRoom(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, enemies.Knight())

	def intro_text(self):
		if self.enemy.is_alive():
			return """
			You encounter a zealous knight.
			"""
		else:
			return """
			There's a dead knight here.
			"""







