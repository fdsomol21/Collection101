#Francis
#Slots
import random
symbols = ["♠","♡","♢","7"]
weights = [35,35,25,5]
player_credit = 0
print("Hello! Welcome to Slots")
print("Each spin costs 10 tokens")
def spin_reels():
    r1 = random.choices(symbols, weights)
    r2 = random.choices(symbols, weights)
    r3 = random.choices(symbols, weights)
    return r1, r2, r3
def check_win(reels):
    r1 = reels[0]
    r2 = reels[1]
    r3 = reels[2]
    if r1 == r2 and r2 == r3:
        if r1 == "7":
            return "JACKPOT!", 200
        else:
            return "Small Win!", 50
    return "No win this time.", 0
def main():
    global player_credit
    while True:
        print("1. Deposit money")
        print("2. Spin")
        print("3. Cash Out")
        choice = input("Select: 1, 2, 3: ")
        if choice == "1":
            amount = input("Deposit 50, 100, or 500 tokens: ")
            if amount in ["50","100","500"]:
                player_credit = player_credit + int(amount)
                print(f"Your current balance is {player_credit} tokens.")
            else:
                print("Invalid deposit amount.")
        elif choice == "2":
            if player_credit < 10:
                print("Not enough credits to spin.")
            else:
                player_credit = player_credit - 10
                reels = spin_reels()
                print(f"Spin results: {reels}")
                msg, payout = check_win(reels)
                print(msg)
                if payout > 0:
                    player_credit = player_credit + payout
                    print(f"You won {payout} tokens!")
                print(f"Remaining balance: {player_credit} tokens")
        elif choice == "3":
            print(f"Thanks for playing. You cashed out with {player_credit} tokens.")
            break
        else:
            print("Invalid input. Try again.")
def sim():
    total_spent = 0
    total_won = 0
    for i in range(1000):
        total_spent = total_spent + 10
        r1 = random.choices(symbols, weights)[0]
        r2 = random.choices(symbols, weights)[0]
        r3 = random.choices(symbols, weights)[0]
        if r1 == r2 and r2 == r3:
            if r1 == "7":
                total_won = total_won + 200
            else:
                total_won = total_won + 50
    print(f"Credits Spent: {total_spent}")
    print(f"Total Credits Won: {total_won}")
    print(f"House Profit: {total_spent - total_won}")
main()
