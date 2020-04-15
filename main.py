
class Quad:
  def __init__(self, x, y, w, h, t):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.t = t
  
  def __repr__(self):
    return "X: " + str(self.x) + " Y: " + str(self.y) + " W: " + str(self.w) + " H: " + str(self.h) 

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
	    symb = OKBLUE + symb + ENDC
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

# list of output quads
o = [] 
# if tile was visited -> True and therefore doesnt have to be checked again and meshed again
merged = [[False for _ in range(m)] for _ in range(n)]

# loop through map
for y in range(n):
  x = 0
  while x < m:
    
	# if allready merged -> continue to look at next tile
    if merged[y][x]:
      x += 1
      continue

	# block at world coordinates
    t = world[y][x]
	# width and height of quad
    w = h = 1

		# x + w < m -> while in width bounds
		# t == world[y][x + w] -> while its the same kind of tile
		# not merged[y][x + w] -> not allready looked at
    while x + w < m and t == world[y][x + w] and not merged[y][x + w]: 
	  # increase width and continue expanding to the right
      w += 1

	# while in height bounds
    while y + h < n:
      good = True
	  # loop through row
      for i in range(w):
		# if the tile is different -> cant expand downwards
        if t != world[y + h][x + i]:
          good = False
          break
      if good:
		# the whole row of the width of the row above matches -> expand height
        h += 1
      else:
        break
    
    for j in range(h):
      for i in range(w):
		# set all of the new matched tiles to True to not further look at
        merged[y + j][x + i] = True
    
	# append a new Quad to the output
    o.append(Quad(x, y, w, h, t))
	# expand by with and continue looking there for new quads
    x += w

	# dump debug info to console
    debug(o)