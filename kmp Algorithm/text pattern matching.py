# Knuth-Morris-Pratt algorithm for string pattern searching
# on-the-fly cache for prefix as suffix, reduce O(M * N) -> O(M + N) by naive sliding-window
def KMPSearch(text, pattern):
    M, N = len(text), len(pattern)
    kmp = [0] * N

    ret = []

    # construct look-up table/cache
    for i in range(1, N):
        suffix = kmp[i - 1]
        while suffix > 0 and pattern[suffix] != pattern[i]:
            suffix = kmp[suffix - 1]

        if pattern[suffix] == pattern[i]:
            kmp[i] = suffix + 1

    i, j = 0, 0

    # reduce time-complexity when N is large(i.e. long-paragraph)
    while M - i >= N - j:
        if text[i] == pattern[j]:
            i += 1
            j += 1

            # pattern found, add to result
            if j == N:
                ret.append(i - N)
                # print(text[i - N: i])
                j = kmp[j - 1]

        # fix for index-out-of-range while i is increasing
        elif i < M and text[i] != pattern[j]:
            # reduce suffix length
            if j > 0:
                j = kmp[j - 1]

            # no possible matching, increase index for next candidate
            else:
                i += 1

    return ret

# Testing
if __name__ == '__main__':
    txt = "ABCBGBKQABABCQBGJABCQWGQAB"
    pat = "ABC"

    print(f'Find pattern at index: {KMPSearch(txt, pat)}')