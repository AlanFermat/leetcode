def judgeCircle(moves):
	return  (moves.count("U")==moves.count("D")) and (moves.count("R")==moves.count("L"))
	
moves = "DRDLLUURLR"
print (judgeCircle(moves))