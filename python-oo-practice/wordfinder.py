"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    ...
    def __init__(self, file):
        """Read dictionary and reports items read."""

        dict_file = open(file)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """list of words."""

        return [w.strip() for w in dict_file]

    def random(self):
        """Return random word"""

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """skip blanks and comments"""
    def parse(self, dict_file):
        return [w.strip() for w in dict_file
            if w.strip() and not w.startswith('#')]