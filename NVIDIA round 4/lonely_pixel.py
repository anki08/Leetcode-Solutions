class Solution:
    def findLonelyPixel(self, picture):
        R,C = len(picture), len(picture[0])
        row = []
        col = []
        for i in range(R):
            for j in range(C):
                if picture[i][j] == 'B':
                    row.append(i)
                    col.append(j)
                else:
                    continue
        count = 0
        for i in range(len(row)):
            col_new = col[:i]+col[i+1:]
            row_new = row[:i]+row[i+1:]
            if row[i]not in row_new and col[i] not in col_new:
                count +=1
        return (count)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findLonelyPixel([["W","W","B"],["W","B","W"],["B","W","W"]]))