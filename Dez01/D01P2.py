with open(  "Dez01/input.txt", "r", encoding = "utf-8" )  as tmp_data_in:
    numbers = tmp_data_in.read( ) .split( )   
    numbers = list( map( int, numbers) ) 
l1 = []
l2 = []

for i, number in enumerate( numbers ) :
    if i % 2 == 0: l1.append( number )
    else:         l2.append( number )

score = 0

print(l1)
for i in l1:
    print("checking", i ,"| ", end="")
    c = l2.count(i)
    print(f"score {score} += i ({i}) * c ({c})  |  score increases by {c*i}")
    score += c * i
print (score)
