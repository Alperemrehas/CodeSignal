def solution(cell1, cell2):
    charachter_black = ['A', 'C', 'E', 'G']
    charachter_white = ['B', 'D', 'F', 'H']

    cell1_c = cell1[0]
    cell1_n = int(cell1[1])
    cell2_c = cell2[0]
    cell2_n = int(cell2[1])

    cell1_color = 'b' if (cell1_c in charachter_black and cell1_n % 2 != 0) or (cell1_c in charachter_white and cell1_n % 2 == 0) else 'w'
    cell2_color = 'b' if (cell2_c in charachter_black and cell2_n % 2 != 0) or (cell2_c in charachter_white and cell2_n % 2 == 0) else 'w'

    return cell1_color == cell2_color


'''def solution(cell1, cell2):
    charachter_black = ['A', 'C', 'E', 'G']
    charachter_white = ['B', 'D', 'F', 'H']

    cell1_c = cell1[0]
    cell1_n = int(cell1[1])
    cell2_c = cell2[0]
    cell2_n = int(cell2[1])

    cell1_color = 'b' if (cell1_c in charachter_black and cell1_n % 2 != 0) or (cell1_c in charachter_white and cell1_n % 2 == 0) else 'w'
    cell2_color = 'b' if (cell2_c in charachter_black and cell2_n % 2 != 0) or (cell2_c in charachter_white and cell2_n % 2 == 0) else 'w'

    return cell1_color == cell2_color


'''