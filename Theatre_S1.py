import pandas as pd
import numpy as np
import random as rd

locations = ['A', 'B', 'C']

base_score = {
    'A': 30,
    'B': 40,
    'C': 50
}

score_multiplier = {
    'Win': 2,
    'Tie': 1,
    'Lose': 0.5
}

#21 days
#96 at day 12
drones_available = [1, 15, 24, 39, 54, 66, 72, 78, 87, 93, 93, 96, 96, 96, 96, 96, 96, 96, 96, 96, 96]

#placement 1 for winner, placement 3 for loser
#placement_A = [3, 1, 1, 1, 1, 3, 1, 1, 2, 3, 1, 1, 2, 2, 1, 1, 2, 1, 1, 1]
#placement_B = [1, 2, 2, 3, 2, 1, 2, 3, 1, 1, 3, 3, 1, 1, 3, 2, 3, 2, 2, 3]
#placement_C = [2, 3, 3, 2, 3, 2, 3, 2, 3, 2, 2, 2, 3, 3, 2, 3, 1, 3, 3, 2]

#votes, percentage of 100
#votes_A = [40.03, 21.08, 19.12, 30.37, 24.46, 41.44, 24.66, 28.10, 33.31, 35.79, 27.10, 26.55, 33.69, 32.48, 32.15, 28.18, 34.05, 29.51, 31.85, 31.08]
#votes_B = [25.20, 25.12, 35.60, 34.97, 32.05, 25.64, 35.50, 39.52, 29.74, 28.57, 36.61, 37.30, 29.95, 32.32, 34.55, 35.04, 35.58, 34.33, 32.18, 37.46]
#votes_C = [34.77, 53.80, 45.28, 34,66, 43.48, 32.92, 39.84, 32.38, 36.95, 35.64, 36.28, 36.15, 36.36, 35.20, 33.30, 36.79, 30.37, 36.16, 35.97, 31.47]

#note that data for day 21 is fudged. It was reported that the result was B > A > C but not the exact percentages.
votes = {
    'A': [40.03, 21.08, 19.12, 30.37, 24.46, 41.44, 24.66, 28.10, 33.31, 35.79, 27.10, 26.55, 33.69, 32.48, 32.15, 28.18, 34.05, 29.51, 31.85, 31.08, 32.48],
    'B': [25.20, 25.12, 35.60, 34.97, 32.05, 25.64, 35.50, 39.52, 29.74, 28.57, 36.61, 37.30, 29.95, 32.32, 34.55, 35.04, 35.58, 34.33, 32.18, 37.46, 32.32],
    'C': [34.77, 53.80, 45.28, 34.66, 43.48, 32.92, 39.84, 32.38, 36.95, 35.64, 36.28, 36.15, 36.36, 35.20, 33.30, 36.79, 30.37, 36.16, 35.97, 31.47, 35.20]
}

def daily_calc(location, place):
    daily = base_score[location] * score_multiplier[place] * drones_available[day]
    return daily

def outcome(choice):
    global total
    if choice == winning_loc:
        daily = daily_calc(choice,'Win')
        total = total + daily
        print(choice + ' WIN  - ' + ' Points: ' + str(daily) + ' Total: ' + str(total))
    elif choice == losing_loc:
        daily = daily_calc(choice,'Lose')
        total = total + daily
        print(choice + ' LOSE - ' + ' Points: ' + str(daily) + ' Total: ' + str(total))
    else:
        daily = daily_calc(choice, 'Tie')
        total = total + daily
        print(choice + ' Tie  - ' + ' Points: ' + str(daily) + ' Total: ' + str(total))
		
vote_table = pd.DataFrame(votes)
t_vote_table = vote_table.transpose()

print('Daily Ranking')
for day in t_vote_table:
    winning_loc = t_vote_table[day].idxmin()
    losing_loc = t_vote_table[day].idxmax()
    tie_loc = [loc for loc in locations if winning_loc != loc and losing_loc != loc]
    print('Winner: ' + winning_loc + ', Tie: ' + tie_loc[0] + ', Loser: ' + losing_loc)
	
print('ALL WINS')
total = 0
for day in t_vote_table:
    winning_loc = t_vote_table[day].idxmin()
    daily = base_score[winning_loc] * score_multiplier['Win'] * drones_available[day]
    total = total + daily
    print('Winner: ' + winning_loc + ' Points: ' + str(daily) + ' Total: ' + str(total))

print('ALL LOSSES')
total = 0
for day in t_vote_table:
    losing_loc = t_vote_table[day].idxmax()
    daily = base_score[losing_loc] * score_multiplier['Lose'] * drones_available[day]
    total = total + daily
    print('Loser: ' + losing_loc + ' Points: ' + str(daily) + ' Total: ' + str(total))

print('ALL TIES')
total = 0
for day in t_vote_table:
    winning_loc = t_vote_table[day].idxmin()
    losing_loc = t_vote_table[day].idxmax()
    tie_loc = [loc for loc in locations if winning_loc != loc and losing_loc != loc]
    daily = daily_calc(tie_loc[0],'Tie')
    total = total + daily
    print('Tie: ' + tie_loc[0] + ' Points: ' + str(daily) + ' Total: ' + str(total))

print('C ONLY')
total = 0
for day in t_vote_table:
    winning_loc = t_vote_table[day].idxmin()
    losing_loc = t_vote_table[day].idxmax()
    tie_loc = [loc for loc in locations if winning_loc != loc and losing_loc != loc]
    
    if 'C' == winning_loc:
        daily = daily_calc('C','Win')
        total = total + daily
        print('C ' + 'WIN  - ' + ' Points: ' + str(daily) + ' Total: ' + str(total))
    elif 'C' == losing_loc:
        daily = daily_calc('C','Lose')
        total = total + daily
        print('C ' + 'LOSE - ' + ' Points: ' + str(daily) + ' Total: ' + str(total))
    else:
        daily = daily_calc('C', 'Tie')
        total = total + daily
        print('C ' + 'TIE  - ' + ' Points: ' + str(daily) + ' Total: ' + str(total))

print('B ONLY')
total = 0
choice = 'B'
for day in t_vote_table:
    winning_loc = t_vote_table[day].idxmin()
    losing_loc = t_vote_table[day].idxmax()
    tie_loc = [loc for loc in locations if winning_loc != loc and losing_loc != loc]
    
    if choice == winning_loc:
        daily = daily_calc(choice,'Win')
        total = total + daily
        print(choice + ' WIN - ' + ' Points: ' + str(daily) + ' Total: ' + str(total))
    elif choice == losing_loc:
        daily = daily_calc(choice,'Lose')
        total = total + daily
        print(choice + ' LOSE - ' + ' Points: ' + str(daily) + ' Total: ' + str(total))
    else:
        daily = daily_calc(choice, 'Tie')
        total = total + daily
        print(choice + ' Tie - ' + ' Points: ' + str(daily) + ' Total: ' + str(total))
		
print('A ONLY')
total = 0
choice = 'A'
for day in t_vote_table:
    winning_loc = t_vote_table[day].idxmin()
    losing_loc = t_vote_table[day].idxmax()
    tie_loc = [loc for loc in locations if winning_loc != loc and losing_loc != loc]
    outcome(choice)
	
print('PICK PREVIOUS WINNER')
total = 0
choice = 'B'
for day in t_vote_table:
    winning_loc = t_vote_table[day].idxmin()
    losing_loc = t_vote_table[day].idxmax()
    tie_loc = [loc for loc in locations if winning_loc != loc and losing_loc != loc]
    outcome(choice)
    choice = winning_loc
	
print('PICK PREVIOUS LOSER')
total = 0
choice = 'B'
for day in t_vote_table:
    winning_loc = t_vote_table[day].idxmin()
    losing_loc = t_vote_table[day].idxmax()
    tie_loc = [loc for loc in locations if winning_loc != loc and losing_loc != loc]
    outcome(choice)
    choice = losing_loc
	
print('PICK PREVIOUS TIE')
total = 0
choice = 'B'
for day in t_vote_table:
    winning_loc = t_vote_table[day].idxmin()
    losing_loc = t_vote_table[day].idxmax()
    tie_loc = [loc for loc in locations if winning_loc != loc and losing_loc != loc]
    outcome(choice)
    choice = tie_loc[0]
	
print('KEEP PREVIOUS CHOICE UNTIL LOSS, THEN NEW WINNER')
total = 0
choice = 'B'
for day in t_vote_table:
    winning_loc = t_vote_table[day].idxmin()
    losing_loc = t_vote_table[day].idxmax()
    tie_loc = [loc for loc in locations if winning_loc != loc and losing_loc != loc]
    outcome(choice)
    if choice == losing_loc:
        choice = winning_loc

print('KEEP PREVIOUS CHOICE UNTIL WIN, THEN NEW LOSER')
total = 0
choice = 'B'
for day in t_vote_table:
    winning_loc = t_vote_table[day].idxmin()
    losing_loc = t_vote_table[day].idxmax()
    tie_loc = [loc for loc in locations if winning_loc != loc and losing_loc != loc]
    outcome(choice)
    if choice == winning_loc:
        choice = losing_loc

print('SPIN THE WHEEL')
total = 0  
for day in t_vote_table:
    
    rd.seed()
    rng = rd.random()

    if rng >= 0.6666:
        choice = 'A'
    elif rng >= 0.3333 and rng <=0.6666:
        choice = 'B'
    else: choice = 'C'
    
    winning_loc = t_vote_table[day].idxmin()
    losing_loc = t_vote_table[day].idxmax()
    tie_loc = [loc for loc in locations if winning_loc != loc and losing_loc != loc]
    outcome(choice)
	
'''Spin the wheel a lot. Don't run this without removing print line from outcome()
random_results=[]

for i in range(1000):
    total = 0
    for day in t_vote_table:
    
        rd.seed()
        rng = rd.random()

        if rng >= 0.6666:
            choice = 'A'
        elif rng >= 0.3333 and rng <=0.6666:
            choice = 'B'
        else: choice = 'C'
    
        winning_loc = t_vote_table[day].idxmin()
        losing_loc = t_vote_table[day].idxmax()
        tie_loc = [loc for loc in locations if winning_loc != loc and losing_loc != loc]
        outcome(choice)
    
    random_results.append(total)
	
df = pd.DataFrame(random_results)
df.to_csv("spin the wheel.csv", index=False, header=False)'''