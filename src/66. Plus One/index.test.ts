import { plusOne } from "."
import { Check } from "../types/index"

it("check", () => {
    const checks: Check[] = [
        { input: [1, 2, 3], expect: [1, 2, 4] },
        { input: [4, 3, 2, 1], expect: [4, 3, 2, 2] },
        { input: [9], expect: [1, 0] },
    ]

    checks.forEach((check) => {
        expect(plusOne(check.input)).toEqual(check.expect)
    })
})
