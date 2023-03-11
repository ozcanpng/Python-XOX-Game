def print_board(board):
    print("-------------")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("-------------")

def check_win(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player) or \
       (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[0] == player and board[4] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False

def main():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print_board(board)
    player = "X"
    count = 0
    while True:
        move = int(input("Nereye koymak istersin " + player + " (1-9)? "))
        if board[move-1] == "X" or board[move-1] == "O":
            print("Bu alan zaten kullanıldı. Lütfen tekrar deneyiniz.")
            continue
        else:
            board[move-1] = player
            count += 1
            print_board(board)
        if check_win(board, player):
            print("Tebrikler! Oyuncu " + player + " Kazandı!")
            break
        if count == 9:
            print("Berabere!")
            break
        if player == "X":
            player = "O"
        else:
            player = "X"

if __name__ == "__main__":
    main()