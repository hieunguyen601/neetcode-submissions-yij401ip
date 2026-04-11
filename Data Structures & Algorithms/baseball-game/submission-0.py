class Solution:
    def calPoints(self, operations: List[str]) -> int:
        new_array = []
        for i in range(len(operations)):
            if operations[i] == "C":
                new_array.pop()
            elif operations[i] == "+":
                new_array.append(new_array[-1] + new_array[-2])
            elif operations[i] == "D":
                new_number = 2 * new_array[-1]
                new_array.append(new_number)
            else:
                new_array.append(int(operations[i]))
        return sum(new_array)