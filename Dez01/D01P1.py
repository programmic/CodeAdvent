with open(  "Dez01/input.txt", "r", encoding = "utf-8" )  as tmp_data_in:
    numbers = tmp_data_in.read( ) .split( )   
    numbers = list( map( int, numbers) ) 
l1 = []
l2 = []
u1 = []
u2 = []

for i, number in enumerate( numbers ) :
    if i % 2 == 0:
        l1.append( number )
        u1.append( number )
    else:
        l2.append( number )
        u2.append( number )


l1 = sorted(l1)
l2 = sorted(l2)

counter = 0
for idx in range ( len( l1 ) ) :
    tmpC = 0
    print( f"{u1[idx]} {u2[idx]} | ", end="") 
    print( f"{l1[idx]} {l2[idx]} | ", end="") 

    tmpC += abs(l1[idx] - l2[idx])
    counter += tmpC
    print ( f"{tmpC}  || {counter}") 