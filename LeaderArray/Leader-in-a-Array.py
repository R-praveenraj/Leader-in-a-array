#Given an integer array A containing N distinct integers, 
#you have to find all the leaders in array A. 
#An element is a leader if it is strictly greater than all the elements to its right side.
#PS: The rightmost element is always a leader.
#Input   A = [16, 17, 4, 3, 5, 2]    Output   [17, 2, 5]

def leader(array):
    lead=[]
    maximum=-float('inf')
    for i in range(len(array)-1,-1,-1):
        if array[i]>maximum:
            maximum=array[i]
            lead.append(array[i])
    return lead


array=[16, 17, 4, 3, 5, 2]
print(leader(array))