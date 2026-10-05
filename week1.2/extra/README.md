# Additional Work For Week 1.2

If you finish the tasks quickly and have time on your hands, here are some
other things you can try. Put your code for this additional work in this
directory, to keep it separate from the other tasks.

## Session 1

* Lists can be constructed using a feature called a **list comprehension**.
  Investigate this feature, and write some Python code to demonstrate it.

  Do the same for set comprehensions and dictionary comprehensions.

  # similar to java streams.
  fruitsWithA = [f for f in fruits if "a" in f] # this does not modify the original list

* Given a list `x`, what is the difference between these two lines of code?

  ```python
  x.sort() # sorts the list in question
  sorted(x) # returns a new sorted list
  ```

* Investigate the following types provided by the `collections` module in
  the Python standard library:

  + `namedtuple` # in python this gives tuples dot notation identifiers so you can access individual tuples. 
  + `deque` # in java, this is not thread safe. this data type allows for both pushing/popping and enqueuing/dequeuing
  + `Counter` # in python, this is a dictionary that represents the number of instances of elements in a collection.

  In each case, write a small program that demonstrates how the collection
  can be used.

  # too lazy to write a program, but named tuples can be used in defining important coordinates in a tuple-based coordinate system. 
  # deques can be used for anything that requires putting values in the end and the start, such as queues in a rollercoaster where some people might have priority because of some pass.
  # counters can be used to count the number of votes cast for a specific candidate in an election.


## Session 2

* What does the following Python code return, and why?

  ```python
  answer = False
  isinstance(answer, int) 
  # not yet answered but its true because booleans are integers under the hood (boolean is subclass of int). 0 == false, everything else == true.
  # this is how c works with booleans. 
  ```

* Create new versions of the ATM simulator and calculator from Task 5.
  These new versions should use a match statement instead of a multi-branch
  if statement.

* Rewrite the calculator example from Task 5 so that it allows the user
  to enter their calculation as a single string, e.g., `2 + 5`, `4 * 37`.
