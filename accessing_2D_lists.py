"#Your code below:
incoming_class = [['Kenny', 'American',9], ['Tanya','Ukrainian',9], ['Madison', 'Indian',7]]
print(incoming_class)

#change Madison's class for 8, use positive indices and bracket notation
incoming_class [2][2] = 8
print('After first change')
print (incoming_class)

#change Kenny into Ken, use negaative indices and bracket notation
incoming_class [-3][-3] = 'Ken'
print('After second change')
print (incoming_class)

#Output:
'''[['Kenny', 'American', 9], ['Tanya', 'Ukrainian', 9], ['Madison', 'Indian', 7]]
After first change
[['Kenny', 'American', 9], ['Tanya', 'Ukrainian', 9], ['Madison', 'Indian', 8]]
After second change
[['Ken', 'American', 9], ['Tanya', 'Ukrainian', 9], ['Madison', 'Indian', 8]]'''
"