def has_negatives(a):
    """
    YOUR CODE HERE
    """
    pos = []
    neg = []
    results = {}
    #create new lists with positive and negative 
    #iterate thru the lists comparing
    # or
    #check each number to be equal and opposite
    #put the number (no sign) into results
    for num in range(len(a)):
        if num < 0:
            neg.append(num)
        elif num >= 0:
            pos.append(num)
        
    
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
