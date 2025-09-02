class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        read = 0        # pointer to scan through the array
        write = 0       # pointer to write compressed data in place

        while read < n:
            ch = chars[read]
            count = 0

            while read < n and chars[read] == ch:
                read += 1
                count += 1

            chars[write] = ch
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write

