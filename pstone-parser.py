#!/usr/bin/env python


from pstone.parser import BasicParser


if __name__ == "__main__":
    snippet = """
        foo = "Hello, world"
        // this line should be skipped
        while i < 10 {
            sum = sum + i
            i = i + 1
        }
        sum
    """

    print("Hello, world!")
