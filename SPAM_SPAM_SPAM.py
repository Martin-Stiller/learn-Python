from random import shuffle

liste=("amazing gorgeous vibrant blazing stunning biggest fastest tremendous fantastic phenomenal delightful \
ambitious staggering  smarter massive incredible spectacular super excited cool magical revolutionary intuitive").upper().split()

shuffle(liste)

for x in range(5):
    for n in range(2):
        for i in range(4):
            print("Spam ",end='')
        print()
        
    ele1 = liste.pop()
    ele2 = liste.pop()

    print("{} SPAM , {} SPAM".format(ele1, ele2))
    print()
    print ()
    