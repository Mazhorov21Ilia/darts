import random

turn = random.randint(0, 1)
users = {'Vlad': 0, 'Ilia': 0}

chet = int(input("До скольки игра: "))

def one_time(turn):
    print("Очередь Ильи") if turn == 1 else print("Очередь Влада")

    tries = sum(map(int, input().split()))
    if turn == 1:
        users["Ilia"] += tries
    else:
        users["Vlad"] += tries
    print(f"\nИлья: {users["Ilia"]}\nВлад: {users["Vlad"]}\n")
    turn = 1 - turn
    print("Очередь Ильи") if turn == 1 else print("Очередь Влада")

    tries = sum(map(int, input().split()))
    if turn == 1:
        users["Ilia"] += tries
    else:
        users["Vlad"] += tries
    print(f"\nИлья: {users["Ilia"]}\nВлад: {users["Vlad"]}\n")
    turn = 1 - turn

while True:
    if users["Ilia"] == chet and users["Vlad"] != chet:
        print("Илья победил")
        break
    elif users["Vlad"] == chet and users["Ilia"] != chet:
        print("Влад победил")
        break
    elif users["Vlad"] == chet and users["Ilia"] == chet:
        print("ГОООООООООООООООООЙДА")
        break
    else:
        one_time(turn)

