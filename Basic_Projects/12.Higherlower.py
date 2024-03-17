import random
data = [
    {
        'name': 'Instagram',
        'follower': 346,
        'description': 'social media player',
        'country': 'us'
    },
    {
        'name': 'Kohli',
        'follower': 400,
        'description': 'cricket player',
        'country': 'india'
    },
    {
        'name': 'Ronaldo',
        'follower': 500,
        'description': 'football player',
        'country': 'portugal'
    },
    {
        'name': 'messi',
        'follower': 400,
        'description': 'football player',
        'country': 'argentina'
    },
]


def check_result(guess, c1_follower, c2_follower, score):
    if c1_follower == c2_follower:
        print("Neutral")
        score += 0
    elif c1_follower > c2_follower:
        return guess == "A"
    elif c2_follower > c1_follower:
        return guess == "B"


def format_data(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return (f"{account_name}, a {account_description} from {account_country}")


game_continue = True
score = 0
while game_continue == True:
    c1 = (random.choice(data))
    c2 = (random.choice(data))
    if c1 == c2:
        c2 = random.choice(data)
    print(f"Compare A :{format_data(c1)}")
    print("VS")
    print(f"Compare B :{format_data(c2)}")
    guess = input("Who has more followers A or B?\n")
    c1_follower = c1['follower']
    c2_follower = c2['follower']
    is_correct = check_result(guess, c1_follower, c2_follower, score)

    if is_correct:
        score += 1
        print(f"Your score is {score}")
    else:
        print("Dont worry")
        game_continue = False
