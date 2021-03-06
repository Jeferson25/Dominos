class ListNode(object):

    def __init__(self, data, next):
        self.data = data
        self.next = next
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    ###########################################
    ###########################################
class List:
    def __init__(self):
	    self.head = None
    	    self.tail = None

    def show(self):
        print "Showing list data:"
        current_node = self.head
        while current_node is not None:
            print current_node.data, 
	    current_node = current_node.next
        

    def append(self, data):
        node = ListNode(data, None)
        if self.tail is None:
            self.tail = self.head = node
        else:
            self.head.next = node
        self.head = node
    def insert(self, node, data):
        new_node = ListNode(data, node.next)
        node.next = new_node
        if self.tail == node:
            self.tail = new_node
    def insert_end(self, data):
        if self.tail is None:
            new_node = ListNode(data, None)
            self.head = self.tail = new_node
        else:
            self.insert(self.tail, data)
    def insert_beginning(self, data):
        new_node = ListNode(data, self.head)
        self.head = new_node
    def appendH(self, data):
        node = Node(data, None)
        if self.tail is not  None:
                self.head = node
        else:
                while(self.head.next != None):
                        self.head = self.head.next
                self.head = node
#    def show(self):
#	while list.next != None:
#		print(list.data)
#		list = list.next
    def iterate(self):
        node = list.head
        while node is not None:
            print(node.data)
            node = node.next
    
    def count(self):
	node = self.head
	c = 0
	while node is not None:
		c = c+1
		node = node.next
	return c


    def isItThere(self, domino):
	re = False
	#print(domino, "heeeere")
	current = self.head
        while current and re is False:
            if current.data == domino:
		re = True
	    else:
		current = current.next
	return re
	
"""
list = List()
for x in range(1,10):
    list.insert_end(x)
print(list)

list.insert_beginning(99)
#list.iterate()
list.show()
"""
