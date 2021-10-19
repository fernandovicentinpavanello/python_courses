- Handling Errors

Try Statement

We can use try statements to handle exceptions. There are four clauses you can use (one more in addition to those shown in the video).

    try: This is the only mandatory clause in a try statement. The code in this block is the first thing that Python runs in a try statement.
    except: If Python runs into an exception while running the try block, it will jump to the except block that handles that exception.
    else: If Python runs into no exceptions while running the try block, it will run the code in this block after running the try block.
    finally: Before Python leaves this try statement, it will run the code in this finally block under any conditions, even if it's ending the program. E.g., if Python ran into an error while running code in the except or else block, this finally block will still be executed before stopping the program.

Specifying Exceptions

We can actually specify which error we want to handle in an except block like this:

try:
    # some code
except ValueError:
    # some code

Now, it catches the ValueError exception, but not other exceptions. If we want this handler to address more than one type of exception, we can include a parenthesized tuple after the except with the exceptions.

try:
    # some code
except (ValueError, KeyboardInterrupt):
    # some code

Or, if we want to execute different blocks of code depending on the exception, you can have multiple except blocks.

try:
    # some code
except ValueError:
    # some code
except KeyboardInterrupt:
    # some code

- Accessing Error Messages

When you handle an exception, you can still access its error message like this:

try:
    # some code
except ZeroDivisionError as e:
   # some code
   print("ZeroDivisionError occurred: {}".format(e))

This would print something like this:

ZeroDivisionError occurred: integer division or modulo by zero

So you can still access error messages, even if you handle them to keep your program from crashing!

If you don't have a specific error you're handling, you can still access the message like this:

try:
    # some code
except Exception as e:
   # some code
   print("Exception occurred: {}".format(e))
