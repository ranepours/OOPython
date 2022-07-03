#serial number generator
class SerialGenerator:
    def __init__(self, start=0):
        self.start = self.next = start

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        self.next += 1
        return self.next - 1

    def reset(self):
        self.next = self.start

