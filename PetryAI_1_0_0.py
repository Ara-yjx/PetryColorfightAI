# You need to import colorfight for all the APIs
import colorfight
import petryailib as petry
# import os
if __name__ == '__main__':

	# You need to join the game using JoinGame(). 'MyAI' is the name of your
	# AI, you can change that to anything you want. This function will generate
	# a token file in the folder which preserves your identity so that you can
	# stop your AI and continue from the last time you quit. 
	# If there's a token and the token is valid, JoinGame() will continue. If
	# not, you will join as a new player.
	g=colorfight.Game()
	g.JoinGame("petry")


	P = petry.PetryAI("Petry110")

	#petry.battleField[0].print()


	print("/")


	# Put you logic in a while True loop so it will run forever until you 
	# manually stop the game
	while True:
		# Use a nested for loop to iterate through the cells on the map
		print("HQ:")
		print(P.hqPosition)
		


		for i in P.allSoldiers():
			if i.isMine():
				i.print()

		"""
		#get the greastest potential
		max_p = -1
		max_p_sol = [0,0]

		for c in P.allSoldiers():
			# If the cell I got is mine

			if c.outFrontline():
				print("FRONTLINE: ")
				c.print()

				if not c.isTaking: 
					#if an outFrontline not being attacked
					if c.potential()>max_p:
						max_p_sol = c.cor()
						max_p = c.potential()

		# attack the one with max potential
		print("ATTACKING:  "+str(max_p_sol))

		if not P.call(max_p_sol).isMine():

			attackResult = P.G.AttackCell(max_p_sol[0],max_p_sol[1])
			print(attackResult)
		else:
			print("It's mine")
				# Get that adjacent cell
#                    cc = g.GetCell(x+d[0], y+d[1])
				# If that cell is valid(current cell + direction could be
				# out of range) and that cell is not mine
#                    if cc != None:
#                        if cc.owner != g.uid:
						# Attack the cell and print the result
						# if (True, None, None) is printed, it means attack
						#d is successful, otherwise it will print the error
						# code and error message
#                            print(g.AttackCell(x+d[0], y+d[1]))
						# Refresh the game, get updated game data


		"""

		input("PAUSED")
		
		P.refreshHq()