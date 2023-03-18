import { Check } from "../types/index"
import {productExceptSelf} from "./index";

it("check", () => {
  const checks: Check[] = [
    { input: [1,2,3,4], expect: [24,12,8,6] },
    { input:  [-1,1,0,-3,3], expect: [0,0,9,0,0] },
  ]

  checks.forEach((check) => {
    expect(productExceptSelf(check.input)).toEqual(check.expect)
  })
})
