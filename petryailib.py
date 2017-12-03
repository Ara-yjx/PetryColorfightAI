import colorfight
import localserver
import operator

class PetryAI:
	#global setting

	def __init__ (self, gameInstance, name, eval, mode="test"): 
		self.mode = mode # decides which API shall use
		self.eval = eval
		self.G = gameInstance
		self.base = None

		if mode=="test":
			self.myId = self.G.JoinGame(name)
		else: 
			self.G.JoinGame(name)
			self.myId = self.G.uid
		self.Soldiers = []

		#initalize Soldiers
		for j in range(self.G.height):
			for i in range(self.G.width):
				self.Soldiers.append(self.Soldier(self.G.GetCell(i, j)))
		
		for s in self.Soldiers:
			s.isMine = (s.owner == self.myId) #initialize Soldier.isMine
			self.initNeighboursCor(s) #Remain None if out of boarder
			self.initActualTT(s)
			if s.isBase and s.isMine: self.base = s.cor #initialize base
		



	def initNeighboursCor(self, soldier):
		if soldier.cor[1]<self.G.height-1: 
			soldier.neighboursCor[0] = tuple(map(operator.add, soldier.cor, (0,1)))
		if soldier.cor[0]<self.G.width-1: 
			soldier.neighboursCor[1] = tuple(map(operator.add, soldier.cor, (1,0)))
		if soldier.cor[1]>0: 
			soldier.neighboursCor[2] = tuple(map(operator.add, soldier.cor, (0,-1)))
		if soldier.cor[0]>0: 
			soldier.neighboursCor[3] = tuple(map(operator.add, soldier.cor, (-1,0)))

	def initActualTT(self, soldier):
		neiMine = 0
		for i in soldier.neighboursCor:
			if i!=None:
				if self.call(i).isMine:
					neiMine+=1
		if neiMine>0: soldier.takeTime -= (neiMine-1)*0.5

		"""
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
					if s.isMine: 
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
						if call(i).isMine:
							neighbourIsMine += 1
				if neighbourIsMine>1 :
					s.takeTime -= neighbourIsMine*0.5



			print("=w=  INITIALIZED")
			print()
		"""

	def call(self,coordinate): 
	# access to soldier !!! CANNOT HANDLE {None}
		return self.Soldiers[coordinate[0] + coordinate[1]*self.G.width]

	def outFrontline(self, soldier):
		if not soldier.isMine: 
		#if itself is not mine
			for n_cor in soldier.neighboursCor:
				if n_cor != None:
					if self.call(n_cor).isMine: 
						#and if any of its neighbours is mine
						return True 
		return False


	def refresh(self):
		#initalize Soldiers
		self.base = None
		for s in self.Soldiers:
			s.refresh(self.G.GetCell(s.cor[0],s.cor[1]))
			s.isMine = (s.owner == self.myId) #initialize Soldier.isMine
			self.initActualTT(s)
			
			if s.isBase and s.isMine: 
				self.base = s.cor #initialize base

	def getAttrbutions(self, soldier):
		return {
			"takeTime": soldier.takeTime,
			"cellType": soldier.cellType,
			"isBase": soldier.isBase,
			"cor": soldier.cor
		}


	def eval(self, attr):
		#return 1//attr["takeTime"]
		r = 1/attr["takeTime"]
		if attr["cellType"] == "gold": r*=5
		return r

	def secureBase(self):
		if self.mode != "test":
			baseNeiMine = 0
			for baseNei in self.call(self.base).neighboursCor:
				if baseNei != None:
					if self.call(baseNei).isMine: baseNeiMine+=1

			if baseNeiMine <= 1: #find new base
				for s in self.Soldiers:
					if s.isMine:
						newBaseNeiMine = 0 #check if new base is safe
						for i in s.neighboursCor: 
							if baseNei != None:
								if self.call(baseNei).isMine: newBaseNeiMine+=1
						if newBaseNeiMine==4:
							self.G.BuildBase(s.cor[0],s.cor[1])
							return False
		return True


	class Soldier:
	
		def __init__(self, cell):
			self.cor=(cell.x, cell.y)
			self.isMine = False #updated outside
			self.owner = cell.owner
			self.cellType = cell.cellType
			self.isTaking = cell.isTaking
			self.takeTime = cell.takeTime #updated outside
			self.attacker = cell.attacker
			self.finishTime = cell.finishTime
			self.isBase = cell.isBase
			#self.occupyTime = c.occupyTime # time stamps. not useful
			#self.attackTime = c.attackTime # time stamps. not useful
			#self.neighboursTime()

			self.neighboursCor = [None, None, None, None] #updated outside


		def refresh(self, cell):
			self.owner = cell.owner
			self.isTaking = cell.isTaking
			self.takeTime = cell.takeTime #updated outside
			self.attacker = cell.attacker
			self.finishTime = cell.finishTime
			if cell.isBase:
				self.isBase = True
				
			else:
				self.isBase = False

			"""
			self.NeighboursTime = [None, None, None, None]
			self.initNeighboursTime()
			"""
	



	
		
			"""
		def neighbourTo(self, position):
			if position == "up": return self.neighbour().call(n[0])
			elif position == "right": return self.neighbour().call(n[1])
			elif position == "down": return self.neighbour().call(n[2])
			elif position == "left": return self.neighbour().call(n[3])
			



		def atFrontline(self):
			if self.isMine:
				for n_cor in self.neighboursCor:
					if n_cor != None:
						if not sellf.call(n_cor).isMine: 
							#if any of its valid neighbour is not mine
							return True 
			return False


			"""


		def potential(self): #pre: an outFrontline not being attacked
			p = 1//self.takeTime
			p //= self.distanceToHq()
		
			if self.cellType == "gold": p*=5
			#for n in self.neighbours():
			
			return p


			"""
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
			"""


		def print(self):
			print(self.cor)
			if self.isMine:
				print("owner: " + str(self.owner) + "  --MINE")
			else:
				print("owner: " + str(self.owner) + "  --OTHER'S")




class PetrySimpleAI:

	def __init__ (self, name, eval_rules, mode="test"): 
		self.mode = mode # decides which API shall use
		self.eval_rules = eval_rules

		if self.mode == "test":
			self.G = localserver.JoinGame(name)
		else:
			self.G=colorfight.Game()
			self.G.JoinGame(name)


	

	def eval(self):

		self.initAttr()

		return [0,0]


	def actualTT(self, cell_cor, uid):
		tt = self.g.GetCell(cell_cor[0],cell_cor[1])
		

	#initialize attributions
	def initAttr(self, cell_cor):
		attributions = {
			"TT"		: self.takeTime,
			"isMine"	: False,
			"celltype"	: "normal",
		}