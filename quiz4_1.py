#Cody Brown, code 1
def count_hashtag(string, target):
    index = 0
    total = 0
    while index < len(string):
        if string[index : index + len(target)] == target:
            total += 1
            index += 1
            return total
        else:
            index += 1
    return total
