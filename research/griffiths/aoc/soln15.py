import sys
from icecream import ic

def main () -> int:

    itxt = open("input", mode='r').read().strip().splitlines()

    iq = {(i,j): {'$': int(v), 'v': None} for i, r in enumerate(itxt) for j, v in enumerate(r)} #input
    cq = dict() # $ed
    vq = dict() # visited
    last = (max([r for (r,c) in iq.keys()]), max([c for (r,c) in iq.keys()]))

    def getncs(r: int, c: int) -> set:
        return [i for i in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)] \
            if i[0] >= 0 and i[0] <= last[0] and i[1] >= 0 and i[1] <= last[1]]

    def getnns(nc:tuple, q:dict) -> set:
        return {ik: iv for ik, iv in q.items() if ik in getncs(*nc)}

    def qsrt(q:dict) -> set:
        return(dict(sorted(q.items(), key=lambda i: i[1]['$'])))

    def qget(q:dict) -> dict:
        q = qsrt(q)
        fk = list(q.keys())[0]
        fv = q.get(fk)
        del q[list(q.keys())[0]]
        return(({fk:fv},q))

    def qput(q:dict, i:dict) -> dict:
        q.update(i)
        return(q)

    cq = qput(cq,{(0,0):{'$': 0, 'v': None}})
    del iq[(0,0)]

    while len(iq):
        (p,cq) = qget(cq)
        pc = list(p.keys())[0]
        cost = p[pc]['$']

        for k,v in getnns(pc,iq).items():
            if cost <= v['$'] or v['v'] == None:
                cq = qput(cq,{k:{'$': cost + v['$'], 'v': pc}})
                del iq[k]
        
        vq = qput(vq,{pc:{'$': cost,'v': p[pc]['v']}})

    for k,v in cq.items():
        if k in vq.keys():
            if vq.get(k)['$'] < v['$']:
                vq = qput(vq,{k:{'$': v['$'], 'v': v['v']}})
        else:
            vq = qput(vq,{k:{'$': v['$'], 'v': v['v']}})

    print(vq.get(last,0)['$'])

    
if __name__ == '__main__':
    sys.exit(main()) 

import sys
import heapq

def main () -> int:

    def getncs(r: int, c: int) -> set:
        return [i for i in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)] \
            if i[0] >= 0 and i[0] <= lr and i[1] >= 0 and i[1] <= lc]

    itxt = open("input", mode='r').read().strip().splitlines()
    
    jq = [(int(v),i,j) for i, r in enumerate(itxt) for j, v in enumerate(r)] 
    lr, lc = (max([r for (v,r,c) in jq]), max([c for (v,r,c) in jq])) #last

    jq = [(((r+c+v-1)%9+1),ir+(r*lr)+r,ic+(c*lc)+c) \
        for (v,ir,ic) in jq for c in range(5) for r in range(5)] #embiggen
    lr, lc = (max([r for (v,r,c) in jq]), max([c for (v,r,c) in jq])) #recalc last

    iq = {(r,c): int(v) for (v,r,c) in jq} 
    oq = dict()

    jq.pop(0) # pop (0,0)
    cq = [(0,0,0)]
    heapq.heapify(cq)
    
    while len(jq) != len(oq.keys()):
        (v,r,c) = heapq.heappop(cq)

        for (nr, nc) in getncs(r,c):
            if v < iq.get((nr,nc)) or (r,c) not in oq.keys():
                heapq.heappush(cq,(iq.get((nr,nc))+v, nr,nc))

        oq.update({(r,c):v})

    oq.update({(r,c):v for (r,v,c) in cq if v < oq.get((r,c),99999999)})
    print(oq.get((lr,lc)))

if __name__ == '__main__':
    sys.exit(main())
