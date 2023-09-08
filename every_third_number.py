
'''def every_three_nums(start):
    empty_list = []
    if i< 100:
      for i in range(start, 101, 3):
        #print(i)
        empty_list.append(i)
    print(empty_list)

print(every_three_nums(91))'''

def every_three_nums(start):
  return list(range(start, 101, 3))

every_three_nums(100)