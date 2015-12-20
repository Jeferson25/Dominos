class Node(object):
    
    def __init__(self, data, next):
        self.data = data
        self.next = next
    ###########################################                                             
    ###########################################                                    
class SingleList(object):                                
    
    head = None                                                                         
    tail = None                                                                   
                                                                                              
    def show(self):
        print "Showing list data:"
        current_node = self.head
        while current_node is not None:
            print current_node.data, " -> ",
            current_node = current_node.next
        print None
    
    def append(self, data):
        node = Node(data, None)
        if self.tail is None:
            self.tail = self.head = node
        else:
            self.head.next = node
        self.head = node

    def appendH(self, data):
	node = Node(data, None)
	if self.tail is not  None:
		self.head = node
	else:
		while(self.head.next != None):
			self.head = self.head.next
		self.head = node
#	current = self.head 
#	while current is not None:
#		#self.head = self.head.next
#		current = current.next
	#self.head = node
#	self.head.next = self.head #and self.head.next = self.head.next.next

    def printHead(self):
	print self.head.data
		

#from random import shuffle
  
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
i = 0
tails = []
for size in deck:
        for size0 in size:
#               print(size0)
#               print(" ")
                tails.append(size0)



p1 = []
p2 = []
p3 = []
p4 = []
i1 = 0
i2 = 0
#shuffle(tails)
for x in tails:
                if len(p1) != 7:
                        p1.append(x)
#                       print("p1: ", x)
                        tails.remove(x)

                elif len(p2) != 7:
                        p2.append(x)
 #                       print("p2: ", x)
                        tails.remove(x)

for x in tails:
                if len(p3) != 7:
                        p3.append(x)
  #                      print("p3: ", x)
                        tails.remove(x)
"""
for x in tails:
                while len(p4) != 7:
                        p4.append(x)
   #                     print("p4: ", x)
                        tails.remove(x)
"""
s = 0
while len(p4) != 7:
        p4.append(tails[s])
        tails.remove(tails[s])
        s + s+1

"""
print(tails)
print(p1)
print(p2)
print(p3)
print(p4)

"""

def pla(place, p):
	lis = []
	if len(place) == 0:
		place.append(p)
	elif place[0][0] == p[0]:
		place =  [p] + place 
	elif place[-1][1] == p[1]:
		place.append(p)
	else:
		print("inv")
	return place

place = []
pla(place, p1[1])
print(place)
a = [2,3]
b = [0,3]
c = [6,2]
f = [4,6]
pla(place, a)
pla(place, c)
pla(place, f)
print(pla(place, b))
print(place)


##########################
d = SingleList()
 
#d.append(p1)
#d.append(p2)
#d.append(p3)
#d.append(p4)

def move(index, node):
  	if node.head is None:
		node.append(index)
		print("yes")
	else:
		print("no")
#move(p1[0], d)
"""
d.append(10)
d.append(5)
d.append(15)
d.append(3)  
d.show()
d.printHead()
d.appendH(6)
d.printHead()
d.show()
"""
