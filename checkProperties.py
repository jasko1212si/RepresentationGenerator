# Check if the structure's predicates and functions are closed
def checkClosure(numOfElements, conv, comp, po):

    if numOfElements != len(conv):
        raise Exception("Converse length %d, should be %d, Exiting" %
                                                (len(conv), numOfElements))

    for i in range(numOfElements):
        if i not in conv:
            raise Exception("%d does not have a conv, Exiting" % i)

    if len(comp) != numOfElements:
        raise Exception("Bad composition matrix dimension, Exiting")

    for row in comp:
        if len(row) != numOfElements:
            raise Exception("Bad composition matrix dimension, Exiting")

        for elem in row:
            if elem < 0 or elem >= numOfElements:
                raise Exception("Composition not closed, Exiting")

    for pair in po:
        if len(pair) != 2:
            raise Exception("Bad patrial order dimension, Exiting")
        for elem in pair:
            if elem < 0 or elem >= numOfElements:
                raise Exception("Order contains illegal elements, Exiting")

# Check if the structure is associative
def checkAssoc(numOfElements, comp):
    for a in range(numOfElements):
        for b in range(numOfElements):
            for c in range(numOfElements):
                if comp[comp[a][b]][c] != comp[a][comp[b][c]]:
                    raise Exception("%d;(%d;%d) != (%d;%d);%d, Exiting"
                                                                %(a,b,c,a,b,c))

# Check the Identity
def checkId(numOfElements, comp):
    for a in range(numOfElements):
        if comp[0][a] != a:
            raise Exception("1';%d != %d, Exiting"%(a,a))


# Check if the algebra is a group (provided associativity and identity)
def checkGroup(numOfElements, conv, comp, partialOrder):
    for i in range(numOfElements):
        #check converse is inverse
        if comp[i][conv[i]] != 0:
            return False

        #check only one element (i) is in the set of elements greater than i
        if len(partialOrder[i]) != 1:
            return False
    return True

# Check the converse axioms are obeyed
def checkConv(numOfElements, conv, comp):
    if conv[0] != 0:
        raise Exception("conv of identity not identity, Exiting")

    for i in range(numOfElements):
        if conv[conv[i]] != i:
            raise Exception("conv of conv %d does not equal %d, Exiting"
                                                                    % (i,i))

    for a in range(numOfElements):
        for b in range(numOfElements):
            if conv[comp[a][b]] != comp[conv[b]][conv[a]]:
                raise Exception("(%d;%d)~ != %d~;%d~, Exiting" %(a,b,b,a))

# Check anti-reflexivity of the Order
def checkOrder(numOfElements, partialOrder):
    for a in range(numOfElements):
        for b in range(numOfElements):
            if a!=b and a in partialOrder[b] and b in partialOrder[a]:
                raise Exception("%d < %d and %d < %d, but %d != %d, Exiting"
                                                            % (a,b,b,a,a,b))

def checkMonotone(numOfElements, conv, comp, partialOrder):
    #check monotonicity of conv
    for a in range(numOfElements):
        for b in range(numOfElements):
            if a in partialOrder[b] and conv[a] not in partialOrder[b]:
                raise Exception("%d<%d, but not %d~<%d"%(b,a))

    #check monotonicity of ;
    for a in range(numOfElements):
        for b in range(numOfElements):
            if a in partialOrder[b]:
                for c in range(numOfElements):
                    if comp[a][c] not in partialOrder[comp[b][b]]:
                        raise Exception("%d<%d, but not %d;%d<%d;%d, Exiting"
                                                            % (b,a,b,c,a,c))


# check for all a: 1 < a;conv(a)
def checkTotality(numOfElements, conv, comp, partialOrder):
    for a in range(numOfElements):
        if comp[a][conv[a]] not in partialOrder[0]:
            return False
    return True
