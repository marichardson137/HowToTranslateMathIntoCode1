@Override
public List<Square> getLegalMoves(Board b) {
    Square[][] board = b.getSquareArray();
    int x = this.getPosition().getXNum();
    int y = this.getPosition().getYNum();
    
    return getDiagonalOccupations(board, x, y);
}