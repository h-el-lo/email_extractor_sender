###### New things learned ######

* I learned of context managers. A context manager is an object that defines a runtime context within the with-as statement. Python defines variables within the with-as block and automatically cleans them up soon as the block has completely run. E.g

with open('data.txt') as file:
    data = file.readlines
    print(int(data[0]))

This implies that the 'file' variable is unavailable until runtime when that specific with-as statement is run. This also implies that the file variable is done away with automatically, soon as the with-as block is completely run.
https://www.pythontutorial.net/advanced-python/python-context-managers/

* In the example above, if there were a ValueError resulting fron the presence of a string instead of an integer, without the with-as statement and block, the file.close() might not run properly, as such, the file might not close properly. This problem could be solved using the try-except-finally structure, forcing the file.close() to run at the 'finally' block. However, this prove verbose. So, in its place, a context manager is introduced. The use of a context manager would ensure that the 'file' is properly closed since the 'file' OBJECT is only initiated at runtime with the '__enter()__' method and cleaned up immediately after with the '__exit()__' method. This is better explained in webpage with the link above.


* Also, content managers are not supported by all types. They are unsupported by types like lists etc.

* readline() function reads a line of the file and return it in the form of the string. It takes a parameter n, which specifies the maximum number of bytes that will be read. However, does not reads more than one line, even if n exceeds the length of the line. It will be efficient when reading a large file because instead of fetching all the data in one go, it fetches line by line. readline() returns the next line of the file which contains a newline character in the end. Also, if the end of the file is reached, it will return an empty string.

* readlines() is used to read all the lines at a single go and then return them as each line a string element in a list. This function can be used for small files, as it reads the whole file content to the memory, then split it into separate lines. We can iterate over the list and strip the newline ‘\n’ character using strip() function. https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/.

* Handling the smtp.gmail.com api. https://towardsdatascience.com/how-to-easily-automate-emails-with-python-8b476045c151.


