#!/usr/bin/env python
import repl

# https://semver.org/
VERSION = "1.0.0"

def main():
    repl.REPL().loop()
    
if __name__ == "__main__":
    print("Welcome to yet another task manager!")
    main()
