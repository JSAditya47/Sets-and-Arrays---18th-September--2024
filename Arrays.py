import array as arr 

array_num = arr.array('i', [1, 3, 5, 3, 7, 9, 3, 3, 3, 3, 5])

print("Original Array:" + str(array_num))

print("Number of Occurences of the Number 3 in the Said Array:"+str(array_num.count(3)))

array_num.reverse()
print("Reverse the Order of the Items: ")
print(str(array_num))