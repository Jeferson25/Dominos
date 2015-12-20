"""

zero  =   [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6]]
one   =   [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6]]
two   =   [[2,2],[2,3],[2,4],[2,5],[2,6]]
three =   [[3,3],[3,4],[4,5],[3,6]]
four  =   [[4,4],[4,5],[4,6]]
five  =   [[5,5],[5,6]]
six   =   [[6,6]]

deck = []
deck.append(zero)
deck.append(one)
deck.append(two)
deck.append(three)
deck.append(four)
deck.append(five)
deck.append(six)
tails = []
for size in deck:
	for size0 in size:
		tails.append(size0)



p1 = []
p2 = []
p3 = []
p4 = []

shuffle(tails)
for x in tails:
		if len(p1) != 7:
			p1.append(x)
			tails.remove(x)
		
		elif len(p2) != 7:
			p2.append(x)
			tails.remove(x)

for x in tails:
                if len(p3) != 7:
                        p3.append(x)
                        tails.remove(x)

s = 0
while len(p4) != 7:
	p4.append(tails[s])
	tails.remove(tails[s])
	s + s+1

########
print(tails)
print("------------")
print(p1)
print(p2)
print(p3)
print(p4)
print("-----------")
######333
place = List()
def move(place, p):
	try:
		if place.head is None:
			place.insert_end(p)
			print("yes - start ", p)
		elif place.head.data[0] == p[1]:
			print (p , "yes beginning")
			place.insert_beginning(p)
		elif place.head.data[0] == p[0]:
			p[0], p[1] = p[1], p[0]
			print (p , "yes switch begin")
			place.insert_beginning(p)
		elif place.tail.data[1] == p[0]:
			place.insert_end(p)
			print (p , "yes end")
		elif place.tail.data[1] == p[1]:
			p[0], p[1] = p[1], p[0]
			print (p , "yes switch end")
			place.insert_end(p)
		else:	
			pass
			print("no", p)
	except IndexError:
		place.insert_end('null')

def validMove(p):
	if place.head is None:
		return True
	elif place.head.data[0] == p[0] or place.head.data[0] == p[1]:
		return True
	elif place.tail.data[1] == p[0] or place.tail.data[1] == p[1]:
		return True
	else:	
		return False

def findVallidValue(player):
	index_with_valid_moves = []
	for x in player:
		if validMove(x) == True:
			index_with_valid_moves.append(player.index(x))
			#print index_with_valid_moves
		else:
			#print(index(x), " is not vallid")
			pass

	return index_with_valid_moves
			
def randomMove(player):
	# 
	# TODO IF THERE IS NO VAIILED MOVES? 
	#
	vallid = findVallidValue(player)
	if vallid != []:
		x = random.choice(vallid)
		move(place, player[x])
		player.remove(player[x])
		#print(player, "dominos for" )
	else:
		pass		

	
place.show()
move(place, p1[5])
print(place.head.data , "head")
print(place.tail.data , "tail")
move(place, p3[0])
move(place, p2[6])
move(place, p1[1])
move(place, p3[4])
move(place, p4[4])
print(place.head.data , "head")
print(place.tail.data , "tail")

def returnList(st):
	lst = []
	try:
		if st == '1':
			lst = p1[0]
		elif st == '2':
			lst = p1[1]
		elif st == '3':
			lst = p1[2]
		elif st == '4':
			lst = p1[3]
		elif st == '5':
			lst = p1[4]
		elif st == '6':
			lst = p1[5]
		elif st == '7':
			lst = p1[6]
		elif st == 'pass':
			pass
		else:
			print("this is wrong")	
	except IndexError:
		lst = 'null'		
	return lst
			
#def playHuman():

def theGameIsStillOn(player):
	if len(player) == 0:
		#print("this ", player, "won the game")
		return True
	else:
		return False

#
# TODO -> TOHEED 
#

#
# TODO -> Qaflah
#
#: '''or theGameIsStillOn(p2) != True or theGameIsStillOn(p3) != True or theGameIsStillOn(p4) != True:'''
def playRandomMoves():
	while theGameIsStillOn(p1) != True or theGameIsStillOn(p2) != True or theGameIsStillOn(p3) != True or theGameIsStillOn(p4) != True:
		#print (p1 ,"your dominaos")
		place.show() 
		'''
		print "this is the arena"
		inp = raw_input("enter index: ")
		#print(place.isItThere(returnList(inp)))
		if place.isItThere(returnList(inp)) != True:
			move(place, returnList(inp))
			try:
				p1.remove(returnList(inp))	
			except ValueError:
				pass
		else:
			print("in line 193")
		'''
		randomMove(p1)
		randomMove(p2)
		randomMove(p3)
		randomMove(p4)
	print("this game is over")
	

playRandomMoves()

place.show()

randomMove(p1)
print(findVallidValue(p2), "moves for 4")
randomMove(p2)
print(findVallidValue(p3), " moves for three" )
randomMove(p3)
print(findVallidValue(p4), " moves for 4" )
randomMove(p4)
place.show()
#print("count -> ", place.count())

print("----")
print(p1)
"""

