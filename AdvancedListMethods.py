# Task 1: Given the two lists:

# submitted = ["Alice", "Bob", "Charlie", "David"]
# attended = ["Charlie", "Eve", "Alice", "Frank"]

# Find out which students both submitted their assignments and attended the class.




submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

both_list = []
for all in attended:
    if all in submitted:
        both_list.append(all)
print(both_list)




# Task 2: Check if the two lists are identical in terms of their content, regardless of order.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
submitted.sort()
attended.sort()
if submitted == attended:
    print("the list are the same")
else:
    print("the list are diffrent")



# Task 3: Using list methods, remove any student from the
# attended list who did not submit their assignment.


submitted = ["Alice", "Bob", "Charlie", "David"] 
attended = ["Charlie", "Eve", "Alice", "Frank"] # eve, frank

attended.remove("Eve")
attended.remove("Frank")
print(attended)

