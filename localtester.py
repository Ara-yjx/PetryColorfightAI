import petryailib as petry
import localserver as server

PLAYER_LIST =[]
PLAYER_NUM = 8

g = server.Game()


for i in range(PLAYER_NUM):
	PLAYER_LIST.append(g.JoinGame(str(id)+"P"))

while True:

	for playerI in PLAYER_LIST:
		if g.PLAYERS[i].cd <=0 :
			