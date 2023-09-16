export function productExceptSelf(nums: number[]): number[] {
  const prefix: number[] = []
  const postfix: number[] = []
  const result: number[] = []

  for (let i = nums.length - 1; i > 0; i--) {
    if (i < nums.length - 1) {
      postfix[i] = postfix[i + 1] * nums[i]
    } else {
      postfix[i] = nums[i]
    }
  }

  for (let i = 0; i < nums.length; i++) {
    if (i === 0) {
      prefix[i] = nums[i]
      result[i] = postfix[i + 1]
    } else if (i === nums.length - 1) {
      result[i] = prefix[i - 1]
    } else {
      prefix[i] = prefix[i - 1] * nums[i]
      result[i] = prefix[i - 1] * postfix[i + 1]
    }
  }

  return result
}
