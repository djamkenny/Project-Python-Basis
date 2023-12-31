Exercise 10.1. Write a function called nested_sum that takes a list of lists of integers and adds up
the elements from all of the nested lists. For example:
>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
21
Exercise 10.2. Write a function called cumsum that takes a list of numbers and returns the cumu-
lative sum; that is, a new list where the ith element is the sum of the first i + 1 elements from the
original list. For example:
>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]
Exercise 10.3. Write a function called middle that takes a list and returns a new list that contains
all but the first and last elements. For example:
>>> t = [1, 2, 3, 4]
>>> middle(t)
[2, 3]10.15. Exercises
101
Exercise 10.4. Write a function called chop that takes a list, modifies it by removing the first and
last elements, and returns None. For example:
>>> t = [1, 2, 3, 4]
>>> chop(t)
>>> t
[2, 3]
Exercise 10.5. Write a function called is_sorted that takes a list as a parameter and returns True
if the list is sorted in ascending order and False otherwise. For example:
>>> is_sorted([1, 2, 2])
True
>>> is_sorted(['b', 'a'])
False
Exercise 10.6. Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns True if they are anagrams.
Exercise 10.7. Write a function called has_duplicates that takes a list and returns True if there
is any element that appears more than once. It should not modify the original list.
Exercise 10.8. This exercise pertains to the so-called Birthday Paradox, which you can read about
at http: // en. wikipedia. org/ wiki/ Birthday_ paradox .
If there are 23 students in your class, what are the chances that two of you have the same birthday?
You can estimate this probability by generating random samples of 23 birthdays and checking for
matches. Hint: you can generate random birthdays with the randint function in the random
module.
You can download my solution from http: // thinkpython2. com/ code/ birthday. py .
Exercise 10.9. Write a function that reads the file words.txt and builds a list with one element
per word. Write two versions of this function, one using the append method and the other using
the idiom t = t + [x]. Which one takes longer to run? Why?
Solution: http: // thinkpython2. com/ code/ wordlist. py .
Exercise 10.10. To check whether a word is in the word list, you could use the in operator, but it
would be slow because it searches through the words in order.
Because the words are in alphabetical order, we can speed things up with a bisection search (also
known as binary search), which is similar to what you do when you look a word up in the dictionary.
You start in the middle and check to see whether the word you are looking for comes before the word
in the middle of the list. If so, you search the first half of the list the same way. Otherwise you search
the second half.
Either way, you cut the remaining search space in half. If the word list has 113,809 words, it will
take about 17 steps to find the word or conclude that it’s not there.
Write a function called in_bisect that takes a sorted list and a target value and returns True if
the word is in the list and False if it’s not.
Or you could read the documentation of the bisect module and use that! Solution: http: //
thinkpython2. com/ code/ inlist. py .
Exercise 10.11. Two words are a “reverse pair” if each is the reverse of the other. Write a program
that finds all the reverse pairs in the word list. Solution: http: // thinkpython2. com/ code/
reverse_ pair. py .
Exercise 10.12. Two words “interlock” if taking alternating letters from each forms a new
word. For example, “shoe” and “cold” interlock to form “schooled”. Solution: http: //102
Chapter 10. Lists
thinkpython2. com/ code/ interlock. py . Credit: This exercise is inspired by an example at
http: // puzzlers. org .
1. Write a program that finds all pairs of words that interlock. Hint: don’t enumerate all pairs!
2. Can you find any words that are three-way interlocked; that is, every third letter forms a
word, starting from the first, second or third?
