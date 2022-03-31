import dictionary as dictionary

jihc = {"osp": "ol senin probleman", "hayirlisi": "bari jaqsy bolady"}
print(jihc)
jihc["izin"] = "ruqsat"
print(jihc)

print(len(jihc))

print("ruqsat" in jihc)  # only keys

val = jihc.values()
print(val)

ki = jihc.keys()
print(ki)

it = jihc.items()
print(it)


def count(a):
    d = dict()
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    print(d)


count("Ramazan")

ramo = {"Ema": "Just amazing", "ketsh": "Get out of here", "Rodnoi": "brat", "Emae": "Angry", "Uhuhuhuuuu": "Success",
        "We are venom": "Venom fan"}
print(ramo)
ramo["Eeeee"] = "Jestoka"
print(ramo)
print(len(ramo))