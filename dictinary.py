class Node:
    def __init__(self,value):
        self.value=value
        self.list=[]
        self.next=None
        

class dictionary_list:
    def __init__(self,value):
        new_node=Node(value.split('.')[1])
        self.head=new_node
        self.tail=new_node
        self.length=1
           
    def append(self,value):
        exe=value.split('.')[1]
        temp=self.head
        while temp is not None:
            if temp.value == exe:
                exist=True
                
                list_point=temp
                temp=None
            else:
                temp=temp.next
                exist = False
        
        if exist:
            list_point.list.append(value)
            
        else:
            new_node=Node(value.split('.')[1])
            new_node.list.append(value)
            if self.head is None :
                self.head=new_node
                self.tail=new_node
                 
            else:
                self.tail.next=new_node
                self.tail=new_node
            self.length +=1
        
   
    def print_data(self):
        temp=self.head
        while temp is not None:
            print(temp.value,"->",temp.list)
            temp=temp.next


        
        
        

        