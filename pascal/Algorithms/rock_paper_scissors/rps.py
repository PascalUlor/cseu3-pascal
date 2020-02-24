#!/usr/bin/python
"""
Write a function `rock_paper_scissors` to generate all of the possible plays that can be made in a game of "Rock Paper Scissors", given some input `n`, which represents the number of plays per round. 

For example, given n = 2, your function should output the following:

```python
[['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'], ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'], ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]
```
1. Get all possible plays for the game
2. 
"""

import sys

def rock_paper_scissors(n):
  # pass
  combination = []
  moves = ['rock', 'paper', 'scissors']
  def get_combo(turns, combo=[]):
    if turns == 0:
      combination.append(combo)
      return
    for move in moves:
      get_combo(turns - 1, combo + [move])
  get_combo(n, [])
  return combination


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')