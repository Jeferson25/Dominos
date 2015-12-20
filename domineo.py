from random import shuffle
from random import randint
from SinNode import List
from SinNode import ListNode
import random
from collections import Counter




class Player:
	dominos = []
	
	def __init__(self, name):
		self.name = name
	def add_dominos(self, setD):
		self.dominos =setD
	i = 0

	'''
	while dominos[i][ is not None:
		sc = sc + dominos[i]
		i = i + 1
	'''
	def get_score(self, dominos):
		sc = 0
		for score in dominos:
			
			for score0 in score:
				sc = sc + score0
							
		return sc


	def get_theindex(self, dominos):
		print(dominos)

def generate_tiles():

	zero  =   [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6]]
	one   =   [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6]]
	two   =   [[2,2],[2,3],[2,4],[2,5],[2,6]]
	three =   [[3,3],[3,4],[3,5],[3,6]]
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
	shuffle(tails)
	#
	# TODO -> do a butter shuffle method so that one does not have five domins of the same set or 4 dess  
	#
	return tails

def devide_plyer(number_of_plyers):
	temp = [[] for x in range( int(number_of_plyers) )] 
	#temp = temp.remove[0]
	dominos = generate_tiles()
	#    print(dominos, "here")
	p1 = []
	p2 = []
	p3 = []
	p4 = []
	if number_of_plyers == 4:
	    
	    temp[0].append(dominos[0:7])
	    temp[1].append(dominos[7:14])
	    temp[2].append(dominos[14:21])
	    temp[3].append(dominos[21:28])
	else:
	    print("no")
	lst = []
	lst.append(temp[0][0])
	lst.append(temp[1][0])
	lst.append(temp[2][0])
	lst.append(temp[3][0])
	return lst

def move(place, p, player):
	try:
		if place.head is None:
			place.insert_end(p)
			#print("yes - start ", player.name)
		elif place.head.data[0] == p[1]:
			#print (player.name , "yes beginning")
			place.insert_beginning(p)
		elif place.head.data[0] == p[0]:
			p[0], p[1] = p[1], p[0]
			#print (player.name , "yes switch begin")
			place.insert_beginning(p)
		elif place.tail.data[1] == p[0]:
			place.insert_end(p)
			#print (player.name , "yes end")
		elif place.tail.data[1] == p[1]:
			p[0], p[1] = p[1], p[0]
			#print (player.name , "yes switch end")
			place.insert_end(p)
		else:	
			pass
			#print("no", player.name)
	except IndexError:
		place.insert_end('null')

def validMove(place,p):
	
	if place.head is None:
		return True
	elif place.head.data[0] == p[0] or place.head.data[0] == p[1]:
		return True
	elif place.tail.data[1] == p[0] or place.tail.data[1] == p[1]:
		return True
	else:	
		return False

def findVallidValue(place, player):
	index_with_valid_moves = []
	for x in player:
		if validMove(place,x) == True:
			index_with_valid_moves.append(player.index(x))
			#print index_with_valid_moves
		else:
			#print(index(x), " is not vallid")
			pass

	return index_with_valid_moves
			
def randomMove(place,player):
	# 
	# TODO IF THERE IS NO VAIILED MOVES? 
	#
	
  
	vallid = findVallidValue(place,player.dominos)
	if vallid != []:
		x = random.choice(vallid)
		move(place, player.dominos[x], player)
		player.dominos.remove(player.dominos[x])
		#print(player.name)
		#print(player, "dominos for" )
	else:
		pass

def returnList(st, p1):
	lst = []
	p1 = p1.dominos
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

def theGameIsStillOn(p1,p2,p3,p4):
	p1 = p1.dominos
	p2 = p2.dominos
	p3 = p3.dominos
	p4 = p4.dominos
	
	if len(p1) == 0 or len(p2) == 0 or len(p3) == 0 or len(p4) == 0:
		#print("this ", player, "won the game")
		return True
	else:
		return False


#
# TODO -> TOHEED -> 
#

#
# TODO -> playhuman -> 
#

def hasDoubples(p):
	doms = p.dominos
	print(doms)
	lst = []
	for x in doms:
		if x[0] == x[1]:
			lst.append(x)

	print lst	
	
#
# TODO -> myDoor -> (TESTING)
#

def testMyDoor(p):
	i = 0
	lst= []
	lst1 = []
	while i < 7:
		lst.append(myLuckyNumber(p, i))
		i = i+1
	for item in lst:
		if item != []:
			lst1.append(item[0])

	return lst1

def myDoor(p):
	doms = p.dominos
	luck = testMyDoor(p)
	print luck
	for x in luck:
		for y in doms:
			if x == y[0] or x == y[1]:
				print y

def myLuckyNumber(p, find):
	doms = p.dominos
	my_door = []
	count =0
	# = 0
	goal = 0
	for x in doms:		
		for y in x:
			if find == y:
				count = count+1
				if count > 2:
					count = 0 	
					while count < 1: 	 
						goal = y
						my_door.append(y)
						count = count +1
	return my_door


	
#def getMy
		
def getThwinir(p1, p2, p3, p4):
	a = p1.get_score(p1.dominos)
	b = p2.get_score(p2.dominos)
	c = p3.get_score(p3.dominos)
	d = p4.get_score(p4.dominos)
	lst = []
	lst.append(a)
	lst.append(b)
	lst.append(c)
	lst.append(d)
	re = ''
	theWiningScore = min(lst)
	if theWiningScore == a:
		re = p1
		#print(p1.name, a)
	elif theWiningScore == b:
		re = p2
		#print(p2.name, b)
	elif theWiningScore == c:
		re = p3
		#print(p3.name, c)
	elif theWiningScore == d:
		re = p4
		#print(p4.name, d)
	else:
		print("more than one winiers")
	return re


#
# TODO -> Kaflah (Testing) -> (DONE) 
#



def theGameIsClosed(place):
	try:
		node = place.head
		
		check = place.head.data[0]
		check0 = place.tail.data[1]
		
		c = 0
		s = 0
		if check == check0:
			#print("yes they are the same")
			while node is not None:
				indexZ = node.data[0]
				indexO = node.data[1]		
				if check == indexZ:
					c = c+1
				elif check == indexO:
					s = s+1
				node = node.next
			
		#else:
			#print("no, they are not")
		x = s+c
		#print(x)
		if x == 7:
			return True
		return False
	except AttributeError:
		pass	

def doesItMatch(place, domino):
	boo = False
	try:
		if place.head is None:
			boo = True

		tail = place.tail.data[1]
		head = place.head.data[0]
		if domino[0] == tail:
			boo = True
		elif domino[1] == tail:
			boo =  True
		elif domino[0] == head:
			boo =  True
		elif domino[1] == head:
			boo =  True
		else:
			boo =  False
	except AttributeError:
		pass	
	return boo

def getTheScore(p1, p2, p3, p4):
	a = len(p1.dominos)
	b = len(p2.dominos)
	c = len(p3.dominos)
	d = len(p4.dominos)
	lst = []
	lst.append(a)
	lst.append(b)
	lst.append(c)
	lst.append(d)
	re = ''
	theWiningScore = min(lst)
		
	return theWiningScore

def random_game():	
	place = List()
	one = Player("talal")
	two = Player("nasser")
	three = Player("khalil")
	four = Player("alsarrani")
	lst = devide_plyer(4)
	one.add_dominos(lst[0])
	two.add_dominos(lst[1])
	three.add_dominos(lst[2])
	four.add_dominos(lst[3])

	inp = ''
	con = len(one.dominos)
	con2 = len(two.dominos)
	con3 = len(three.dominos)
	con4 = len(four.dominos)
	boo = True
	
	while  (theGameIsClosed(place) != True):
		if theGameIsStillOn(four,two,three,four) == True:
			break
		
		print one.dominos
		print place.show()
		print '\n'
		inp = raw_input("enter index: ")
		#print(place.isItThere(returnList(inp)))
		
		######################################################
		if doesItMatch(place, returnList(inp, one)) == True:
			move(place, returnList(inp, one), one)
			try:
				one.dominos.remove(returnList(inp, one))	
			except ValueError:
				pass
		else:
			pass
			print("in line 193")
		########################################################
		
		if len(one.dominos) == 0:
			break
		randomMove(place, one)
		if theGameIsStillOn(four,two,three,four) == True:
			break
		randomMove(place, two)
		if theGameIsStillOn(four,two,three,four) == True:
			break
		randomMove(place, three)
		if theGameIsStillOn(four,two,three,four) == True:
			break
		randomMove(place, four)	

	
	imW = getThwinir(one, two , three, four)
	thePlayersList = []
	
	print one.dominos
	print one.get_score(one.dominos)
	print four.dominos
	print four.get_score(four.dominos)
	print two.dominos
	print two.get_score(two.dominos)
	print three.dominos
	print three.get_score(three.dominos)
	print("*****")
	thePlayersList.append(one.get_score(one.dominos) + four.get_score(four.dominos))
	
	thePlayersList.append(three.get_score(three.dominos) + two.get_score(two.dominos))
	print thePlayersList[0]
	print thePlayersList[1]
	print("----------------------")
	return thePlayersList


def test_games():
	c = 0
	teamOneScore = 0
	teamTwoScore = 0
	boo = False
	while boo != True:
		random_game()
		teamTwoScore = teamTwoScore + random_game()[1]
		if teamTwoScore >= 120:
			boo = True
		teamOneScore = teamOneScore + random_game()[0]
		if teamOneScore >= 120:
			boo = True	
	print(teamOneScore, teamTwoScore)


def main():
	place = List()
	one = Player("talal")
	two = Player("nasser")
	three = Player("khalil")
	four = Player("alsarrani")
	lst = devide_plyer(4)
	one.add_dominos(lst[0])
	two.add_dominos(lst[1])
	three.add_dominos(lst[2])
	four.add_dominos(lst[3])
	#hasDoubples(one)
	print one.dominos
	print(myDoor(one))
#main()
test_games()

