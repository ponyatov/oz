
import os, sys

class Object:

    def __init__(self, V):
        self.type = self.__class__.__name__.lower()
        self.val  = V
        self.slot = {}
        self.nest = []
        self.sid  = id(self)


print(Object('Hello'))
