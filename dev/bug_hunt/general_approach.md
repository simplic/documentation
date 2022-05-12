# Starting the bug hunt


## Define the bug scope

- Where is/isn't the bug?
- What should have happend?
- When does/doesn't the bug happen?
- Why does the bug happen? 

It's important to know what is and isn't part of the bug. Sometimes multiple things go wrong at the same time and you need to know what you are working on right now.
If necessary you can create addionaly tickets for the other bugs you find while searching for your current bug.

Related to knowing what is part of the bug is knowing what the desired behavior is. What is the intended behavior of things, be sure to have a clear idea of what should happen.

Make sure you know under which condition the bug happens. Does it always happen or only when a specific thing is selected.

Sometimes you already have an idea why the bug is happening because you have seen a similar problem before. Check these ideas quickly but do not get lost in these hunches.


## Reduce the bug scope

- Check the input and output
- Create clear cases what could cause the problem.
- Reduce the time testing by creating the smallest possible test case where the bug occurs.
- Prioritize your possible error cases by effort, knowhow & likelihood.

By checking the input and output starting with the general process and the gradually reducing the scope to more specific cases/processes, you get a good idea where exactly things go wrong.

Creating cases for the different possible error sources can make it easier and clearer to follow the search and finally find the bug. **It is a good idea to start with looking
into the data inside the database first.**

When you have a process that works with 100 entries and none of them work, you do not need to try to run the process with all 100 entries. Work on getting 1 entry to work
after that you can expand your testing to the rest.

Giving priority to cases that take little effort, don't need specific knowhow and have a high likelyhood of fixing the problem will increase the efficency of your bug hunt.
Starting with the most time consuming proble, you have no idea about is a terrible idea.


### Getting someone elses help

Before getting someone else involved in the problem be sure to be clear on what the exact problem is and how to describe it to someone else. (See questions above)
Tell them what you have done and what you have tried already.
Sometimes they won't know how to fix it either but nontheless you should inform them after finding the problems solution without them.


### Look for similar code that works

Rarely will you have a problem nobody has had before. So looking inside our GitHub for another case where the same components have been used and compare it to the problem side.
Another good option is search for other with a similar or the same problem. If you have a specific error code search for tha in combination with the tool you are using.
If that doesn't deliver the solution you can look for a more general use case of the tools involved in the problem case.
