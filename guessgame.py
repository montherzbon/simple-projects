import random
tries :int=5
theNumberIamThinkingOf = random.randint(1,100)


for x in range(tries):

    guessTheNumber = int(input(f"guess the number you got {tries -x} tries:"))

    if theNumberIamThinkingOf == guessTheNumber:
        print("ding dong you got it right")
    else:
        print("incorrect try agian")
