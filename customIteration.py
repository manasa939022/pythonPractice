class Run:


  # Creating an iterator object
  def __iter__(self):
      self.value = 1
      return self

  # Move to next element using __next__
  def __next__(self):
      # Storing the current old value
      value = self.value
    # double & return old value
      self.value = value * 2
      return value




# Outputs the numbers till value reaches highest = 50
r = Run()
double = iter(r)
for element in double:

    if element>50:
        break
    print(element)


