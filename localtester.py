import petryailib as petry
import localserver as server

#GLOBAL SETTINGS
AI = []
AI_NUM = 8

g = server.Game()


for i in range(PLAYER_NUM):
	AI.append(petry.PetrySimpleAI(str(i)+"P"))


while True:
	for anAI in AI:
		if g <=0 :#if this AI is ready to move
			