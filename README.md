# Python Number Games and Utilities

This repository contains two simple Python scripts:

- `guess_numberss.py` — a number guessing game.
- `sort_numbers.py` — reads numbers from a text file, sorts them, and writes the results to a new file.

## Requirements

- Python 3 installed
- A terminal such as Ubuntu Terminal, PowerShell, or Command Prompt

Check your Python version with:

```bash
python3 --version
```

## Files

- `guess_numberss.py`
- `sort_numbers.py`
- `numbers.txt` (used for testing `sort_numbers.py`)
- `processed_numbers.txt` (created after running `sort_numbers.py`)

## How to Run

### Run the guessing game

```bash
python3 guess_numberss.py
```

This script starts a number guessing game in the terminal.

### Run the sorting script

```bash
python3 sort_numbers.py
```

This script looks for `.txt` files in the current directory, reads numeric values from them, ignores non-numeric lines, sorts the numbers, and writes the sorted values and total sum to a new processed file.

## Testing `sort_numbers.py`

Create a file named `numbers.txt` in the same directory as `sort_numbers.py`.

Example `numbers.txt`:

```text
10
4
7.5
2
apple
12
```

Then run:

```bash
python3 sort_numbers.py
```

Expected behavior:

- The script reads `numbers.txt`
- Ignores non-numeric lines such as `apple`
- Sorts the numeric values
- Creates a file named `processed_numbers.txt`

## Example output file

After running `sort_numbers.py`, the generated `processed_numbers.txt` file should look similar to this:

```text
Sorted Numbers:
2.0
4.0
7.5
10.0
12.0
Sum of Numbers:
35.5
```

## Notes

- Make sure you run the scripts from the directory where the files are located.
