
def strStr(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l1 = []
        for i in range(len(haystack)-len(needle)+1):
            l1.append(haystack[i:i+len(needle)])

        tracker = 0
        for s in l1:
            if s == needle:
                return(tracker)
            tracker += 1


        return(-1)


if __name__ == '__main__':
    Haystack = "sadbutsad"
    Needle = "sad"

    print(strStr(Haystack, Needle))

    