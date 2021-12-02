
def main(row, col):
    x = getWeight(row, col)
    printWeight(x)

def getWeight(row, col):
    x = 0
    #If either the row or column is less than zero 
    if row < 0 or col < 0:
        return ('Error, values cannot be less than zero')
    #If both row and column are zero, the person holds no weight
    elif row == 0 and col == 0:
        return x
    #If the col=0 and row does not, the person is on the left edge
    elif col == 0 and row != 0:
        return (128 + getWeight(row-1, col))/2 
    #If row =col and they don't=0 then they are on the right edge
    elif col == row and col != 0:
        return (128 + getWeight(row-1, col-1))/2
    #Else they are in the middle of the pyramid
    else:
        return(128 + getWeight(row-1, col-1)/2 + getWeight(row-1, col)/2)
        
def printWeight(x):
    print(x)
    
#Enter the row and column number you wish to test for
main(0,0)
