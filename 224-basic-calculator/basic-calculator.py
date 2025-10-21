class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_result = 0
        current_sign = 1 # 1 for positive, -1 for negative
        index = 0
        length = len(s)

        while index < length:
            char = s[index]

            if char.isdigit():
                number = 0
                digit_start = index
                
                while digit_start < length and s[digit_start].isdigit():
                    number = number * 10 + int(s[digit_start])
                    digit_start += 1
                
                current_result += current_sign * number
                
                index = digit_start - 1
            elif char == '+':
                current_sign = 1
            elif char == "-":
                current_sign = -1
            elif char == "(":
                stack.append(current_result)
                stack.append(current_sign)

                current_result = 0
                current_sign = 1
            
            elif char == ")":
                prev_sign = stack.pop()
                prev_result = stack.pop()

                current_result = prev_sign * current_result + prev_result
            
            index += 1
        
        return current_result