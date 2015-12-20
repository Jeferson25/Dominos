	a = 0
	d = 0
	fin1 = 0 
	count1 = 0
	goal2 = 0 
	find1 =  doms[a][d] 	
	for w in doms:
		for z in w:
			if find1 == z:
				fin1 = fin1+1
				print(fin1)
				if fin1 > 2:	
					if z != goal or z != goal1:
						while count1 < 1:
							goal2 = z
							#print(z, "z")
							my_door.append(z)
							count1 = count1 + 1
						print (goal2,  'goal2')
					
				else:
					if d < 7:
						
						find = doms[a+1][d+1]
					
			else:
					if a < 7:
						find = doms[a+1][d+1]

	find1 =  doms[a][d] 
	for w in doms:
		for z in w:
			if find1 == z:
				fin1 = fin1+1
				print(fin1)
				if fin1 > 2:	
					if z != goal:
						while count1 < 1:
							goal1 = z
							#print(z, "z")
							my_door.append(z)
							count1 = count1 + 1
						print (goal1,  'goal1')
					
				else:
					if d < 7:
						
						find = doms[a+1][d]
					
			else:
					if a < 7:
						find = doms[a][d+1]
