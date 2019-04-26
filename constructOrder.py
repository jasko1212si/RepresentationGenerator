def transitiveClosure(numOfElements, po):
    #construct partial order
    partialOrder = [[i] for i in range(numOfElements)]

    for pair in po:
        partialOrder[pair[0]].append(pair[1])

    #assure transitivity
    added = True
    while added:
        added = False
        for a in range(numOfElements):
            for b in partialOrder[a]:
                if a != b:
                    for c in partialOrder[b]:
                        if c not in partialOrder[a]:
                            added = True
                            partialOrder[a].append(c)

    return partialOrder
