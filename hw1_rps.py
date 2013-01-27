while True:
	p1=raw_input("Player1? ")
	if p1 not in ("rock", "paper", "scissors"):
		print ("not valid")
	else:
		p2=raw_input("Player2? ")
		if p2 not in ("rock", "paper", "scissors"):
			print ("not valid")
		else:
			break
print p1 , p2
win_cond={"rockrock":"00", "rockpaper":"01", "rockscissors":"10", "paperrock":"10", "paperpaper":"00", "paperscissors":"01","scissorsrock":"01", "scissorspaper":"10","scissorsscissors":"00"}

if win_cond[p1+p2]=="00":
	print "tie"
elif win_cond[p1+p2]=="10":
	print "Player1 wins"
else:
	print "Player2 wins"
