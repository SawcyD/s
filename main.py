import random

with open ("Number.txt", "w") as f:
    maxNumber = 100


    def randomNumber ():
        randNumber = random.randint (1, 100000)
        return randNumber


    def gen100Numbers ():
        i = 0
        nums = []
        while i < 100:
            ran = randomNumber()
            nums.append (ran)
            # print (ran)
            i += 1

        nums = sorted (nums)
        return map (lambda a: str (a), nums)


    numbers2 = '\n'.join (gen100Numbers ())
    f.write (numbers2)

    # f.writelines ('\n'.join (numbers2))

f.close ()

# i = 0
# while i < 100: