import petryailib as petry
import colorfight as server
import math

#GLOBAL SETTINGS


def distance(a, b):
	return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

g = server.Game()


AI=petry.PetryAI(g, "Petry", eval, "battle")

#g.Print()
while True:
	"""
	for s in AI.Soldiers:
		if s.isMine:
			print("MINE:")
			s.print()
		
	print("---")
	"""
	if AI.secureBase():

		max_evalS = 0
		max_evalS_S = None

		for s in AI.Soldiers:
			if AI.outFrontline(s) and not s.isTaking:
				print("FRONTLINE:")
				s.print()

				attr = AI.getAttrbutions(s) 
			
				#evalS = AI.eval(attr)
				evalS = 1/attr["takeTime"]
				if attr["cellType"] == "gold": evalS*=5
				if attr["cellType"] == "energy": evalS*=1.2
				evalS /= (distance(AI.base, attr["cor"]))+0.1

				print("EVAL() = "+str(evalS))
				if evalS>max_evalS:
					max_evalS_S = s
					max_evalS = evalS

		#g.PlayerAttackCell(AI[0].myId, max_evalS_S.cor[0], max_evalS_S.cor[1])
		g.AttackCell(max_evalS_S.cor[0], max_evalS_S.cor[1])

	print("BASE:")
	print(AI.base)
	print("GAME REFRESHING")
	g.Refresh()
	print("AI REFRESHING")
	AI.refresh()
#g.Print()
