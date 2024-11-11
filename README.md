# Breakout Game Collab

### Prerequisites:

- Python (3 or higher)

  - Mac: Python should be pre-installed. If not, you can install it via Homebrew or Python's website.
  - Windows: Download and install Python from the official Python website.
  - Ubuntu: Python is typically pre-installed. If not, install it using sudo apt install python3.

- pip (Python package installer)

## Directions for Local Development

1. Ensure prerequisites are installed

```
pip --version
python --version
```

2. Install requirements.txt

```
pip install -r requirements.txt
```

Debian users: `sudo pip3 install -r requirements.txt --break-system-packages` to skip PEP 668 no globals restriction (use sparingly)

3. Execute the script:

Navigate to `/src` then run:

```
python main.py
```

4. Run unit tests:


All tests in `/tests` directory:

```
python -m unittest discover -s tests
```

Or one test at a time:

```
python -m unittest tests.test_game
```

Running firsttrybreakout1:

- Nav to `/firsttrybreakout` 
- then run: `python -m firsttrybreakout1.py` 
- for tests run ` python -m unittest test_breakout.py`

### Troubleshooting:
Ensure that the `/src` directory is on the Python import path. This can be done by modifying the PYTHONPATH or by modifying the system path within your test file.
```

export PYTHONPATH=$PYTHONPATH:/path/to/project-root/src

```

## Directions to Play