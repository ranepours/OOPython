class SerialGenerator:
    """serial number generator - create unique incrementing serials"""
    def __init__(self, start=0):
        self.start = self.next = start

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        self.next += 1
        return self.next - 1

    def reset(self):
        self.next = self.start

import random
class WordFinder:
    """find random words from dictionary"""
    def __init__(self, path):
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")
    def parse(self, dict_file):
        return [w.strip() for w in dict_file]
    def random(self):
        return random.choice(self.words)

class SpecialwordFinder(WordFinder):
    """finds random but excludes blank lines and comments"""
    def parse(self, dict_file):
        return [w.strip() for w in dict_file if w.strip() and not w.startswith('#')]
