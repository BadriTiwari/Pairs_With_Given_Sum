import pandas as pd
def Pairs_With_Given_Sum(In_Array, Num):
    
    Pairs = pd.DataFrame(None, None, columns = ['Num1','Num2'])
    L = len(In_Array)
    print('\n Lenght of the Array = ', L)
    print('\n Araray before sorting: \n', In_Array)
    
    InArray = list(sorted(In_Array))
    print('\n Araray after sorting: \n', InArray)
    
    i = j = None
    
    for i in range(len(InArray) - 1):
        print ('\n i = ', i) 
        print('Current pair (', InArray[i], ',', InArray[L-1],')')
        if (InArray[i] + InArray[L-1]) == Num:
            print('Found a Pair: ', InArray[i], ' and ', InArray[L-1])
            Pairs = Pairs.append({'Num1':InArray[i], 'Num2':InArray[L-1]}, ignore_index = True)
        
        elif (InArray[i] + InArray[L-1]) > Num:
            j = L - 1
            print ('\n j = ', j)         
            for k in range(j, i, -1):
                print ('\n k = ', k) 
                print('Current pair (', InArray[i], ',', InArray[k-1],')')
                
                if (InArray[i] + InArray[k-1]) == Num:
                    print('Found a Pair: ', InArray[i], ' and ', InArray[k-1])
                    Pairs = Pairs.append({'Num1': InArray[i], 'Num2': InArray[k-1]}, ignore_index = True)                
                elif (InArray[i] + InArray[k - 1]) < Num:
                    print('NOT a Pair for the required sum: ', InArray[i], ' and ', InArray[k-1])
                    break
        print('\n Current status of found Pairs: \n', Pairs)
    return Pairs               

# Test Case                
Numbers = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,10,11,12,13,14,1,2,3,4,5,6]    
Sum = 20
Pairs_for_Sum = Pairs_With_Given_Sum(Numbers, Sum)
print('\n Pair of Numbers with the SUM = ', Sum, ': \n', Pairs_for_Sum)
