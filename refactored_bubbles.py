import random

#counter for while loop
counter = 0

#will hold cheapest price
cost = 100.0

#will hold index of cheapest bubble solution
cheapest = 0

#empty list that holds 50 random bubble solution scores between 1 and 100
bubble_score = []

#empty list for random prices, one for each bubble solution score
bubble_price = []

#empty list to hold best bubble solution score(s)
best_bubble_solution = []

#sorting algorithm
def bubble_sort(sorted_list, solution_number):
    swapped = True #set to true to start first pass
    
    while swapped:
        swapped = False
        for i in range(0, (len(bubble_score) - 1)): 
            if bubble_score[i] < bubble_score[i + 1]: #if greater, swap items
                temp = bubble_score[i] 
                bubble_score[i] = bubble_score[i + 1] #swapping 
                bubble_score[i + 1] = temp
                temp = solution_number[i]
                solution_number[i] = solution_number[i + 1]
                solution_number[i + 1] = temp
                swapped = True #if items are swapped, another pass is intitiated

#for loop appending 50 random numbers between 1 and 100 to bubble_score
for i in range(50):
    i = random.randrange(1, 101)
    bubble_score.append(i)

#for loop appending random prices to bubble_price 
for i in range(50):
    i = round(random.uniform(0, 1), 2)
    bubble_price.append(i)
    
#highest score variable set to the first item in bubble_score 
highest_score = bubble_score[0]

#for loop to find the highest score
for i in bubble_score:
    if i >= highest_score:
        highest_score = i
        
#for loop appending best bubble solution score in case there are multiple
for i in range(len(bubble_score)):
    if highest_score == bubble_score[i]:
        best_bubble_solution.append(i)

#for loop to find the cheapest and highest scoring bubble solution
for i in range(len(best_bubble_solution)):
    index = best_bubble_solution[i]
    if cost > bubble_price[index]:
        cheapest = index
        cost = bubble_price[index]
        
#while loop to print corresponding solution number, score, and price
while counter < len(bubble_score):
    print(f'\nBubble solution #{counter} score: {bubble_score[counter]} '
          f'with a price of {bubble_price[counter]:.2f} cents')
    counter += 1
    
#will hold length of bubble_score
score_number = len(bubble_score)

#will hold the solution number for every corresponding bubble score
solution_score_number = list(range(score_number))

bubble_sort(bubble_score, solution_score_number)
         
print(f'\nBubble solutions tested: {len(bubble_score)}')

print(f'\nHighest bubble solution score: {highest_score}')

print('\nSolutions with the highest score: ', best_bubble_solution)
        
print(f'\nBubble solution {cheapest} is the most cost '
      f'effective with a price of {cost:.2f}')

print('\nTop 5 Bubble Solutions')
for i in range(5):
    print(f'\n{i + 1}) Bubble Solution #{solution_score_number[i]} '
          f'| Score: {bubble_score[i]}') 