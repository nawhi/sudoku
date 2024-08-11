# Sudoku Solver Playground

A framework for playing around with all the many ways you can implement a Sudoku solver, without having to write too
much parsing boilerplate. In particular I was interested in writing solution strategies the way a human might do it,
to see how that compared in performance to algorithmic approaches. Inspired
by [this Wikipedia page](https://en.wikipedia.org/wiki/Sudoku_solving_algorithms),
and [Rob](https://github.com/robertsteane) (who you should hire).

Note that this repo is not intended to be production quality code or to have a perfect API / data model for managing the Sudoku board.
A numpy ndarray was good enough for what I wanted.

## Installation

The project uses Python 3.11.6. This might be `python` or `python3` on your machine depending on your setup. These instructions are for Unix-like systems.

Clone the repo and install the requirements:

```bash
git clone https://github.com/nawhi/sudoku
cd sudoku

# Create a virtual environment and activate it
python3 -m venv .venv  
source .venv/bin/activate

# Install the requirements in the venv
pip install -r requirements.txt
```

## How to add a new strategy

- Create a Python file in `core/strategies`
- If you want to unit test, create a test file in `test/strategies` (look at the other tests for examples). Note the tests are heavily designed to work in PyCharm or another IDE where assertEqual results can be viewed in the native diff viewer. Their output may not be as useful in the console. 
- For debugging you can use the methods in `core/printer.py`
- To test a full sudoku in combination with all strategies, use `core/solver.py` and its test

