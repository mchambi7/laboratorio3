import sys
from array import array

line=sys.stdin.readline()
if not line:
    sys.exit(0)
t=int(line.strip())
queries=[]
max_b=0

for i in range(t):
    line=sys.stdin.readline()
    if not line: 
        break
    a_str, b_str=line.split()
    a=int(a_str)
    b=int(b_str)
    if a>b:
        a,b=b,a
    queries.append((a,b))
    if b>max_b:
        max_b=b
if not queries:
    sys.exit(0)

limit=max_b
primo=bytearray(b'\x01')*(limit+1)
primo[0]=primo[1]=0
for i in range(2, int(limit ** 0.5)+1):
    if primo[i]:
        inicio=i*i
        paso=i
        primo[inicio:limit + 1:paso]=b'\x00' * ((limit-inicio)//paso+1)
prefix = array('I',[0])*(limit+1)
contador=0
for i in range(limit+1):
    if primo[i]:
        contador+=1
    prefix[i]=contador

out_lines=[]
for a, b in queries:
    primb=prefix[b]
    prim1=prefix[a-1] if a > 0 else 0
    out_lines.append(str(primb - prim1))
sys.stdout.write("\n".join(out_lines))