     
     def integralOfNormal(t):
     
         k = 0
         a = []
         for n in range(100):
     
             f = n*2+1
             #print(f)
             l = np.power(t, f) * np.power(-1, n) / math.factorial(n) / (n*2+1)
             #print(l, n)
             k += l
             a.append(l)
     
         return  k 
