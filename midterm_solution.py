roster = [
    [1, 'Layla', 'Marksman'],
    [2, 'Tigreal', 'tank'],
    [3, 'Gusion', 'Assassin'],
    [4, 'Kagura', 'Mage'],
    [5, 'Chou', 'Fighter'],
]

roster = [
    [1, 'Layla', 'Marksman'],
    [2, 'Tigreal', 'tank'],
    [3, 'Gusion', 'Assassin'],
    [4, 'Kagura', 'Mage'],
    [5, 'Chou', 'Fighter'],
]
ranks = ["epic", "legend", "mythic"]
# let's take the user's info
ign = input("Enter your in-game IGN: ")
rank = None
while True:
    rank_input = input("Enter our current rank based on the given criteria (Epic / Legend / Mythic): ").strip().lower()
    if rank_input in ranks:
        rank = rank_input.title()
        break
    else:
        print("Invalid input. Please enter a valid rank (Epic, Legend, Mythic).")
        continue


# print the current roster
print("="*20)
print(f"{'MOBILE LEDENDS -- HERO ROSTER':^20}")
print("="*20)
for i in range(len(roster)):
    print(f"{roster[i][0]}. {roster[i][1]} - {roster[i][2]}")
print("="*20)

# we will store the KDA as nested list, instead of storing it per variables.
KDAList = [] # the format KDA is [number, selected hero, KDA, match status, performance status]
for i in range(4):
    print(f"Match {i+1}")
    selected_hero = None # we'll leave this as blank as we will use this for reference per match
    valid = True
    temp_hero = None # we have to hold temporarily the data from the while loop

    # we'll let the user to select their character before starting the match
    while True:
        hero = int(input(f"Enter the hero number (0 to skip): "))
        if hero > len(roster):
            print("Invalid input. Please enter a valid hero name or list number.")
            continue
        else:
            temp_hero = hero
            break

    if temp_hero == 0:
        continue
    else:
        hero_idx = temp_hero
        for i in range(len(roster)):
            if temp_hero == roster[i][1] or hero_idx == roster[i][0]:
                selected_hero = roster[i][1]
                break
    
    kills = int(input(f"Enter the number of kills for {selected_hero}: "))
    Deaths  = int(input(f"Enter the number of deaths: "))
    Assists = int(input(f"Enter the number of assists: "))
    match_status = input("Did you win the match? (yes/no): ").lower().strip()
    match_status = "WON" if match_status == "yes" else "LOST" # we will overwrite the match status to make it more readable
    
    KDA_val = (kills + Assists) / (1 if Deaths < 1 else Deaths) # calculating the KDA
    performance_status = None # we'll use this for determining the performance of the user in this match
    
    # we will compute the value of KDA so that we can determine whether the user on this match is doing great/WON or not.
    if KDA_val > 5 and match_status == "WON":
        performance_status = "DOMINATION!"
    elif KDA_val > 5 and match_status == "LOST":
        performance_status = "Carried hard!"
    elif KDA_val < 5 and match_status == "WON":
        performance_status = "Team effort!"
    else:
        performance_status = "Better luck next time!"

    KDAList.append([i, selected_hero, KDA_val, match_status, performance_status])

# let's calculate the average performance
total_wins = 0
total_lost = 0
best_match = None

for i in range(len(KDAList)):
    best_match = KDAList[i]
    if KDAList[i][3] == "WON":
        total_wins += 1
    else:
        total_lost += 1

    if best_match[2] < KDAList[i][2] and KDAList[i][3] == "WON":
        best_match = KDAList[i]

win_rate = ((total_wins / (total_wins + total_lost)) * 100) # final KDA from the summation_win

print("="*70)
print(f"{ign} -- MATCH LOG({rank})".center(70))
print("="*70)
for i in range(len(KDAList)):
    print(f"[{i}]: {KDAList[i][1]} | KDA: {KDAList[i][2]} | {KDAList[i][3]} | {KDAList[i][4]}")
print("-"*70)
print(f"Matches Played: {len(KDAList)}")
print(f"Wins: {total_wins} | Losses: {total_lost}")
print(f"Win Rate: {win_rate}%")
print(f"Best Match: [{best_match[0]}] {best_match[1]} (KDA: {best_match[2]})")
print("="*70)