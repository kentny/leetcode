export function plusOne(digits: number[]): number[] {
    let increment = 1
    const result: number[] = []

    while (true) {
        const digit = digits.pop()
        if (digit === undefined) {
            if (increment > 0) {
                result.push(increment)
            }
            return result.reverse()
        }
        let sum = digit + increment
        if (sum > 9) {
            increment = 1
            sum %= 10
        } else {
            increment = 0
        }
        result.push(sum)
    }
}
