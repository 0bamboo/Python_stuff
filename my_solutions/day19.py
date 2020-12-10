# ================================= Q76 ============================
import zlib
print('========================= Q76 ==========================')
s = b"hello world!hello world!hello world!hello world!"
compress = zlib.compress(s)
print(s)
print(compress)

# ======================== DONE =========================
#  ======================= Q77 =============================== 
print('======================= Q77 ======================')
import time as t 
now = t.time()
for i in range(100):
    z = 1 + 1
after = t.time()
exec_time = after - now
print('Execution time = {}'.format(exec_time))
# ===================== DONE ========================
# ==================== Q78 ====================
import random as r
print('======================== Q78 =====================')
lis_to_shuffle = [3,6,7,8]
r.shuffle(lis_to_shuffle)
print('The list after shuffling : ', lis_to_shuffle)
# ==================== DONE ==========================
#  ===================== Q79 ================================
print('======================== Q79 =======================')
sub = ['I', 'You']
verb = ['Play', 'Love']
obj = ['Hockey', 'Football']
for i in range(6):
    print(r.choice(sub), r.choice(verb), r.choice(obj))
print('=========== another one ================')
for s in sub:
    for v in verb:
        for o in obj:
            print(s, v, o)
    
# =========================== THE END =========================