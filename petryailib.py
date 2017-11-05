import colorfight

class PetryAI:
	#global setting

	def __init__(self, name):
		self.NAME = name

		self.G = colorfight.Game()
		self.G.JoinGame(self.NAME)
		self.refreshHq()

	def refreshHq(self):
		print()
		print("OvO  Refreshing HQ")
		self.G.Refresh()

		self.mySoldiersNum = 0
		self.battleField = []

		hq_pos_sum_x = 0.0	#temp var for calcaulating the HQ coordinate
		hq_pos_sum_y = 0.0
		for j in range(self.G.height):
			for i in range(self.G.width):
				s=self.Soldier(i, j, self.G)
				self.battleField.append(s)
				if s.isMine(): 
					hq_pos_sum_x += i
					hq_pos_sum_y += j
					mySoldiersNum += 1
		hq_pos_sum_x /= mySoldiersNum
		hq_pos_sum_y /= mySoldiersNum
		self.hqPosition = [hq_pos_sum_x,hq_pos_sum_y]

		print("MY_SOL = "+str(mySoldiersNum))
		print("HQ_POS = "+str(hqPosition))

		#update TAKETIME
		for s in self.allSoldiers():
			neighbourIsMine = 0
			for i in s.neighbours():
				if i!=None:
					if call(i).isMine():
						neighbourIsMine += 1
			if neighbourIsMine>1 :
				s.takeTime -= neighbourIsMine*0.5



		print("=w=  INITIALIZED")
		print()


	def call(self,coordinate): 
	# access to soldier !!! CANNOT HANDLE {None}
		return self.battleField[coordinate[0] + coordinate[1]*G.width]


	def allSoldiers(self):
		result = []
		for j in range(self.G.height):
			for i in range(self.G.width):
				result.append(self.call([i,j]))
		return result



	class Soldier:
	


		def __init__(self, set_x, set_y, G):
			self.cor=[set_x,set_y]
			c = G.GetCell(self.x(), self.y())
			self.owner = c.owner

			self._neighbours = None #so that neighbour will only run once
			self._neighboursTime = None

			self.isTaking = c.isTaking
			self.takeTime = c.takeTime # seconds it would take if you attack this cell
			self.attacker = c.attacker
			self.finishTime = c.finishTime
			#self.occupyTime = c.occupyTime # time stamps. not useful
			#self.attackTime = c.attackTime # time stamps. not useful
			#self.neighboursTime()

		def x(self): return self.cor[0]
		def y(self): return self.cor[1]

		def isMine(self):
			return self.owner == self.G.uid


		def neighbours(self):
			if self._neighbours == None:
				up = [self.x, self.y+1] if self.y<G.height-1 else None #Out Of Boarder
				right = [self.x+1, self.y] if self.x<G.width-1 else None
				down = [self.x, self.y-1] if self.y>0 else None
				left = [self.x-1, self.y] if self.x>0 else None
				self._neighbours = [up, right, down, left]
			return self._neighbours

	
		def neighbourTo(self, position):
			if position == "up": return self.neighbour().call(n[0])
			elif position == "right": return self.neighbour().call(n[1])
			elif position == "down": return self.neighbour().call(n[2])
			elif position == "left": return self.neighbour().call(n[3])

		def atFrontline(self):
			if self.isMine():
				for n_cor in self.neighbours():
					if n_cor != None:
						if not call(n_cor).isMine(): 
							#if any of its valid neighbour is not mine
							return True 
			return False


		def outFrontline(self):
			if not self.isMine(): #if itself is not mine
				#print("IN OUTFRONTLINE: NOT MINE")
				for n_cor in self.neighbours():
					if n_cor != None:
						if call(n_cor).isMine(): #and if one of its neighbour is mine
							return True 
			return False


		def potential(self): #pre: an outFrontline not being attacked
			p = 1//self.takeTime
			p //= self.distanceToHq()
		
			if self.cellType == "gold": p*=5
			#for n in self.neighbours():
			
			return p



		def neighboursTime(self):
			if self._neighboursTime == None:
				self._neighboursTime = []
				n = self.neighbours()
				for n_cor in (n):
					print("N_COR")
					print(n_cor)
					if n_cor == None: #if out of boarder
						self._neighboursTime.append(None) 
					elif call(n_cor).isTaking: #if being attacked, currently return 22
	#!!!!!!!!
						self._neighboursTime.append(22) 
					else:
						self._neighboursTime.append(call(n_cor).takeTime)
			return self._neighboursTime


		def minNeighbourTime(self):
			min_cor = self.neighbours()[0]
			min_time = self.neighboursTime()[0]

			for i in range(1,4):
				if self.neighboursTime()[i] != None:
					if self.neighboursTime()[i] < min_time:
						min_time = self.neighboursTime()[i]
						min_cor = self.neighbours()[i]
			return [min_time, min_cor]

		def distanceToHq(self):
			return abs(self.x-hqPosition[0])+abs(self.y-hqPosition[1])

		def print(self):
			print("[ " + str(self.x) + ", " + str(self.y) + " ]")
			if self.isMine():
				print("owner: " + str(self.owner) + "  --MINE")
			else:
				print("owner: " + str(self.owner) + "  --OTHER'S")


	#Soldier OOB(0,0)


class PetrySimpleAI:

	def __init__ (self, name, GAME):
		self.coe_rules=coe_rules
		self.g=colorfight.Game()
		self.g.JoinGame(name)
		

	def eval(self):
		return 1


	def actualTT(self, cell_cor, uid):
		tt = self.g.GetCell(cell_cor[0],cell_cor[1]).
		


	def getAttributions(self, cell_cor):
		attributions = {
			"TT"		: self.takeTime,
			"isMine"	: False,
			"celltype"	: "normal",

		}