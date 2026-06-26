from typing import List


def sort_words(words: List[str]) -> List[str]:
    new_list = []
    for word in words:
        new_list.append(word)
        new_list.sort(key=lambda word: len(word), reverse=True)
    return new_list


def sort_numbers(numbers: List[int]) -> List[int]:
    new_list = []
    for number in numbers:
        new_list.append(number)
        new_list.sort(key=lambda number: abs(number))
    return new_list

# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
