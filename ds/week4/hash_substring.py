# python3

class Rabin:

    def __init__(self, pattern, text):
        self.pattern = pattern
        self.text = text
        self.window = len(pattern)
        self.scan_bound = len(text) - len(pattern) + 1
        self.checksums = []

    def checksum(self, string):
        return sum([ord(string[i]) for i in range(len(string))])

    def precompute(self):
        self.checksums.append(self.checksum(self.text[:self.window]))

        for i in range(1, self.scan_bound):
            old_hash = self.checksums[i - 1]
            left_l_hash = ord(self.text[i - 1])
            right_l_hash = ord(self.text[i + self.window - 1])

            ith_hash = old_hash - left_l_hash + right_l_hash
            self.checksums.append(ith_hash)

    def psearch(self):
        pattern_checksum = self.checksum(self.pattern)
        self.precompute()
        results = []
        for i in range(self.scan_bound):
            if pattern_checksum == self.checksums[i]:
                if self.pattern == self.text[i:i + self.window]:
                    results.append(i)
        return results


if __name__ == "__main__":
    pattern, text = input().rstrip(), input().rstrip()
    ts = Rabin(pattern, text)
    result = ts.psearch()
    print(" ".join(map(str, result)))

