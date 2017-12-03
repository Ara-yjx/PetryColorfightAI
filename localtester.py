import petryailib as petry
import localserver as server

#GLOBAL SETTINGS
AI = [] #AIs
AI_NUM = 8

g = server.Game()
#

AI.append(petry.PetryAI(g, "0P", None, "battle"))

#g.Print()

for s in AI[0].Soldiers:
	if s.isMine:
		print("MINE:")
		s.print()
		
print("---")


max_evalS = 0
max_evalS_S = None

for s in AI[0].Soldiers:
	if AI[0].outFrontline(s):
		print("FRONTLINE:")
		s.print()
		evalS = AI[0].eval(AI[0].getAttrbutions(s))
		print("EVAL() = "+str(evalS))
		if evalS>max_evalS:
			max_evalS_S = s
			max_evalS = evalS

#g.PlayerAttackCell(AI[0].myId, max_evalS_S.cor[0], max_evalS_S.cor[1])
g.AttackCell(max_evalS_S.cor[0], max_evalS_S.cor[1])
g.Refresh()
#g.Print()




"""
while True:
	for anAI in AI:
		if g.PLAYERS[anAI.g.id] <=0 : #if this AI is ready to move
			eval_result = anAI.eval()
			atk = g.PlayerAttackCell(anAI.g.id, eval_result[0], eval_result[1])
			#print attack result 
			if atk == 0: 
				print("AT " + str(g.NOW) +\
					" [" + str(anAI.g.i) + "] ATTACK (") +\
					str(eval_result[0]) + "," + str(eval_result[1]) + ") SUCCESS"
			else: 
				print("AT " + str(g.NOW) +\
					" [" + str(anAI.g.i) + "] ATTACK (") +\
					str(eval_result[0]) + "," + str(eval_result[1]) +\
					") FAIL: ERROR_CODE=" + str(atk)

	g.getNextTimePass
"""