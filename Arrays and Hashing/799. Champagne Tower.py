class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        # Start with champagne is the top glass
        current_row = [poured]

        # Build the tower row by row until we reach query_row
        for row in range(query_row):
            next_row = [0] * (row + 2)

            # For each glass in current row
            for col in range(len(current_row)):
                # Calculate overflow (excess beyond 1 cup capacity)
                overflow = max(0, current_row[col] - 1)

                # Split overflow equally to two glasses below
                if overflow > 0:
                    next_row[col] += overflow / 2
                    next_row[col + 1] += overflow / 2

            current_row = next_row

        # Return the amount in the queried glass (max 1.0 since that's the capacity)
        return min(1.0, current_row[query_glass])