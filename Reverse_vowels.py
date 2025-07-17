#Given a string, reverse only the vowels of the string.

def reverse_vowels(s):
    vowels = set('aeiouAEIOU')
    s = list(s)
    left,right = 0, len(s) - 1
    while left < right:
        if s[left] not in vowels:
            left = left + 1
        elif s[right] not in vowels:
            right = right - 1

        s[left], s[right] = s[right], s[left]
        left +=1
        right -=1
    return ''.join(s)

print(reverse_vowels("hello"))