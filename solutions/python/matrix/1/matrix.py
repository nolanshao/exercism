class Matrix:
    def __init__(self, matrix_string):
        
        row_list = matrix_string.split("\n")
        
        
        self.matrix = []


        for row in row_list:
            tokens = row.split(" ")
            int_list = []
            for token in tokens: 
                int_list.append(int(token))


            self.matrix.append(int_list)
        
    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        y = []
        for l in self.matrix:
            y.append(l[index - 1])
        return y


