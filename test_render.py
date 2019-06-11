import Board
import BoardUI
import Pieces
import Moves


b = Board.Board()
ui = BoardUI.BoardUI(b)

b.board[10][10].append(Pieces.Spider())
b.board[11][10].append(Pieces.Ant(1))
b.board[12][10].append(Pieces.Queen(1))
b.board[10][11].append(Pieces.Beetle(1))
b.board[11][11].append(Pieces.Spider(1))
b.board[12][11].append(Pieces.Beetle(0))
b.board[10][12].append(Pieces.Grasshopper(0))
b.board[11][12].append(Pieces.Grasshopper(1))

moves = Moves.moves_spider(b, 10, 10)

ui.render_moves(moves)
ui.render()

Moves.play_move(b, (10, 10), (13, 11))

ui.render()
ui.manage_events()