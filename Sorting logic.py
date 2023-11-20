# Nested list of student's info in a science olympiad
# List elements: (Student's Name, Marks out of 100, Age)
participant_list = [('Alison', 50, 18),('Terence',  75, 24),('David', 62, 15),('jimmy', 59, 23),('john', 95, 26)]
def sorter(item):
      # Since highest marks first, least error = most marks
      error = 100 - item[1]
      age = item[2]
      return (error, age)
sorted_list = sorted(participant_list, key=sorter)
print(sorted_list)
