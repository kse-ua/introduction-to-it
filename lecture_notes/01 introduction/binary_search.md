Initial algorithm:

```
1  Pick up catalog
2  Open catalog at the middle
3  Look at card
4  If person is on card
5      File Exist!
6  Else if person is earlier in catalog
7      Open to middle of bottom half of catalog
8      Go back to line 3
9  Else if person is later in catalog
10     Open to middle of upper half of catalog
11     Go back to line 3
12 Else
13     Quit
```

Slightly more formal:

```
1  Pick up catalog
2  Define low as 0
3  Define up as catalog’s size
4  While low is smaller that up
5      Define middle as (low + up)/2
6  	 Look at card #middle	
7      If person is on card
8      	  File Exists!
9  	 If person is earlier in catalog
  Define	up as middle - 1
 else 
	  Define low as middle + 1	
10 Quit
```

Even more formal:

```
1  Pick up catalog
2  low = 0
3  up = catalog’s size
4  While low <= up
5      middle = (low + up)/2
6  	 Look at card #middle	
7      If person is on card
8      	  File Exists!
9  	 If person is earlier in catalog
      up = middle - 1
 else 
	  low = middle + 1	
10 Quit
```