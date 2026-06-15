import random
random_number=random.randint(1, 100);
counter = 0
guess_number= int(input("Guess a number between 1 and 100: "))
#kaç tane tahmin var bilmiyorum for kullanmıcam while daha mantıklı
while guess_number != random_number:
    counter += 1
    if guess_number < random_number:
        print("Too low please your guess higher")
        guess_number= int(input("Guess a number between 1 and 100: "))
    else:
        print("Too high please your guess lower")
        guess_number= int(input("Guess a number between 1 and 100: "))
if guess_number == random_number:
    print("Your number is " + str(guess_number) + " and you guessed the number in " + str(counter) + " tries")