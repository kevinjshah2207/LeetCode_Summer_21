class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        flag_r = False
        flag_c = False
        # for i in range(1,m,1):
        #     for j in range(1,n,1):
        #         if matrix[i][j] == 0:
        #             matrix[i][0] = 'a'
        #             matrix[0][j] = 'a'
        # if matrix[0][0] == 'a':
        #     flag = True
        # else:
        #     flag = False
        # for i in range(m-1,0,-1):
        #     if matrix[i][0] == 'a':
        #         flag1 = True
        #         for j in range(n):
        #             matrix[i][j] = 0
        # for j in range(n-1,0,-1):
        #     if matrix[0][j] == 'a':
        #         for i in range(m):
        #             matrix[i][j] = 0
        # if flag:
        #     for i in range(m):
        #         matrix[i][0] = 0
        #     for j in range(n):
        #         matrix[0][j] = 0
        # return matrix
        for i in range(m):
            for j in range(n):
                if matrix[i][0] == 0:
                    flag_r = True
                if matrix[0][j] == 0:
                    flag_c = True
                if matrix[i][j] == 0:
                    matrix[i][0] = 'a'
                    matrix[0][j] = 'a'
        for i in range(m-1,0,-1):
            if matrix[i][0] == 'a':
                flag1 = True
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(n-1,0,-1):
            if matrix[0][j] == 'a':
                for i in range(m):
                    matrix[i][j] = 0
        if flag_r:
            for i in range(m):
                matrix[i][0] = 0
        if flag_c:
            for j in range(n):
                matrix[0][j] = 0
        return matrix