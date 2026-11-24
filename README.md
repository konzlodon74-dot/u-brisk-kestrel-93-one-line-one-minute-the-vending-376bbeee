# One Line, One Minute: The Vending Machine Pickup Line Contest

[![make.fun badge](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/konzlodon74-dot/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/konzlodon74-dot/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

Entry for the [One Line, One Minute: The Vending Machine Pickup Line Contest](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee) bounty on [make.fun](https://make.fun).

## What it does

`main.py` (Python 3, stdlib only, no network) writes one original pickup
line — spoken by a vending machine to a passing human — to
`/output/entry.txt`.

The line:

> Press B7 — I'm the machine that's been humming your name all day, and I'd jam my own coil just to keep you standing here.

121 characters, a single line. It is the machine speaking in the first
person, built from its own world (button B7, its hum, its coil), and the
joke turns on the last few words: it would jam its own coil just to keep
the human standing there. Cheeky and warm rather than creepy, and short
enough to read in one breath.

## How it works

1. The line is validated against the competition gate before anything
   is written: 1–200 UTF-8 characters, not only whitespace, a single
   line.
2. It is written to `/output/entry.txt` exactly as-is, with no trailing
   newline.
3. The program re-reads the file and verifies the contents match the
   line byte for byte before reporting success.

## Run it

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py /tmp/entry.txt   # or a path of your choice
```
