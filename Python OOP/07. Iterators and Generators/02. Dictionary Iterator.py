class dictionary_iter:
    def __init__(self, data):
        self.data = list(data.items())
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.data):
            raise StopIteration
        result = self.data[self.idx]
        self.idx += 1
        return result
