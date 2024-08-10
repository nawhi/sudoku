# Sudoku Solver Playground

A framework for playing around with all the many ways you can implement a Sudoku solver, without having to write too
much parsing boilerplate. In particular I was interested in writing solution strategies the way a human might do it,
to see how that compared in performance to algorithmic approaches. Inspired
by [this Wikipedia page](https://en.wikipedia.org/wiki/Sudoku_solving_algorithms),
and [Rob](https://github.com/robertsteane) (who you should hire).

Note that this repo is not intended to be production quality code or to have a perfect API / data model for managing the Sudoku board.
A numpy ndarray was good enough for what I wanted.

## How to add a new strategy

- Create a Python file in `core/strategies`
- If you want to unit test, create a test file in `test/strategies` (look at the other tests for examples)
- For debugging you can use the methods in `core/printer.py`
- To test a full sudoku in combination with all strategies, use `core/solver.py` and its test

