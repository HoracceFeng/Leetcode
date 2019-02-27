# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/30/

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
## solution-1: The Best
        rows = [[] for k in range(9)]
        cols = [[] for k in range(9)]
        blos = [[] for k in range(9)]
        
        for i in range(9):
            for j in range(9):
                bloId = (i//3)*3 + j //3
                num = board[i][j]
                if num == '.':
                    continue
                
                if num not in rows[i]:
                    rows[i].append(num)
                else:
                    return False
                    # print 'rows', rows
                
                if num not in cols[j]:
                    cols[j].append(num)
                else:
                    return False
                    # print 'cols', cols
                
                if num not in blos[bloId]:
                    blos[bloId].append(num)
                else:
                    return False
                    # print 'blos', blos 
        
        return True



# ## solution-2
#         _data = board[0]
#         for index in range(1, len(board)):
#             _data.extend(board[index])
                
#         anchors  = [0,27,54]
#         for i in range(9):
#         ## row
#             _row = []
#             for indice in range(9*i, 9*(i+1)):
#                 _row.append(_data[indice])
#             if self.check_repeat(_row):
#                 return False
            
            
#         ## col
#             _col = []
#             for indice in range(i, 9*9+i, 9):
#                 _col.append(_data[indice])
#             if self.check_repeat(_col):
#                 return False
                
#         ## block
#             rolId = i // 3
#             colId = i % 3

#             anchor = anchors[rolId]
#             _blockId = []
#             _block = []
#             for j in range(0,3):
#                 _blockId.extend([anchor+9*0+3*colId+j, anchor+9*1+3*colId+j, anchor+9*2+3*colId+j])
#             for indice in _blockId:
#                 _block.append(_data[indice])
#             if self.check_repeat(_block):
#                 return False
        
#         return True
                        
        
#     def check_repeat(self, nums):
#         '''
#         :type nums: reverse sorted list
#         :rtype: bool
#         '''
#         nums = sorted(nums, reverse=True)
#         for i in range(len(nums)-1):
#             if nums[i] == '.':
#                 return False
#             if nums[i] == nums[i+1]:
#                 return True


## leetcode answer
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # init data
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3 ) * 3 + j // 3
                    
                    # keep the current cell value
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                    
                    # check if this value has been already seen before
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False         
        return True