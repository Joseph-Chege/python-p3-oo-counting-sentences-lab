#!/usr/bin/env python3

class MyString:
  """MyString in count_sentences.py"""
  def __init__(self, value=""):
    self.value = value

  def is_sentence(self):
    """returns True if value ends with a period and False otherwise."""
    return self.value[-1] == "."
  
  def is_question(self):
    """returns True if value ends with a question mark and False otherwise."""
    return self.value[-1] == "?"
  
  def is_exclamation(self):
    """returns True if value ends with an exclamation mark and False otherwise."""
    return self.value[-1] == "!"
  
  def count_sentences(self):
    """returns the number of sentences in value."""
    return self.value.count(".") + self.value.count("?") + self.value.count("!")

  pass
