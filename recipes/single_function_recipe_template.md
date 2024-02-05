# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

Someone wants an estimated readin time for a text so that they know how long it will take them to read something.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

def reading_time(book):
    parameters: book = string

    returns: hours: minutes (datetime or string)

    side-effects: none that we can see!

def reading_time(book):
    book = book.split()
    len(book) / 200 = number of minutes
    number_of_minutes/ 60 = hours
    decimal * 60 = minutes
    return hours: minutes


```python
# EXAMPLE

def extract_uppercase(mixed_words):
    """Extracts uppercase words from a string

    Parameters: (list all parameters and their types)
        mixed_words: a string containing words (e.g. "hello WORLD")

    Returns: (state the return value and its type)
        a list of strings, each one a word (e.g. ["WORLD"])

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
extract_uppercase("hello WORLD") => ["WORLD"]

Given a book and returns a datetime or string with
hours and minutes to read.

reading_time(book) => 10 hours 17 minutes 25 seconds
reading_time(book) => 10:17:25
reading_time(text_message) => 00:00:03 seconds


"""
Given two uppercase words
It returns a list with both words
"""
extract_uppercase("HELLO WORLD") => ["HELLO", "WORLD"]

"""
Given two lowercase words
It returns an empty list
"""
extract_uppercase("hello world") => []

"""
Given a lower and a mixed case word
It returns an empty list
"""
extract_uppercase("hello WoRLD") => []

"""
Given a lowercase word and an uppercase word with an exclamation mark
It returns a list with the uppercase word, no exclamation mark
"""
extract_uppercase("hello WORLD!") => ["WORLD"]

"""
Given an empty string
It returns an empty list
"""
extract_uppercase("") => []

"""
Given a None value
It throws an error
"""
extract_uppercase(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
