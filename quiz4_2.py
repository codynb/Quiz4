#Cody Brown, code 2

def hash_spam(string, target):
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
    if total >= 4:
        print("this tweet will be considered a spam!")
    else:
        return None
