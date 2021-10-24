input_data = input()

row = int(input_data[1])
column = int((ord(input_data[0]) - ord('a')) + 1)
result = 0
# print(f'ROW : {row} COL : {column}')

# 이동 경우의 수 8가지
steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

for step in steps:
    next_row = row + step[1] # 행 계산
    next_col = column + step[0] # 열 계산

    if next_row >= 1 and next_col <= 8 and next_row <= 8 and next_col >= 1:
        result += 1

print(result)