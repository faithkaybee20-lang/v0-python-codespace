colors = ["gray", "cream", "cyan"]
clothes = ["shirt", "flannel"]

def print_combinations(colors, clothes):
    for color in colors:
        for item in clothes:
            print(color, item)
