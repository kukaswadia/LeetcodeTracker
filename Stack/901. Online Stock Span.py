class StockSpanner:
    def __init__(self):
        # Stack to keep track of (price, span) pairs.
        self.stack = []

    def next(self, price: int) -> int:
        # Start with a span of 1 for the current price.
        span = 1

        # Pop elements from the stack while the current price is greater
        # or equal to the price on the top of the stack.
        while self.stack and self.stack[-1][0] <= price:
            # Add the span of the popped element to the current span.
            span += self.stack[-1][1]
            self.stack.pop()

        # Push the current (price, span) pair onto the stack.
        self.stack.append((price, span))
        return span

# --- Dry Run for Stack Approach ---
# For price = 70 (when the sequence is [100, 80, 60, 70]):
# 1. After processing 100, 80, 60:
#    Stack = [(100, 1), (80, 1), (60, 1)]
# 2. Process 70:
#    - span = 1
#    - Top of stack is (60, 1) and 60 <= 70, so pop it and add span: span becomes 2.
#    - Now top is (80, 1) and 80 > 70, so stop.
#    - Push (70, 2) → Stack becomes [(100, 1), (80, 1), (70, 2)]
# 3. Return span = 2.
