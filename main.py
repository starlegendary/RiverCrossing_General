def checkall( f, ls): #some commonly used function
    return sum(list(map(f,ls))) == len(ls)
def checkone(f, ls):
    for i in ls: 
        if f(i): return True
    return False
def bfs(src,tar, toaction, tonext, tofood, isequal):
    def env(node): #Define Environment 
        result = ['','']
        i_side,j_side, i,j  = toside(node,human)
        for m in j_side:
          if(m in tofood.keys()):
              if(tofood[m] in j_side):
                  j_side = j_side.replace(tofood[m],'')
        result[i],result[j] = i_side, j_side
        return result
    explored = []
    q = [[src]]
    while q != []:
        currpath = q.pop(0)
        currnode = currpath[-1]
        #Get last node of the path in a queue
        if not checkone(lambda x: isequal(currnode,x), explored):
            allaction = toaction(currnode) #Get all next movement
            explored.append(currnode) #Add to is explored
            
            for action in allaction:
                nextnode = env(tonext(currnode, action)) #state action
                nextpath = list(currpath) + [nextnode] #add state to record

                if(isequal(nextnode,tar)): 
                    return nextpath
                q.append(nextpath)

    return None
def toaction(node):
      allnext = []
      for animal in animals:
          move = human + animal
          if(isvalid(node,move)):
              allnext += [move]
      allnext += human
      return allnext

def toside(node,m):
      if m in node[0]: return node[0], node[1], 0 ,1
      elif m in node[1]: return node[1], node[0], 1,0
      else: return None

def tonext(node, action):
    result = ['','']
    i_side,j_side, i,j  = toside(node,action[0])

    for a in action:
        i_side = i_side.replace(a,'')
        j_side = j_side + a
    result[i],result[j] = i_side, j_side
    return result


def isequal(node1, node2):
    if(list(map(len,node1)) != list(map(len,node2))): return False
    return checkall(lambda side:checkall(lambda x: x in node2[side], node1[side]), range(len(node1)))


def isvalid(node,move):
      side, _,_,_ = toside(node,move[0])
      if(side == None): return False
      return checkall(lambda x: x in side, move)

init = ['hbcd','']
targ = ['','hbcd']
human = 'h'
animals = ''.join(set(init[0]+init[1])).replace(human,'')

for step in bfs(targ,init , toaction, tonext, {'b':'c', 'c':'d'},isequal):
    print(step)