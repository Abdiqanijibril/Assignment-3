'''

This code was cooked by the one and only AJ

'''
'''
def newlist():
    list1 = [1,2,3,4,5]
    list2 = [5,6,7,8,9]
    list3 = set(list1 + list2) 
    return list3



AJ = newlist()

print (AJ)

'''
'''
def AJ (number, letter):
    if len(number) != len(letter):
        print ("you are a dumbass")
    
    btchahh = ''.join([char * num for char, num in zip(letter, number)])
    
    return btchahh

print(AJ((1,2,3,4), 'Alex'))

'''