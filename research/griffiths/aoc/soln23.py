import heapq
from typing import Optional

VALUE = [0] * 70  # ord('D') = 68
for c, v in zip('ABCD', [1, 10, 100, 1000]):
    VALUE[ord(c)] = v

PART = 2 # either 1 or 2
# PROBLEM_P = b'BACDBCDA       '  # test in problem description
PROBLEM_P = b'ADCABDCB       ' # xdavidliu actual input

def InsertPart2(p: bytes):
    return p[0:1] + b'DD' + p[1:3] + b'CB' + p[3:5] + b'BA' + p[5:7] + b'AC' + p[7:]

assert PART in (1, 2)
if PART == 2:
    PROBLEM_P = InsertPart2(PROBLEM_P)

H4 = len(PROBLEM_P) - 7
H = H4 // 4
SPACE = ord(' ')

PARTIAL = [None] * 70
for c in 'ABCD':
    PARTIAL[ord(c)] = [bytes(' ' * (H - n) + c * n, 'utf') for n in range(H)]

DIST = [[None] * len(PROBLEM_P) for _ in PROBLEM_P]
for r0 in range(4):
    for r1 in range(4):
        if r0 >= r1: continue  # within room dist not needed; also r0 > r1 handled by symmetry
        for k0 in range(H):
            for k1 in range(H):
                # Starting from i0, take k0+1 to enter hallway, then 2*(r1-r0) to reach
                # spot in hallway right outside r1, then k1+1 to reach i1.
                i0 = r0 * H + k0
                i1 = r1 * H + k1
                DIST[i0][i1] = DIST[i1][i0] = 2*(r1 - r0) + k0 + 1 + k1 + 1
for h in range(7):
    for r in range(4):
        for k in range(H):
            # start from ir, take k+1 to enter hallway, then abs(2*r - 2*h + 3) to ih.
            # Use diagram in RightOfRoom below to convince yourself of this.
            # ALSO! the first and last h are special, so subtract 1!
            ir = r * H + k
            ih = H4 + h
            val = k + 1 + abs(2*r - 2*h + 3)
            if h in (0, 6): val -= 1
            DIST[ir][ih] = DIST[ih][ir] = val

def RightOfRoom(r: int) -> int:
    # h = 0 1 2 3 4 5 6
    # r =    0 1 2 3
    return H4 + r + 2

def ClearBetweenRoom(p: bytes, r0: int, r1: int) -> bool:
    assert r0 != r1
    if r0 > r1: r0, r1 = r1, r0
    return p[RightOfRoom(r0) : RightOfRoom(r1)].isspace()

# h itself need not be space
def ClearHallwayToRoom(p: bytes, h: int, r: int) -> bool:
    rr = RightOfRoom(r)
    sl = slice(H4 + h + 1, rr) if h < r + 2 else slice(rr, H4 + h)
    psl = p[sl]
    # When the index of h in p coincides with rr, psl will be empty
    return (not psl) or psl.isspace()

def IsPartial(p: bytes, r: int) -> bool:
    return p[r*H : (r+1)*H] in PARTIAL[r + ord('A')]

def LowestSpace(p: bytes, r: int) -> int:
    i = r * H
    assert p[i] == SPACE
    nxt = (r+1)*H
    while i + 1 < nxt and p[i+1] == SPACE: i += 1
    return i

def Top(p: bytes, r: int) -> int:
    i = r * H
    while p[i] == SPACE: i += 1
    assert i < (r+1)*H
    return i

def Drop(p: bytearray, h: int, r: int) -> Optional[int]:
    ih = H4 + h
    ir = LowestSpace(p, r)
    c = p[ih]
    p[ih], p[ir] = p[ir], p[ih]
    return VALUE[c] * DIST[ih][ir]

DROP_MEMO = dict()

def DropUntilStop(p: bytearray) -> int:
    p0 = bytes(p)
    res = DROP_MEMO.get(p0)
    if res is not None:
        val, pf = res
        p.clear()
        p.extend(pf)
        return val
    is_partial = [IsPartial(p, r) for r in range(4)]
    improved = True
    val = 0
    while improved:
        improved = False
        if not p[H4:].isspace():
            for h in range(7):
                c = p[H4 + h]
                if c == SPACE: continue
                r = c - ord('A')
                if is_partial[r] and ClearHallwayToRoom(p, h, r):
                    val += Drop(p, h, r)
                    improved = True
        if not all(is_partial):
            for r in range(4):
                if is_partial[r]: continue
                ir = Top(p, r)
                c = p[ir]
                rd = c - ord('A')
                if not (is_partial[rd] and ClearBetweenRoom(p, r, rd)): continue
                ird = LowestSpace(p, rd)  # destination
                p[ir], p[ird] = p[ird], p[ir]
                val += VALUE[c] * DIST[ir][ird]
                improved = True
                is_partial[r] = IsPartial(p, r)  # The source room may become partial.
    DROP_MEMO[p0] = (val, bytes(p))
    return val

def Dijkstra(p0: bytes) -> int:
    hp = [(0, p0)]
    best = dict()
    DONE = bytes('A' * H + 'B' * H + 'C' * H + 'D' * H + ' ' * 7, 'utf')
    while hp:
        cost, p = heapq.heappop(hp)
        # invariant: everything popped cannot be further DroppedUntilStop
        if p == DONE: return cost
        b = best.get(p)
        if b is not None:
            assert cost >= b  # cannot be < b because it must've been previously popped
            continue
        best[p] = cost
        for r in range(4):
            if IsPartial(p, r): continue
            ir = Top(p, r)
            c = p[ir]
            for h in range(7):
                ih = H4 + h
                if not (p[ih] == SPACE and ClearHallwayToRoom(p, h, r)): continue
                pa = bytearray(p)
                pa[ir], pa[ih] = pa[ih], pa[ir]
                new_cost = cost + VALUE[c] * DIST[ir][ih] + DropUntilStop(pa)
                pp = bytes(pa)
                bb = best.get(pp)
                if bb is not None:
                    assert new_cost >= bb
                else:
                    heapq.heappush(hp, (new_cost, pp))

# For debugging purposes; not actually needed
def Draw(p: bytes) -> None:
   """ex: Draw('BACDBCDA.......')"""
   p = p.decode('utf').replace(' ', '.')
   print('#############')
   hall = p[H4:]
   draw_hall = hall[0] + '.'.join(hall[1:-1]) + hall[-1]
   print(f'#{draw_hall}#')
   for i in range(H):
       x = '#'.join(p[i:H4:H])
       side = '##' if i == 0 else '  '
       print(f'{side}#{x}#{side}')
   print('  #########  ')

print(f'part {PART} = {Dijkstra(PROBLEM_P)}')
