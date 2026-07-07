class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sum_array = []
        for op in operations:
            if op == "+":
                sum_array.append(sum_array[-1] + sum_array[-2])
            elif op == "D":
                sum_array.append(sum_array[-1] * 2)
            elif op == "C":
                sum_array.pop()
            else:
                sum_array.append(int(op))
        return sum(sum_array)