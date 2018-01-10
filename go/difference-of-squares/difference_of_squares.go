package diffsquares

func SquareOfSums(n int) int {
	sum := sum(n)
	square := sum * sum
	return square
}

func sum(val int) int {
	if val == 0 {
		return 0
	}
	return val + sum(val-1)
}

func SumOfSquares(num int) int {
	if num == 0 {
		return 0
	}
	return num*num + SumOfSquares(num-1)
}

func Difference(n int) int {
	return SquareOfSums(n) - SumOfSquares(n)
}

