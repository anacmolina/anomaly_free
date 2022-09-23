from params import generate_lk
import time

t=time.time()
lks = generate_lk(n=5, m=3, N=5000000)
print(time.time()-t)
print(lks.shape)
#print(lks)