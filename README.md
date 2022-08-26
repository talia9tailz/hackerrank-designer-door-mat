# Designer Door Mat
My solution to the challenge [here](https://www.hackerrank.com/challenges/designer-door-mat/problem) using an Object Oriented Programming approach.


###### Example Output:
```
Please supply an odd number: 9
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
```

Note: Though the challenge specifies that two integers `N` and `M` be supplied as input, `M` is granted to always be equal to `N * 3`. With this in mind, I wrote my solution to only require the first integer, `N`, and ignore `M` if supplied, as the value of `M` can be calculated using `N`. Furthermore, since `N` is required to be an odd integer, I have added a sanity check that prompts again if supplied with an even number.
