def reduce_time(pumps):
    return pumps - 1


def fill_max_time(pumps, A):
    # print(pumps[0])
    # print(A)
    moments = sum(A)
    # print(moments)
    P0 = P1 = P2 = 0
    min_r = 0
    max_r = 2

    for moment in list(range(moments)):
        # for i in range(0, max_r):
        # for i, x in enumerate(range):
        i = 0
        while i < max_r:
            #print("max_r {}".format(max_r))
            car = A[i]
            carasig = False
            if car <= int(pumps[0]) and P0 == 0 and carasig is False and car > 0:
                P0 = car
                max_i = i
                A[i] = -1
                carasig = True

            if car <= int(pumps[1]) and P1 == 0 and carasig is False and car > 0:
                P1 = car
                max_i = i
                A[i] = -1
                carasig = True
                if P1 == -1:
                    max_r = max_i + 1

            if car <= int(pumps[2]) and P2 == 0 and carasig is False and car > 0:
                print("Car " + str(car) + "  " + str(pumps[2]) + "  " + str(P2) + "  " + str(carasig))
                P2 = car
                max_i = i
                A[i] = -1
                carasig = True
                if P2 == -1:
                    max_r = max_i + 1
            i = i + 1
        # print("Max  {}".format(max_i))

        print("Momento {} carro {} P0 {} P1 {} P2 {}".format(moment, A[i], P0, P1, P2))
        # reduce time
        if P0 > 0:
            P0 = P0 - 1
            if P0 == 0:
                max_r = max_i + 1

        if P1 > 0:
            P1 = P1 - 1
            if P1 == 0:
                max_r = max_i + 1

        if P2 > 0:
            P2 = P2 - 1
            if P2 == 0:
                max_r = max_i + 1


X = 8
Y = 11
Z = 2
# Cars
A = [2, 8, 4, 3, 2]

# Python 3 tuple paramerer not def supported
pumps = [X, Y, Z]
fill_max_time(pumps, A)
print(A)
