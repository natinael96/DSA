class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        length = len(s)  

        # Create a list to store cumulative shifts for each character
        totShift = [0 for _ in range(length+1)]

        # Iterate over each shift operation
        for strt, end, direction in shifts:
            dxn = 1 if direction else -1
            totShift[strt] += dxn
            totShift[end + 1] -= dxn

        out = []
        
        # Apply shifts to each character in the input string
        for i in range(length):
            if i != 0:
                totShift[i] += totShift[i-1]
            newChar = (ord(s[i]) - ord("a") + totShift[i]) % 26 + ord("a")
            out.append(chr(newChar))
        
        # Return the modified string
        return "".join(out)