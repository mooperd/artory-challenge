The phone matchup coding test.

A phone company keeps record of all calls that have been successfully
established. For these calls, the company registers
whether they fail mid-call or complete successfully. We are interested in
computing the "success ratio", which is defined by the number of successful
calls vs. absolute number of calls that involved a party.

The format is:
date: day.month.year 24hours:minutes
caller: phone number
callee: phone number
status: COMPLETED/FAILED

When 111 would call 222 and the call would end successfully, the following
entry would show up in the log_data:
1.1.2014 12:33,111,222,COMPLETED
This call is counted as completed for both parties!
If the same call fails mid-call, the line would look like this
1.1.2014 12:33,111,222,FAILED
This call is counted as failed for both parties!

Implement a function that takes log data from a string and turns it into a
data structure that represents the association between a number and a success
percentage-string which is ready for display.

Feel free to use any available modules from the language standard library.
Feel free to add test cases as you see fit.
 Also, send along an estimate of the time it took you
to complete this test.

We evaluate the submission based on: correctness, structure, appropriate
use of data structures, efficiency, appropriate use of standard library
functionality.

An example:

1.1.2014 12:01,111-222-333,454-333-222,COMPLETED
1.1.2014 13:01,111-222-333,111-333,FAILED
1.1.2014 13:04,111-222-333,454-333-222,FAILED
1.1.2014 13:05,111-222-333,454-333-222,COMPLETED
2.1.2014 13:01,111-333,111-222-333,FAILED

Resulting output of success rates:

111-222-333: 40.00%
454-333-222: 66.67%
111-333 : 0.00%
