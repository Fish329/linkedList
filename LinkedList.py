class Node: 
    def __init__(self, data):
        self.data=data #the data stored in the node
        self.next= None #the next node in the list
        self.head= None #first node in the list. The example code didn't have this and I had to add it in order for the code to work.

    def insertAtBegin(self,data): #inserts a node at the start of the list.
        new_node=Node(data) #create new_node object with data provided
        if self.head==None: #If there isn't a head yet,
            self.head = new_node #then this node will be the head.
        else: #otherwise, shift the head down, and then make new_node the head.
            new_node.next=self.head
            self.head=new_node

    def insertAtIndex(self,data,index): #inserts a node at a specific index.
        new_node=Node(data) #new node with data provided
        current_node=self.head #This variable will detect the data that is inside the node we are currently looking at. The first node we look at is the head.
        position=0 #counter
        if position==index: #if the target position is at the very beginning,
            self.insertAtBegin(data) #use this instead.
        else: #otherwise start the loop
            while (current_node != None and position+1 !=index): #while we are not looking at a blank node and the next node isn't the target
                position=position+1 #increment
                current_node=current_node.next #move to next node
            if current_node != None: #if the target node is not empty,
                new_node.next=current_node.next #move the current list down,
                current_node.next=new_node #and insert the new node at the target
            else: #if the target node is empty,
                print("Index not present") #Put an error

    def insertAtEnd(self,data): #inserts a node at the end of the list.
        new_node=Node(data) #blah blah
        if self.head==None: #If there isn't a head yet, then the list must be zero length.
            self.head=new_node #this node will be the head.
            return #if that's the case, don't bother with the rest of the method.

        current_node=self.head #reports the data inside each node
        while (current_node.next): #until we reach a node with no next,
            current_node=current_node.next #move through the list.
        
        current_node.next=new_node #once we get the node at the end, insert a new node after that.
    
    def updateNode(self,val,index): #changes the data of the node at a specific index.
        current_node=self.head #data reporter variable
        position=0 #counter
        if position==index: #if the target node is the head,
            current_node.data=val #change the head data.
        else: #otherwise start the loop
            while (current_node!=None and position!=index): #until we reach the target node and it isn't blank
                position=position+1 #increment
                current_node=current_node.next #advance
            if current_node!=None: #if the target node isn't empty,
                current_node.data=val #replace the data
            else: #otherwise,
                print("Index not present") #put an error.

    def removeFirstNode(self): #removes the head node.
        if(self.head==None): #if there isn't a head yet,
            return #don't bother.
        self.head=self.head.next #otherwise make the next node the head.

    def sizeOfLL(self): #report the size of the list.
        if(self.head==None):#if the list has no head yet,
            return 0 #then the length is zero.

        current_node=self.head #data
        steps=1 #counter
        if current_node.next==None: #if the head is all there is,
            return 1 #then the length is one.
        
        while(current_node.next): #until we reach a node with no next,
            steps=steps+1 #increment
            current_node=current_node.next #advance
        return steps #once we reach the end variable, report how many nodes we came across.
    
    def printLL(self): #print the list.
        if self.head==None: #if the list has no head,
            return #don't bother. Otherwise, continue.
        current_node=self.head #reporter
        if (current_node.next==None): #if the head is all there is,
            print([[self.head,None]]) #just print the head,
            return #then don't bother with the rest of the method.
        toPrint=[] #empty list to be filled with nodes
        while (current_node.next):
            toPrint.append([current_node.data,current_node.next]) #add current node to toPrint
            current_node=current_node.next #advance
        toPrint.append([current_node.data,None]) #print the tail.
        print (toPrint) #print finished list. it is printed as an array of 2-entry arrays. the first entry of a 2-entry array is the data the node houses, and the second is the adress of the next node.

#Now that we have all that done, we can actually make the list.

myNode=Node("Hello World!")
myNode.insertAtBegin("Shahood")
myNode.insertAtEnd("Mason")
myNode.insertAtEnd("Nathan")
myNode.insertAtEnd("Gavin")
myNode.insertAtEnd("Muntag")
myNode.insertAtEnd("Leo")
myNode.insertAtEnd("Chris")
myNode.insertAtEnd("Marcos")
myNode.insertAtEnd("Aidan")
myNode.insertAtEnd("Ryan")
myNode.insertAtIndex("Jaiden",7)
myNode.printLL()
