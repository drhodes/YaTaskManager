#!/usr/bin/env python
import repl

# https://semver.org/
VERSION = "1.0.0"

def main():
    repl.REPL().loop()
    
if __name__ == "__main__":
    print("building agenda!")
    main()
