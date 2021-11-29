# Generates a runnable .py file with an enormous if-else block.
# Overwrites any existing content in if-else.py

size = 25000000000

with open("C:\\if-else.py", "w") as file:
    file.write("# Joke script, returns true if odd or false if even\n\n\ndef isOdd(n):\n\tif n == 0:\n\t\treturn True\n")
    for i in range(1, size+1):
        file.write("\telif n == {}:\n\t\treturn {}\n".format(i, i % 2 == 1))
