#enumerate powerset\{}
def powerSet(size, numOfElements):
    if (size == 1):
        return[[i] for i in range(numOfElements)]
    ret = []
    smaller = powerSet(size-1, numOfElements)
    ret += smaller
    for i in range(numOfElements):
        temp = []
        for s in smaller:
            if i > s[len(s)-1]:
                t = s[:]
                t.append(i)
                temp.append(t)
        ret += temp
    return ret

def constructUpwardlyClosed(numOfElements, partialOrder):
    power = powerSet(numOfElements, numOfElements)

    upwardlyClosed = []

    for p in power:
        include = True
        for a in p:
            for b in partialOrder[a]:
                if b not in p:
                    include = False
                    break
            if not include:
                break
        if include:
            upwardlyClosed.append(p)

    return upwardlyClosed

def constructTotal(numOfElements, conv, comp, partialOrder):
    upwardlyClosed = constructUpwardlyClosed(numOfElements, partialOrder)

    rep = [[[] for i in range(len(upwardlyClosed))]
                    for i in range(len(upwardlyClosed))]

    for i in range(len(upwardlyClosed)):
        for j in range(len(upwardlyClosed)):
            for a in range(numOfElements):
                aInij = True
                for s in upwardlyClosed[i]:
                    temp = comp[s][a]
                    if temp not in upwardlyClosed[j]:
                        aInij = False
                        break
                if not aInij:
                    continue
                for t in upwardlyClosed[j]:
                    temp = comp[t][conv[a]]
                    if temp not in upwardlyClosed[i]:
                        aInij = False
                        break
                if aInij:
                    rep[i][j].append(a)

    return rep

def constructGroup(numOfElements, conv, comp):
    return [[[comp[conv[a]][b]] for b in range(numOfElements)]
                                        for a in range(numOfElements)]
