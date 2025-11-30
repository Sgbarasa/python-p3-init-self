#!/usr/bin/env python3

class Person:
    """A simple Person class with a name and behavior methods."""

    def __init__(self, name):
        self.name = name

    def talk(self):
        """Prints 'Hello World!'"""
        print("Hello World!")

    def walk(self):
        """Prints 'The person is walking.'"""
        print("The person is walking.")
