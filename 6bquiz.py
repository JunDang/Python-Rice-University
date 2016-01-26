#6b question 2
CARD_CENTER = (36.5, 49)
CARD_SIZE = (73, 98)
i = 12
j = 3

print[CARD_CENTER[0] + i * CARD_SIZE[0],
                    CARD_CENTER[1] + j * CARD_SIZE[1]]


#6b question 7

n = 5000
numbers = range(2,n)
results = []
while(len(numbers)>0):
      a = numbers[0]
      results.append(a)
      new_numbers = []
      for num in numbers:
          if (num%a !=0):
              new_numbers.append(num)
      numbers = new_numbers
print len(results)   

#6b question 8
slow = 1000
fast = 1
n = 0
while (slow > fast):
       slow = 1.2*slow
       fast = 1.4*fast
       n = n+1
print n 