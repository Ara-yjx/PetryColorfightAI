import petryailib as petry
import localserver as server

#GLOBAL SETTINGS
AI = [] #AIs
AI_NUM = 8

g = server.Game()


AI.append(petry.PetrySimpleAI(str(i)+"P"))


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