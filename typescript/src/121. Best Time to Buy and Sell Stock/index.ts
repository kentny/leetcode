export function maxProfit(prices: number[]): number {
    let maxProfit = 0
    let lowestPrice = prices[0]

    prices.forEach((price) => {
        if (price < lowestPrice) {
            lowestPrice = price
        } else {
            maxProfit =
                maxProfit < price - lowestPrice
                    ? price - lowestPrice
                    : maxProfit
        }
    })

    return maxProfit
}
