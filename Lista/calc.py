import numpy as np

def sorting(x1,x2):
    x2_ = x2.argsort()
    x2 = x2[x2_]
    x1 = x1[x2_]
    return x1,x2

def simplex(c,A,b,indices,tam):
  count = 0
  
  while(True):
    #print(A)
    #print(c)
    #print(indices)
    N = A[:,:tam]
    B = A[:,tam:]
    cN = c[:tam]
    cb = c[tam:]
    #print(B)
    #print(N)
    #print(cN)
    #print(cb)
    w = np.dot(cb.T,np.linalg.inv(B))
    c_ = cN.T - np.dot(w.T,N)
    k = np.max(c_)
    #print('Vetor de custos reduzidos:',c_)
    #print(k)
    #print(indices)
    if(not k<=0):
        entrar = indices[:tam][c_==k][0]
        #print('A variável que vai entrar é',entrar)

        yk = np.dot(np.linalg.inv(B),A.T[indices[entrar-1]- 1])
        b_ = np.dot(np.linalg.inv(B),b)
        #print(b_,yk)
        r_ = np.array([i/j if j!=0 else 1e125 for i,j in zip(b_,yk)])
        r = np.min(r_)
        sair = indices[tam:][r_==r][0]
        #print('A variável que vai sair é',sair)
        indices[sair-1] = entrar
        indices[entrar-1] = sair

        aux = np.copy(c[sair-1])
        c[sair-1] = c[entrar-1]
        c[entrar-1] = aux

        aux = np.copy(A.T[:][sair-1])
        A.T[:][sair-1] = A.T[:][entrar-1]
        A.T[:][entrar-1] = aux

        count += 1
        #print('#############################################################')
    else:
        #print(B)
        #print(cN,cb)
        b_ = np.dot(np.linalg.inv(B),b)
        print(f'A função custo é igual a = {np.dot(cb,b_)}')
        b_ = np.hstack((np.zeros(len(indices) - len(b_)),b_))
        b_,indices =  sorting(b_,indices)
        for i,j in zip(indices,b_):
          print(f'A variável de índice x{i} = {j}')
        break