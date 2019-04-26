#Readme

The input algebra is an ordered convoluted monoid, if it is an ordered convoluted monoid and if it is an ordered convoluted monoid that obeys the pseudo-triangle law (i.e. a group). It then generates the representation.

The input it takes is a ```json``` file of that specifies the:

* ```numOfElements```: size of the algebra, i.e. the list of elements of the algebra will be generated as ```[0,1,...,numOfElements-1]``` and the element ```0``` will be the identity element

* ```conv```: the list signifying the converse function, i.e. the converse of the element ```i``` is stored at ```conv[i]```

* ```comp```: the cayley table of the composition operation, i.e. the composition of the elements ```i``` and ```j``` is stored at ```comp[i][j]```

* ```ord``` the list of ordered pairs ```[a,b]``` such that <i>a &#x2264; b</i>, which will form the ordering predicate after transitive closure and the inclusion of the reflexive pairs


An example is shown below

```
{
  "numOfElements":2,
  "conv":[0,1],
  "comp":[
           [0,1],
           [1,1]
         ],
  "ord":[[0,1]]
}
```

We implement a program that decides if an algebra is a group or a total ordered convoluted monoid and constructs a representation and saves the adjacency matrix of the representation graph into ```representation.json``` and exits otherwise.


Readme
The input algebra is an ordered convoluted monoid, if it is an ordered convoluted monoid and if it is an ordered convoluted monoid that obeys the pseudo-triangle law (i.e. a group). It then generates the representation.

The input it takes is a json file of that specifies the:

numOfElements: size of the algebra, i.e. the list of elements of the algebra will be generated as [0,1,...,numOfElements-1] and the element 0 will be the identity element

conv: the list signifying the converse function, i.e. the converse of the element i is stored at conv[i]

comp: the cayley table of the composition operation, i.e. the composition of the elements i and j is stored at comp[i][j]

ord the list of ordered pairs [a,b] such that a <= b, which will form the ordering predicate after transitive closure and the inclusion of the reflexive pairs

An example is shown below

{ "numOfElements":2, "conv":[0,1], "comp":[ [0,1], [1,1] ], "ord":[[0,1]] }

We implement a program that decides if an algebra is a group or a total ordered convoluted monoid and constructs a representation and saves the adjacency matrix of the representation graph into representation.json and exits otherwise.

Copyright 2018 Hideaki Tanabe.
#Readme

The input algebra is an ordered convoluted monoid, if it is an ordered convoluted monoid and if it is an ordered convoluted monoid that obeys the pseudo-triangle law (i.e. a group). It then generates the representation.

The input it takes is a ```json``` file of that specifies the:

* ```numOfElements```: size of the algebra, i.e. the list of elements of the algebra will be generated as ```[0,1,...,numOfElements-1]``` and the element ```0``` will be the identity element

* ```conv```: the list signifying the converse function, i.e. the converse of the element ```i``` is stored at ```conv[i]```

* ```comp```: the cayley table of the composition operation, i.e. the composition of the elements ```i``` and ```j``` is stored at ```comp[i][j]```

* ```ord``` the list of ordered pairs ```[a,b]``` such that a <= b, which will form the ordering predicate after transitive closure and the inclusion of the reflexive pairs


An example is shown below

```
{
  "numOfElements":2,
  "conv":[0,1],
  "comp":[
           [0,1],
           [1,1]
         ],
  "ord":[[0,1]]
}
```

We implement a program that decides if an algebra is a group or a total ordered convoluted monoid and constructs a representation and saves the adjacency matrix of the representation graph into ```representation.json``` and exits otherwise.
