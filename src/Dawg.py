'''
Created on Jun 27, 2012

@author: JS018234
'''

from DawgNode import *

class Dawg:
  def __init__(self):
    self.previousWord = ""
    self.root = DawgNode()

    # Here is a list of nodes that have not been checked for duplication.
    self.uncheckedNodes = []

    # Here is a list of unique nodes that have been checked for
    # duplication.
    self.minimizedNodes = {}

  def insert(self, word):
    if word < self.previousWord:
      raise Exception("Error: Words must be inserted in alphabetical " + "order.")

    # find common prefix between word and previous word
    commonPrefix = 0
    for i in range(min(len(word), len(self.previousWord))):
      if word[i] != self.previousWord[i]: break
      commonPrefix += 1

    # Check the uncheckedNodes for redundant nodes, proceeding from last
    # one down to the common prefix size. Then truncate the list at that
    # point.
    self._minimize(commonPrefix)

    # add the suffix, starting from the correct node mid-way through the
    # graph
    if len(self.uncheckedNodes) == 0:
      node = self.root
    else:
      node = self.uncheckedNodes[-1][2]

    for letter in word[commonPrefix:]:
      nextNode = DawgNode()
      node.edges[letter] = nextNode
      self.uncheckedNodes.append((node, letter, nextNode))
      node = nextNode

    node.final = True
    self.previousWord = word

  def finish(self):
    # minimize all uncheckedNodes
    self._minimize(0);

  def _minimize(self, downTo):
    # proceed from the leaf up to a certain point
    for i in range(len(self.uncheckedNodes) - 1, downTo - 1, -1):
      (parent, letter, child) = self.uncheckedNodes[i];
      if child in self.minimizedNodes:
        # replace the child with the previously encountered one
        parent.edges[letter] = self.minimizedNodes[child]
      else:
        # add the state to the minimized nodes.
        self.minimizedNodes[child] = child;
      self.uncheckedNodes.pop()

  def lookup(self, word):
    node = self.root
    for letter in word:
      if letter not in node.edges: return False
      node = node.edges[letter]
    return node.final

  def nodeCount(self):
      return len(self.minimizedNodes)

  def edgeCount(self):
      count = 0
      for node in self.minimizedNodes:
          count += len(node.edges)
      return count

  def getNode(self, word):
    node = self.root
    for letter in word:
      if letter not in node.edges: return None
      node = node.edges[letter]
    return node