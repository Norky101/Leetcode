def reverse(lst):
  pointer = len(lst)-1
  reversed_lst = []
  for i in range(len(lst)):
    reversed_lst.append(lst[pointer])
    pointer -= 1
  return reversed_lst

list = [9,8,7,6,5,4,3,2,1]
print(reverse(list))