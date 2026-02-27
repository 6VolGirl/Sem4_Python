class Symbols:
    def __init__(self, text, n, m):
        self.text = text
        self.n = n
        self.m = m
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # Конец ли строки
        if self.index + self.n > len(self.text):
            raise StopIteration

        part = self.text[self.index : self.index + self.n]

        self.index += self.m
        return part




a = Symbols ("hello , my darling ", n =5 , m =4)
for x in a :
    print ( x )
