"""
You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.


Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true


Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104

    

Takeaway:

each row is sorted that is meaning perhaps use binary beacuse sorted


"""

class Solution:
    def searchMatrix_(self, matrix: list[list[int]], target: int) -> bool:
        # the first solution that comes my mind
        # brute force
        for row in matrix:
            for col in row:
                if col == target:
                    return True
        return False



    def searchMatrix__(self, matrix: list[list[int]], target: int) -> bool:
        # i try secand solution that comes my mind
        # control to column for each row if col < target just look to other side
        
        for row in matrix:
            print(row)
            low = 0
            high = len(row) - 1
            mid = 0

            while low <= high:
                mid = low + ((high - low) // 2)
                
                if row[mid] == target:
                    return True
                elif row[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
        return False

            
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:           
        # neet code solution
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = bot + ((top - bot) // 2)
            if target > matrix[row][-1]:
                top = row + 1
            elif  target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if not (top <= bot):
            return False
        
        row = bot + ((top - bot) // 2)
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + (r - l)) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True




if __name__ == '__main__':
    sol = Solution()
    #print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
    #print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
    #print(sol.searchMatrix([[1]], 1))
    print(sol.searchMatrix([[1],[3]], 3))
    
