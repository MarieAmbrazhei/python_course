"""Homework10_2:Functions. Writing and implementing programs."""


# Свечи
# Когда свеча догорает, остается остаток. Остатки можно объединить, чтобы
# создать новую свечу, которая при догорании, в свою очередь, оставит
# еще один остаток. У вас есть количество свечей. Какое общее количество
# свечей вы можете сжечь, если предположить, что вы создадите
# новые свечи, как только у вас останется достаточно остатков?

def solution(candles_number: int, make_new: int) -> int:
    """
    Calculates total candles burned, including those made from remainders.
    """
    total_burned = 0
    candle_stubs = 0

    while candles_number > 0:
        total_burned += candles_number
        candle_stubs += candles_number
        candles_number = candle_stubs // make_new
        candle_stubs = candle_stubs % make_new
    return total_burned


assert solution(5, 2) == 9
assert solution(1, 2) == 1
assert solution(15, 5) == 18
assert solution(12, 2) == 23
assert solution(6, 4) == 7
assert solution(13, 5) == 16
assert solution(2, 3) == 2
