# Insertion Sort Algorithm
# Best Case: O(n) when array is already sorted
# Worst Case: O(n^2) when array is sorted in reverse order

elements = map(int, raw_input('Enter your array elements: ').split())

for i in range(1, len(elements)):
    j = i
    key = elements[i]
    while j > 0 and elements[j-1] > key:
        elements[j] = elements[j-1]
        j = j-1
    elements[j] = key

print "Sorted array elements: ", elements