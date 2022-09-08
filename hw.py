#GREED IS GOOD

def score(dice):
    from collections import Counter
    points = {1:1000, 6:600, 5:500, 4:400, 3:300, 2:200}
    dices = Counter(dice)

    tot = 0

#O(n)
#                   O(n)
    for k,v in dices.items():
        if v >= 3:
            tot += points[k] * (v // 3)
        if k == 1:
            tot += 100 * (v % 3)
        elif k == 5:
            tot += 50 * (v % 3)

    return tot

#ANAGRAM DETECTION
# O(1)
def is_anagram(test, original):
    return set(test.lower()) == set(original.lower()) and len(test) == len(original)

#+1 ARRAY
#O(n)
def up_array(arr):
    if len(arr) < 1 :
        return None

    for i in arr:
        if len(str(i)) > 1 or i < 0:
            return None
    else:
        return [int(i) for i in str(int("".join([str(n) for n in arr]))+1)]