["artichoke", "broccoli", "carrot", "daikon"]

def pair_print(items):
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            print(items[i], items[j])
