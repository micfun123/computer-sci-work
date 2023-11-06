return Matrix(
    *[
        [
            sum([val * column[i] for val, column in zip(row, other.rows)])
            for i, _ in enumerate(other.rows[0])
        ]
        for row in self.rows
    ]
)
