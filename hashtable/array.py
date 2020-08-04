#Add up and print the sum of the all of the minimum elements of each inner array. 
#Each array may contain additional arrays nested arbitrarily deep, in which case the 
# minimum value for the nested array should be added to the total.



#The expected output for the above input is:
#8 + 4 + 90 + -1 + 9 + -7 + -56 + -6 + 201 + 0 + 18 = 260

#scroll through arrays, and find minimum values for each connected piece of the array


unsorted = [ 6, 4, 3, 54, 74, 23, 12]

def remove_sort(unsorted):
    sortd = []
    if len(unsorted) == 1:
        return
            
    for i in range(unsorted):
        sortd.append(min(i))
        unsorted.remove(min(i))
        remove_sort(unsorted)

print(remove_sort(unsorted))        


   




