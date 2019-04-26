import sys
import json
import checkProperties
import construct
import constructOrder

try:
    filename = sys.argv[1]
    fp = open(filename)
    o = json.load(fp)
except:
    print("Could not open file, Exiting")
    sys.exit()


numOfElements = o['numOfElements']
conv = o['conv']
po = o['ord']
comp = o['comp']
representation = []

try:
    checkProperties.checkClosure(numOfElements, conv, comp, po)
    checkProperties.checkId(numOfElements, comp)
except Exception as error:
    print(error)
    sys.exit()

partialOrder = constructOrder.transitiveClosure(numOfElements, po)

try:
    checkProperties.checkAssoc(numOfElements, comp)
except Exception as error:
    print(error)
    sys.exit()

if checkProperties.checkGroup(numOfElements, conv, comp, partialOrder):
    print("Algebra is a Group, Constructing")
    representation = construct.constructGroup(numOfElements, conv, comp)
else:
    try:
        checkProperties.checkConv(numOfElements, conv, comp)
        checkProperties.checkOrder(numOfElements, partialOrder)
        checkProperties.checkMonotone(numOfElements, conv, comp, partialOrder)
    except Exception as error:
        print(error)
        sys.exit()

    if checkProperties.checkTotality(numOfElements, conv, comp, partialOrder):
        print("Algebra is a Total Ordered Convoluted Monoid, Constructing")
        representation = construct.constructTotal(numOfElements,
                                                    conv, comp, partialOrder)

if representation:
    fp = open('representation.json', 'w')
    json.dump(representation, fp)
else:
    print("Could not Determine Representability")
