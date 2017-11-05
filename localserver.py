#import time, datetime
import random

class Game:

	#GLOBAL SETTINGS
	width = 30
	height = 30



	def __init__(self):
		self.FIELD = []
		self.PLAYERS = []
		self.playerNum = 0
		self.NOW = 0.0
		#self.view = ""

		for j in range(self.height):
			for i in range(self.width):
				self.FIELD.append(Cell(i, j, "normal") )
	
	def JoinGame(self,name):
		self.PLAYERS.append(Player(name, self.playerNum))

		#allocate a birth point
		bornPlace = int(random.random()*self.width*self.height)
		while self.FIELD[bornPlace].owner!=None:
			bornPlace = int(random()*self.width*self.height)
		c = self.FIELD[bornPlace]
		c.owner = self.playerNum
		c.occupyTime = self.NOW

		self.playerNum+=1
		return self.playerNum-1


	def GetCell(self,x,y):
		return self.FIELD[x+y*self.width]
		
	def PlayerAttackCell(self,attackerId,x,y):
		p = self.PLAYERS[attackerId]
		#check if name is valid
		if p == None: 
			input("ERROR: PlayerAttackCell(): NAMAE NOT FOUND")
			return 4
		#check if in cd
		if p.cd > 0: return 3
		#check if out of boarder
		if x>=self.width or y>=self.height: return 1

		c = self.GetCell(x,y)

		#check if adjacent
		adj = 0 #exclude itself
		for i in self.FIELD:
			if i.owner == attackerId:
				if ((i.x-x==1 or i.x-x==-1) and i.y==y \
					or (i.y-y==1 or i.y-y==-1) and i.x==x):
					adj += 1
		if c.owner!=attackerId and adj==0: return 1
		#check if being taken
		if c.isTaking: return 2

		c.attacker = attackerId
		c.attackTime = self.NOW;
		
		#actuall takeTime
		tt = c.takeTime(self.NOW)
		if adj>=1: actualtt = tt - 0.5*(adj-1)
		c.finishTime = c.attackTime + actualtt
		c.isTaking = True
		p.cd = actualtt
		return 0
		


	def Print(self):
		print("NOW = "+str(self.NOW))
		for j in range(self.height):
			for i in range(self.width):
				ownerId = self.GetCell(i,j).owner
				if ownerId==None:
					print(".", end=" ")
				else:
					print(str(self.GetCell(i,j).owner), end=" ")
			print()



	def TimePass(self, time):
		self.NOW+=time

		for i in self.PLAYERS:
			i.cdDown(time)
		for i in self.FIELD:
			if i.isTaking:
				if i.finishTime<=self.NOW: #should finish
					i.occupyTime = i.finishTime
					i.finishTime = None
					i.owner = i.attacker
					i.attacker = None
					i.isTaking = False
					i.NOW = self.NOW
					i.refreshTakeTime()
	
	def getNextTimePass(self):

		min_cd = 99
		for i in self.PLAYERS:
			if i.cd<min_cd: min_cd = i.cd
		if min_cd == 0: min_cd = 0.1
		
		if auto == True:
			self.TimePass(min_cd)

		return min_cd

	def Refresh(self):
		self.TimePass(self.getNextTimePass())


	def cellNum(self, id):
		r = 0
		for i in self.FIELD:
			if i.owner == id:
				r+=1

		return r


		
class Cell:

	def __init__(self, x, y, cellType):
			
		self.owner      = None
		self.attacker   = None
		self.isTaking   = False
		self.x          = x
		self.y          = y
		self.cellType   = cellType
		self.occupyTime = None
		self.attackTime = None
		self.finishTime = None
		self.NOW = 0
		self.takeTime = 2
		self.refreshTakeTime()

	def refreshTakeTime(self):
		if self.isTaking: return None
		if self.occupyTime == None: return 2;
		timeDiff = self.NOW-self.occupyTime
		self.takeTime = 20*(2**(-timeDiff//20))+2


class Player:

	def __init__(self, name, id):
		self.name = name
		self.cd = 0
		self.id = id
	
	def cdDown(self, time):
		if self.cd>time: self.cd-=time
		else: self.cd=0.0
		return self.cd

	
		
if __name__ == '__main__':

	g = Game()


	player1 = g.JoinGame("1P")
	player2 = g.JoinGame("2P")
	player3 = g.JoinGame("3P")
	player4 = g.JoinGame("4P")


	
	while g.NOW<1200:
		for i in g.FIELD:

			if i.owner == player1:
				d = random.choice([(0,1), (0,-1), (1, 0), (-1,0)])

				if i.x+d[0]>=0 and i.x+d[0]<30 and i.y+d[1]>=0 and i.y+d[1]<30:

					cc = g.GetCell(i.x+d[0], i.y+d[1])
					# If that cell is valid(current cell + direction could be
					# out of range) and that cell is not mine
					if cc != None:
						if cc.owner != player1:
							g.PlayerAttackCell(player1,i.x+d[0], i.y+d[1])

		for i in g.FIELD:
			if i.owner == player2:
				d = random.choice([(0,1), (0,-1), (1, 0), (-1,0)])
				if i.x+d[0]>=0 and i.x+d[0]<30 and i.y+d[1]>=0 and i.y+d[1]<30:
				
					cc = g.GetCell(i.x+d[0], i.y+d[1])
					# If that cell is valid(current cell + direction could be
					# out of range) and that cell is not mine
					if cc != None:
						if cc.owner != player2:
							g.PlayerAttackCell(player2,i.x+d[0], i.y+d[1])

		for i in g.FIELD:
			if i.owner == player3:
				d = random.choice([(0,1), (0,-1), (1, 0), (-1,0)])
				if i.x+d[0]>=0 and i.x+d[0]<30 and i.y+d[1]>=0 and i.y+d[1]<30:
				
					cc = g.GetCell(i.x+d[0], i.y+d[1])
					# If that cell is valid(current cell + direction could be
					# out of range) and that cell is not mine
					if cc != None:
						if cc.owner != player3:
							g.PlayerAttackCell(player3,i.x+d[0], i.y+d[1])



		for i in g.FIELD:
			if i.owner == player4:
				d = random.choice([(0,1), (0,-1), (1, 0), (-1,0)])
				if i.x+d[0]>=0 and i.x+d[0]<30 and i.y+d[1]>=0 and i.y+d[1]<30:
				
					cc = g.GetCell(i.x+d[0], i.y+d[1])
					# If that cell is valid(current cell + direction could be
					# out of range) and that cell is not mine
					if cc != None:
						if cc.owner != player4:
							g.PlayerAttackCell(player4,i.x+d[0], i.y+d[1])
	

		ntp = g.getNextTimePass(auto = False)
		print("NTP="+str(ntp))
		g.TimePass(ntp)
		#g.Print()

		print(str(g.cellNum(player1))+" / "+str(g.cellNum(player2))+" / "+str(g.cellNum(player3))+" / "+str(g.cellNum(player4)))

		print()
	
	g.Print()
	


#testcell.takeTime
