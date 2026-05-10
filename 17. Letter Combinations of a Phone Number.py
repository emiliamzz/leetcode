class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {}
        letters['2'] = ['a', 'b', 'c']
        letters['3'] = ['d', 'e', 'f']
        letters['4'] = ['g', 'h', 'i']
        letters['5'] = ['j', 'k', 'l']
        letters['6'] = ['m', 'n', 'o']
        letters['7'] = ['p', 'q', 'r', 's']
        letters['8'] = ['t', 'u', 'v']
        letters['9'] = ['w', 'x', 'y', 'z']
        output = letters[digits[0]].copy()
        if len(digits) >= 2:
            output_copy = output.copy()
            size = len(output)
            for i in range(len(letters[digits[1]])-1):
                output.extend(output_copy)
            last = 0
            for i in range(len(letters[digits[1]])):
                letter = letters[digits[1]][i]
                print(letters)
                for j in range(last, size+last):
                    output[j] += letter
                last += size
        if len(digits) >= 3:
            output_copy = output.copy()
            size = len(output)
            for i in range(len(letters[digits[2]])-1):
                output.extend(output_copy)
            last = 0
            for i in range(len(letters[digits[2]])):
                letter = letters[digits[2]][i]
                for j in range(last, size+last):
                    output[j] += letter
                last += size
        if len(digits) == 4:
            output_copy = output.copy()
            size = len(output)
            for i in range(len(letters[digits[3]])-1):
                output.extend(output_copy)
            last = 0
            for i in range(len(letters[digits[3]])):
                letter = letters[digits[3]][i]
                for j in range(last, size+last):
                    output[j] += letter
                last += size
        return output