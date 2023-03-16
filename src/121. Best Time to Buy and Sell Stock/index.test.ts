import { maxProfit } from "."
import { Check } from "../types/index"

it("check", () => {
    const checks: Check[] = [
        { input: [7, 1, 5, 3, 6, 4], expect: 5 },
        { input: [7, 6, 4, 3, 1], expect: 0 },
    ]

    checks.forEach((check) => {
        expect(maxProfit(check.input)).toEqual(check.expect)
    })
})
