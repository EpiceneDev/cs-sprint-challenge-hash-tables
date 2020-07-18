
def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # ht = {}
    # #create new lists with positive and negative 
    # #iterate thru the lists comparing
    # # or
    # #check each number to be equal and opposite
    # #put the number (no sign) into results
    # for num in a:
    #     if num >= 0:
    #         ht[num] = True
    
    # numlist = []

    # for num in a:
    #     if num < 0 and ht[abs(num)]:
    #         numlist.append(abs(num))
        

    #     print(numlist)
    
    # return numlist
    h = {}
    r = []
    for i in a:
        if i >= 0:
            h[i] = True
        # print(h)
    for i in a:
        if i < 0 and abs(i) in h:
            r.append(-i)
    print(r)
    return r
   



if __name__ == "__main__":
    # result = has_negatives([1,2,3,-4])
    print(has_negatives([1,2,3,-4]))
    # print(has_negatives([-1,-2,1,2,3,4,-4]))

