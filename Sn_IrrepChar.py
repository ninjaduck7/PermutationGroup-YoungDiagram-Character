# ==========================================
# MIT License
#
# Copyright (c) 2025 田佳猛
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# ==========================================


def print_young(board):
    """
    打印 Young 盘。
    """
    for row in board:
        print(" ".join(str(x) if x != 0 else "." for x in row))
    print("-" * 20)


def dfs_fill(board, partition, numbers, idx=0):
    """
    逐步填充数字到 Young 盘中。
    borad: 已经填充的部分
    partition: 配分/Young 图的结构
    numbers: 所有需要填充的数字
    idx: 当前需要填充的数字
    """

    if idx == len(numbers):
        # 填充完毕
        print_young(board)  # 打印下来看看情况
        return 1

    # sym: 填充的数字。只是起到一个符号的作用，因此命名为symbol
    # count: 填充的个数
    sym, count = numbers[idx]
    nrows = len(partition)

    magic = 0  # 魔法数字

    for start_row in range(nrows):
        # 找到该行最左侧空的格子
        c = 0
        while c < partition[start_row] and board[start_row][c] != 0:
            c += 1
        if c >= partition[start_row]:
            continue

        # 按照指定规则给出填充位置
        boxes = []  # 用来装这些数字所在位置的
        row, col = start_row, c  # 当前位置

        # 判断位置有效性
        is_valid = lambda r, c: 0 <= r < len(partition) and 0 <= c < partition[r]

        boxes += [(row, col)]
        for _ in range(count - 1):
            # 能往上走就往上走
            if is_valid(row - 1, col) and board[row - 1][col] == 0:
                row -= 1
                boxes += [(row, col)]
                continue
            # 不能往上走就往右走
            if is_valid(row, col + 1) and board[row][col + 1] == 0:
                col += 1
                boxes += [(row, col)]
                continue
            # 如果既不能往上走，又不能往右走，那么说明方案不可行
            boxes = []
            break

        # 填完数字后还要看看前一行是不是空的，如果是，则失败
        if is_valid(row - 1, col) and board[row - 1][col] == 0:
            boxes = []

        # 方案不可行
        if len(boxes) == 0:
            continue

        # 数字填充产生的符号
        sign = (-1) ** (start_row - row)

        # 深搜
        for row, col in boxes:
            board[row][col] = sym
        magic += sign * dfs_fill(board, partition, numbers, idx + 1)

        # 回溯
        for row, col in boxes:
            board[row][col] = 0

    return magic


def character(partition, cycle_type):
    """
    计算置换群不可约表示 partition 下共轭类 cycle_type 对应的特征标。
    """

    # 设循环结构为 (v1, v2, ...)
    # numbers 则为 [(1, v1), (2, v2), ...]
    numbers = [(i + 1, l) for i, l in enumerate(cycle_type)]

    # 初始化 Young 盘，未填充的部分用 '0' 标记
    board = [[0] * n for n in partition]

    # 深度优先搜索所有的可能填充方式
    return dfs_fill(board, partition, numbers)


# partition = [3, 2, 2]
# cycle_type = [1, 2, 2, 2]

# partition = [3, 2, 1]
# cycle_type = [1, 2, 1, 1, 1]

# partition = [3, 2, 1]
# cycle_type = [1, 1, 1, 1, 2]

# partition = [3, 2, 1]
# cycle_type = [2, 1, 1, 1, 1]

partition = [3, 2, 1]
cycle_type = [1,1,1,1,2]

print(character(partition, cycle_type))
