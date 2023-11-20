# objects of this class are iterators
class Powtwo:
    def __init__(self, max):
      self.max = max

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        result = 3 ** self.num
        self.num += 1
        return result
    def licount(self):
        print("count is x")


pow_two = Powtwo(5)
pow_two_iter = iter(pow_two)
print(list(pow_two_iter))
pow_two.licount()


sen = "Welcome to the python session"
print(sen.split())
sen.count("s")
