
# Hex

A hexdump command line utility implemented in Python.

Output:

    $ hex < hex.py -n 128
    ────────────────────────────────────────────────────────────────────────────────
         0 │ 23 21 2F 75  73 72 2F 62  69 6E 2F 65  6E 76 20 70 │ #!/usr/bin/env p
        10 │ 79 74 68 6F  6E 33 0A 23  20 2D 2D 2D  2D 2D 2D 2D │ ython3·# -------
        20 │ 2D 2D 2D 2D  2D 2D 2D 2D  2D 2D 2D 2D  2D 2D 2D 2D │ ----------------
        30 │ 2D 2D 2D 2D  2D 2D 2D 2D  2D 2D 2D 2D  2D 2D 2D 2D │ ----------------
        40 │ 2D 2D 2D 2D  2D 2D 2D 2D  2D 2D 2D 2D  2D 2D 2D 2D │ ----------------
        50 │ 2D 2D 2D 2D  2D 2D 2D 2D  2D 2D 2D 2D  2D 2D 2D 2D │ ----------------
        60 │ 2D 2D 2D 0A  23 20 48 65  78 64 75 6D  70 20 63 6F │ ---·# Hexdump co
        70 │ 6D 6D 61 6E  64 20 6C 69  6E 65 20 75  74 69 6C 69 │ mmand line utili
    ────────────────────────────────────────────────────────────────────────────────

Interface:

    $ hex --help

    Usage: hex [FLAGS] [OPTIONS] [ARGUMENTS]

      Hexdump utility.

    Arguments:
      [file]                File to dump. Defaults to reading from stdin.

    Options:
      -l, --line <int>      Bytes per line in output (defaults to 16).
      -n, --number <int>    Number of bytes to read.
      -o, --offset <int>    Byte offset at which to begin reading.

    Flags:
          --help            Display this help text and exit.
          --version         Display version number and exit.

Install from the Python package index using `pip`:

    $ pip install hex

This application requires Python 3.
