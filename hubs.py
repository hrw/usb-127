#!/bin/python3


devices = 0

for h1 in [1,2,3,4]:
    if devices < 128:
        print("hub:%d" % h1)
        devices += 1
        for h2 in [1,2,3,4]:
            if devices < 128:
                print("\thub:%d.%d" % (h1, h2))
                devices += 1
                for h3 in [1,2,3,4]:
                        if devices < 128:
                            print("\t\thub:%d.%d.%d" % (h1, h2, h3))
                            devices += 1
                            for h4 in [1,2,3,4]:
                                if devices < 128:
                                    print("\t\t\tdev:%d.%d.%d.%d" % (h1, h2, h3, h4))
                                    devices += 1
