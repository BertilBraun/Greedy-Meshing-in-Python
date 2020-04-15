
class Quad:
  def __init__(self, x, y, w, h, t):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.t = t
  
  def __repr__(self):
    return "X: " + str(self.x) + " Y: " + str(self.y) + " W: " + str(self.w) + " H: " + str(self.h) 

  def compare(self, o):
    if self.y != o.y:   return self.y < o.y
    if self.x != o.x:   return self.x < o.x
    if self.w != o.w:   return self.w > o.w
    return self.h >= o.h

  def inside(self, o):
    return o.y <= self.y and o.x <= self.x and o.x + o.w >= self.x + self.w and o.y + o.h >= self.y + self.h

def debug(o):
  OKBLUE = '\033[94m'
  ENDC = '\033[0m'
  q = o[-1]
  print (len(o))
  print (q)

  for j, merg in enumerate(merged):
    for i, mer in enumerate(merg):
      symb = '1' if mer else '0'
      if i >= q.x and i < q.x + q.w and j >= q.y and j < q.y + q.h:
        print (OKBLUE + symb + ENDC, end='')
      else:
        print (symb, end='')
    print ()

world = [
  [1, 1, 1, 1, 2, 2, 1],
  [1, 1, 1, 1, 2, 2, 1],
  [1, 1, 2, 2, 2, 2, 2]
]

n = len(world)
m = len(world[0])

o = []
merged = [[False for _ in range(m)] for _ in range(n)]

for y in range(n):
  x = 0
  while x < m:
    
    if merged[y][x]:
      x += 1
      continue

    t = world[y][x]
    w = h = 1

    while x + w < m and t == world[y][x + w] and not merged[y][x + w]:
      w += 1

    while y + h < n:
      good = True
      for i in range(w):
        if t != world[y + h][x + i]:
          good = False
          break
      if good:
        h += 1
      else:
        break
    
    for j in range(h):
      for i in range(w):
        merged[y + j][x + i] = True
    
    o.append(Quad(x, y, w, h, t))
    x += w

    debug(o)