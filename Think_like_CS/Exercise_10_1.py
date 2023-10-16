#Write a function called nested_sum that takes a list of lists of integers and adds up
#the elements from all of the nested lists. For example:

def nested_sum(lists):
    s = 0
    for x in lists:
        s += sum(x)
    print(s)
    return 0
t = [[4, 5,], [2, 4, 8],[2]]
nested_sum(t)


