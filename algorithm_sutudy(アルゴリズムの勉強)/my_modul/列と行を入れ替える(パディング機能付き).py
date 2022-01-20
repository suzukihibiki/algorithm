

class TransposeMsatrix:
            
    def __init__(
        self,
        matrix_ : list
    ) -> None:
        self.matrix = matrix_

    def padding(self,missing_value_ = 0):
        
        # 最大サイズのlen
        l = max(map(len, self.matrix))
                
        B = list(map(
            lambda x: x + [missing_value_]*(l-len(x)), self.matrix
            ))
        
        self.matrix = B
        
    def transpose_matrix(self):
        """
        transpose_matrix
        
        args
        ---
        matrix_ : list
            ex)
            [
                [1, 2, 3, 4, 10, 35],
                [5, 6, 7, 8],
                [9, 10, 11, 12, 8, 4, 9, 8, 13],
            ]
        missing_value_ : int or str
            The value to embed if an incorrect value is found.
        return
        ---
        [
            [1, 5, 9], 
            [2, 6, 10], 
            [3, 7, 11], 
            [4, 8, 12],
            [10, 0, 12],
            [35, 0, 8],s
            [0, 0, 4],
            [0, 0, 9],
            [0, 0, 8],
            [0, 0, 13]
        ]
        
        """
        _transpose_matrix = [
            [row[i] for row in self.matrix] for i in range(len(self.matrix[0]))
        ]
        return _transpose_matrix

mtrix =TransposeMsatrix([
                [1, 2, 3, 4,8],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
            ])
mtrix.padding(
    missing_value_=False
)
a = mtrix.transpose_matrix()
print(a)
