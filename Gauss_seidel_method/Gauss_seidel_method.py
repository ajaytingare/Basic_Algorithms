
    

eq1 =  [12,3,-5,1]
eq2 =  [1,5,3,28]
eq3 =  [3,7,13,76]

# we have to select starting points for the roots
x,y,z = 1,0.5,0.6


for i in range(20):
    
    x = ( eq1[3] - (eq1[1]*y) - (eq1[2]*z) ) / eq1[0]
    
    y = ( eq2[3] - (eq2[0]*x) - (eq2[2]*z) ) / eq2[1] 
    
    z = ( eq3[3] - (eq3[0]*x) - (eq3[1]*y) ) / eq3[2]
    
    print(x,"  ",y,"  ",z)
    
print(f"\nx: {x},\ny: {y}, \nz: {z}")

    
    



