Question 1
Which of the following is valid notation for a set in CodeSkulptor?

Your Answer		Score	Explanation
set([])		4.00	
{1,2,3}		2.00	
While valid in Python 2.7 or 3.0, it is not valid in Python 2.6 or CodeSkulptor.

set()		4.00	
Total		10.00 / 10.00	
Question 2
Which of the following operations can mutate set s? You may want to try some examples in CodeSkulptor and refer to the documentation.

Your Answer		Score	Explanation
t.intersection(s)		1.00	
s.union(t)		1.00	
s.discard(x)		1.00	
s.difference_update(t)		5.00	
s = t		1.00	
This assigns to s, but doesn't mutate s. You should review the difference.

t.symmetric_difference_update(s)		1.00	
Total		10.00 / 10.00	
Question 3
Which of the following give the same result as s.union(t)?

Refer to the CodeSkulptor documentation or try them on examples.

Your Answer		Score	Explanation
t.union(s)		4.00	
s.union(s.difference(t))		1.00	
s.union(t.difference(s))		4.00	
s.intersection(s.union(t))		1.00	
Total		10.00 / 10.00	
Question 4
A set is an unordered collection of distinct elements. Which of the following problem contexts represent instances of this idea?

Your Answer		Score	Explanation
Names for everyone taking this course		1.00	
No, we could easily have multiple students with the same name.

Phonebook		1.00	
While you could have a set of pairs, each with a name and phone number, there wouldn't be an easy way to look up a person's phone number.

Group of distinct cities		8.00	
Total		10.00 / 10.00	
Question 5
How many frames per second are typically projected in modern movies? How many times per second is the draw handler typically called in CodeSkulptor?

Enter two numbers representing these frame rates in frames per second. Use only spaces to separate the numbers.

Answer for Question 5
You entered:

Your Answer		Score	Explanation
24		5.00	
60		5.00	
Total		10.00 / 10.00	
Question 6
In this week, the videos and provided example code define a Sprite class. What attribute (also known as a field) can be used to help index the sub-images forming an animated sprite?

Your Answer		Score	Explanation
age		10.00	
Total		10.00 / 10.00	
Question 7
Which of the following browsers support MP3 audio files? Refer to the CodeSkulptor documentation.

Your Answer		Score	Explanation
Safari		4.00	
Chrome		4.00	
Firefox		2.00	Firefox currently doesn't support MP3 since they are a proprietary format.
Total		10.00 / 10.00	
Question 8
Consider a horizontally-tiled image where each sub-imaged has the same size. If each sub-image is of size 60 x 90 (in pixels), what is the horizontal distance (in pixels) between the centers of adjacent sub-images?

Your Answer		Score	Explanation
60		10.00	
Total		10.00 / 10.00	
Question 9
How many distinct numbers are printed by the following code? Enter the count.

def next(x):
    return (x ** 2 + 79) % 997

x = 1
for i in range(1000):
    print x
    x = next(x)
Hint: Consider how editing the code to use a set could help solve the question.

Answer for Question 9
You entered:

Your Answer		Score	Explanation
46		20.00	
Total		20.00 / 20.00	




def next(x):
    return (x ** 2 + 79) % 997
mset = set([])
x = 1
mset.add(x)
for i in range(1000):
   
    x = next(x)
    mset.add(x)
    
    

print len(mset)