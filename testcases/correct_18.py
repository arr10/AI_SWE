'''Given an integer numRows, return the first numRows of Pascal's triangle.'''

def correct_18(numRows: int):
        a = []
        a.append([1])
        for i in range(1, numRows):
            b = []
            for j in range(len(a[i-1])+1):
                if j != 0 and j < len(a[i-1]):
                    b.append(a[i-1][j-1]+a[i-1][j])
                else:
                    b.append(1)
            a.append(b)
        return a

