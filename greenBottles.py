import time
bottles = 10
for bottles in range(bottles,0,-1):
    print("{0} Green bottles, hanging on the wall \n{0} Green bottles, hanging on the wall ".format(bottles))
    print("And if 1 green bottle should accidently fall \nThere'll be {0} green bottles left hanging on the wall.\n".format(bottles-1))
    time.sleep(8)
