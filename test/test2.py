#! /usr/bin python3
#conding: utf-8

import json


# categories = []
testA = []
testB = []
dico = {}
#name_cate = ["boissons", "fruits", "legumes-et-derives", "produits-laitiers",
#"poissons", "viandes", "desserts", "cereales-et-derives"]
name_cate = ["boissons", "fruits", "legumes-et-derives", "produits-laitiers",
"poissons", "viandes", "desserts", "cereales-et-derives"]

with open("all.json", "r") as file:
    data = json.load(file)

    for cat in name_cate:
        for foo in data[cat]:
            alim_list = foo
            #print(alim_list)
            testA.append(alim_list)

        print(len(testA))
        nb = -1
        for x in testA[:]:
            nb += 1
            if x[0] not in testB:
                testB.append(x[0])
            else:
                del(testA[nb])
                nb -= 1
        dico[cat] = testA
        #print("\n")
        #print(testB)
        #print("\n")
        #print(testA)
        print(len(testA))
        testA = []
        testB = []


#with open("all.json", "w") as file:
#    json.dump(dico, file, indent=4, ensure_ascii=False)