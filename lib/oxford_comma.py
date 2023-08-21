def oxford_comma(items):
#     return " ".join(items)
# def oxford_comma(items):
#     return " and ".join(items)
# def oxford_comma(items):
    if len(items) > 1:
        items[-1] = "and " + items[-1]

    if len(items) > 2:
        return ', '.join(items)
    else:
        return ' '.join(items)

print(oxford_comma(["kiwi", "durian", "starfruit"]))