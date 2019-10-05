import copy
# tab = ([[0,1,2],
#         [3,4,5],
#         [6,7,8]])
# grid= ([[1,0,2],
#         [5,4,3],
#         [6,7,8]])
tab=[[0,1,3],[2,4,5],[6,7,8]]
grid=[[1,3,0],[2,4,5],[6,7,8]]
matrice_ouverte=[]
matrice_fermee=[grid]
succ=[]

def  heuristique(grid):
    cmp=0
    for i in range(3):
        for j in range(3):
            if(tab[i][j]!=grid[i][j]):
                cmp +=1        
                
    return cmp


def cout(x1,y1,grid,i):
    l=[]
    l=verif(grid,i)
    x2=l[0]
    y2=l[1]
    return (x2-x1)+(y2-y1)
            
def verif(grid,f):
    for i in range(3):
        for j in range(3):
            if (grid[i][j]==f):
                l=[]
                l.append(i)
                l.append(j)
                return l

def f_(grid):
    for i in range(3):
        for j in range(3):
            f=cout(i,j,grid,tab[i][j])+heuristique(grid)
            return f
    

        
    
def position_vide_i():
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                return (i)
def position_vide_j():
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                return (j)

def Permutation_Droite():
    print("Permutation_Droite")
    i=position_vide_i()
    j=position_vide_j()
    m=copy.deepcopy(grid)
           
    if j<2 :
        pos=m[i][j]
        m[i][j]=m[i][j+1]
        m[i][j+1]=pos
        if len(m)==4:
            m[3]=f_(m)
        else:
            m.append(f_(m))
        return m    
            
def Permutation_Gauche():
    print("Permutation_Gauche")
    i=position_vide_i()
    j=position_vide_j()
    
    n=copy.deepcopy(grid)
    if j>0:
                
        pos=n[i][j]
        n[i][j]=n[i][j-1]
        n[i][j-1]=pos
        
        if len(n)==4:
            n[3]=f_(n)
        else:
            n.append(f_(n))
        return n



def Permutation_Haute():
    print("Permutation_Haute")
    i=position_vide_i()
    j=position_vide_j()
    
    h=copy.deepcopy(grid)
    
    if i>0:
                
        pos=h[i][j]
        h[i][j]=h[i-1][j]
        h[i-1][j]=pos
       
        if len(h)==4:
            h[3]=f_(h)
        else:
            h.append(f_(h))
        return h

def Permutation_Basse():
    print("Permutation_Base")
    i=position_vide_i()
    j=position_vide_j()
    
    l=copy.deepcopy(grid)
    
    if i<2:
                
        pos=l[i][j]
        l[i][j]=l[i+1][j]
        l[i+1][j]=pos
        
        if len(l)==4:
            l[3]=f_(l)
        else:
            l.append(f_(l))
        return l

def test(x,succ):
    if( x!=None and x  not in succ and x  not in matrice_ouverte):
        return True
    else:
        return False
def remplir_matrice_successeur(m):
    succ=[]
    Matrice_Permutation_Basse=Permutation_Basse()
    Matrice_Permutation_Droite=Permutation_Droite()
    Matrice_Permutation_Gauche=Permutation_Gauche()
    Matrice_Permutation_Haute=Permutation_Haute()
    if(test(Matrice_Permutation_Basse,succ)):
        succ.append(Matrice_Permutation_Basse)
    if(test(Matrice_Permutation_Droite,succ)):
        succ.append(Matrice_Permutation_Droite)
    if(test(Matrice_Permutation_Gauche,succ)):
        succ.append(Matrice_Permutation_Gauche)
    if(test(Matrice_Permutation_Haute,succ)):
        succ.append(Matrice_Permutation_Haute)
    return sorted(succ,key=lambda x: x[3])


def remplir_matrice_fermante(succ):
    global matrice_fermee,grid
    matrice_fermee.append(succ[0])
    grid=succ[0][0:3]
    del succ[0]
    return succ


def remplir_matrice_ouvrante(succ):
    global matrice_ouverte
    matrice_ouverte.extend(succ)


def main():
    global grid, matrice_fermee,matrice_ouverte
    print("Grid but: \n",tab,"\n")
    while grid != tab:
        print("Grid\n",grid,"\n")
        succ=remplir_matrice_successeur(grid)
        print("Successeur\n",succ,"\n")
        succ=remplir_matrice_fermante(succ)
        print("Fermante\n",matrice_fermee,"\n")
        remplir_matrice_ouvrante(succ)
        print("Ouvrante\n",matrice_ouverte,"\n")
    return("Resultat aboutit",[i[0:3] for i in matrice_fermee])
        


print(main())

    





                


    
    

        

