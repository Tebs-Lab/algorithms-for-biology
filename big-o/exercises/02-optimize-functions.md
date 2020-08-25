# Optimizing Code With Big O In Mind

The complexity/Big O value of a program is only one aspect of what might make a program fast or slow, but it is an important one: Often times taking code from one complexity class to another [e.g. `O(n^2)` ==> `O(n)`] can be the difference between a program that cannot realistically be run to completion, and one that can. 

Further optimizations may not change the complexity class, but can still significantly improve the runtime speed of a program. For example, perhaps a critical for loop can be modified to perform fewer operations per loop, while still achieving the same result [e.g. 35n + 10 ==> 10n + 10].

Moving a piece of code from one complexity class to a better one often requires us to completely change our strategy. Optimizations of the second variety are more often slight changes to the existing strategy. There are opportunities for both kinds of optimization in this exercise but we are primarily focused on the first variety of optimization. Keep that in mind as you work though this exercise. 

## The Task

Two of the four functions we saw in the last section are much slower than they need to be. For each of these functions:

* Identify the section or sections of the code that represent the dominant complexity class.
    * Is it a function call?
    * A series of deeply nested for loops?

* Before you start changing the code, describe an alternate strategy to solve the problem that would be in a smaller complexity class.

* Write at least three test cases, so that you can verify your new code still works as you make changes!
    * Consider making one of these test cases with "big" data (remember, Big O only really matters as the data gets large!) 

* Rewrite the code to apply your new strategy. 
    * Remember to test it!

* Perform a Big O analysis on your new code — is it true that it's in a better complexity class? 
    * How much better is it?

* **Bonus points**, read [this article](https://realpython.com/python-timer/) and then use what you learned to time your code and the old code.
    * How much faster is it?
    * Are the speed differences more apparent with larger input data?

## A Few Hints

* Try to find ways to unnest for loops. 
    * Nested loops typically represent multiplicative workloads such as O(n^2) or O(n*m).
    * Removing such a nesting to create something with a runtime of 2n or O(n + m) is a huge improvement.

* Try to find ways to look at each relevant piece of data the fewest number of times.
    * If you're looping over a long string twice to perform two tasks, try to do both tasks at the same time and loop over the data only once.

* Choosing the right data structure to store your data can be a big deal.
    * Finding an item in a list or array is O(n), but finding an item in a dictionary, hashmap, or set is O(1).

* Sometimes adhering to the DRY principle is at odds with optimization.
    * Reusing code is great, but sometimes using a function in another function causes you to duplicate work.

