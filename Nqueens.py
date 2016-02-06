class nqueen:
    def __init__(self,number_of_queens):
        self.rowqueen = [None]*number_of_queens
        self.number_of_rows = self.number_of_queens = self.number_of_columns =  number_of_queens


    def solvequeens(self):
        self.arrangequeen(0)

    def arrangequeen(self,rowindex):
        for i in range(self.number_of_columns):
            if self.isValid(rowindex,i):
                self.rowqueen[rowindex] = i
            if rowindex == (self.number_of_queens - 1):
                self.printqueens()
            else:
                self.arrangequeen(rowindex + 1)

    def isValid(self,rowindex,columnindex):
        for i in range(rowindex):
            if self.rowqueen[i] == columnindex:
                return False

            if ((i - rowindex) == (self.rowqueen[i] or 0 - columnindex)):
                return False
            if ((i - rowindex) == (columnindex - self.rowqueen[i] or 0)):
                return False

    def printqueens(self):
        for i in range(self.number_of_columns):
            for j in range(self.number_of_rows):
                if self.rowqueen[i] == j:
                    print ('Q',end=" ")
                else:
                    print('-',end= " ")
            print()

if __name__ == "__main__":
    nqueens = nqueen(4)
    nqueens.solvequeens()
    print(nqueens.rowqueen)

