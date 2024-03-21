import random

#empty list that holds 50 random bubble solution scores between 1 and 100
bubble_score = []

length = (range(50))

#for loop appending random numbers to bubble_score 
for i in length:
    i = random.randrange(1, 100)
    bubble_score.append(i)

#empty list for random prices, one for each bubble solution score
bubble_price = []

#for loop appending random prices to bubble_price 
for i in length:
    i = round(random.uniform(0, 1), 2)
    bubble_price.append(i)

#counter for while loop
counter = 0

#while loop to print corresponding solution number, score, and price
while counter < len(bubble_score):
    print(f'\nBubble solution #{counter} score: {bubble_score[counter]} '
          f'with a price of {bubble_price[counter]:.2f} cents')
    counter += 1

#to see how many bubble solutions were tested
print(f'\nBubble solutions tested: {len(bubble_score)}')

#highest score variable set to the first item in bubble_score 
highest_score = bubble_score[0]

#for loop to find the highest score
for i in bubble_score:
    if i >= highest_score:
        highest_score = i
        
print(f'\nHighest bubble solution score: {highest_score}')

#empty list to hold best bubble solution score(s)
best_bubble_solution = []

#for loop appending best bubble solution score in case there are multiple
for i in length:
    if highest_score == bubble_score[i]:
        best_bubble_solution.append(i)
        
print('\nSolutions with the highest score: ', best_bubble_solution)

cost = 100.0 #will hold cheapest price
cheapest = 0 #will hold index of cheapest bubble solution

#for loop to find the cheapest and highest scoring bubble solution
for i in range(len(best_bubble_solution)):
    index = best_bubble_solution[i]
    if cost > bubble_price[index]:
        cheapest = index
        cost = bubble_price[index]
        
print(f'\nBubble solution {cheapest} is the most cost'
      f'effective with a price of {cost:.2f}')