
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

""" 

looped through left to right, then top to bottom

	  -> -> -> -> -> -> -> -|
							|
|<--------------------------v
|
v->   -> -> -> -> ...

output is a list of quads representing this combination = [
  ['a', 'a', 'a', 'a', 'b', 'b', 'c'],
  ['a', 'a', 'a', 'a', 'b', 'b', 'c'],
  ['d', 'd', 'e', 'e', 'b', 'b', 'f']
]

List output of Quads:
X: 0 Y: 0 W: 4 H: 2
X: 4 Y: 0 W: 2 H: 3
X: 6 Y: 0 W: 1 H: 2
X: 0 Y: 2 W: 2 H: 1
X: 2 Y: 2 W: 2 H: 1
X: 6 Y: 2 W: 1 H: 1

"""
world = [
  [1, 1, 1, 1, 2, 2, 1],
  [1, 1, 1, 1, 2, 2, 1],
  [1, 1, 2, 2, 2, 2, 2]
]

n = len(world)
m = len(world[0])

o = [] # list of output quads
merged = [[False for _ in range(m)] for _ in range(n)] # if tile was visited -> True and therefore doesnt have to be checked again and meshed again

for y in range(n): # loop through map
  x = 0
  while x < m:
    
    if merged[y][x]: # if allready merged -> continue to look at next tile
      x += 1
      continue

    t = world[y][x] # block at world coordinates
    w = h = 1 # width and height of quad

    while x + w < m and t == world[y][x + w] and not merged[y][x + w]: 
		# x + w < m -> while in width bounds
		# t == world[y][x + w] -> while its the same kind of tile
		# not merged[y][x + w] -> not allready looked at
      w += 1 # increase width and continue expanding to the right

    while y + h < n: # while in height bounds
      good = True
      for i in range(w): # loop through row
        if t != world[y + h][x + i]: # if the tile is different -> cant expand downwards
          good = False
          break
      if good:
        h += 1 # whole row of the width of the row above matches -> expand height
      else:
        break
    
    for j in range(h):
      for i in range(w):
        merged[y + j][x + i] = True # set all of the new matched tiles to True to not further look at
    
    o.append(Quad(x, y, w, h, t)) # append to output
    x += w # expand by with and continue looking there for new quads

    debug(o) # dump debug info to console