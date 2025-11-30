#!/usr/bin/env python3

class Dog:
    """A simple Dog class with name, breed, and behavior methods."""

    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

    def bark(self):
        """Prints 'Woof!'"""
        print("Woof!")

    def sit(self):
        """Prints 'The dog is sitting.'"""
        print("The dog is sitting.")
