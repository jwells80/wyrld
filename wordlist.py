import pathlib
import sys

from string import asciii_letters

in_path = pathlib.PATH(sys.argv[1])
out_path = pathlib.PATH(sys.argv[2])

words = sorted(
    {
        word.lower()
        for word in in_path.read_text(encoding="utf-8").split()
        if all(letter in ascii_letters for letter in word)
    },
    key=lambda word: (len(word), word),
)
out_path.write_text("\n".join(words))
