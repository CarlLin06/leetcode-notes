# LeetCode 9. Palindrome Number

**Difficulty:** Easy
**Link:** https://leetcode.com/problems/palindrome-number/

## Problem

Given an integer `x`, return `True` if `x` is a palindrome (reads the same forwards and backwards), and `False` otherwise.

- `121` → `True`
- `-121` → `False` (negative sign breaks symmetry)
- `10` → `False` (reversed is `01`)

## Thought Process

1. First idea: convert the number to a string, reverse it, compare. Simple and intuitive.
2. Follow-up: can we do it without converting to a string (O(1) space)? Yes — reverse only the second half of the number using `%` and `//`, then compare with the first half.
3. Key edge cases for the math approach: negative numbers are never palindromes; numbers ending in 0 (but not 0 itself) are never palindromes.

## Mistakes & Lessons

- Wrote `num1 = print(s[::-1])` — two bugs: used a non-existent variable `s` instead of `num`, and used `print()` which returns `None` instead of just assigning the reversed string.
- Forgot the colon `:` after `if` and `else` → `SyntaxError: expected ':'`.
- Wrote lowercase `true` / `false` (Java habit) → `NameError: name 'true' is not defined`. Python uses `True` / `False` (and `None`) — capitalized.

Key takeaway: in Python, an `if cond: return True / else: return False` block can be collapsed to `return cond`, because the comparison itself is already a boolean.

## Solutions

### String Reversal (my solution)

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)          # convert int to string
        num1 = num[::-1]      # reverse via slicing
        return num == num1    # compare (the condition is already a bool)
```

**Time:** O(n)　**Space:** O(n)　(n = number of digits; extra strings cost O(n) space)

### Optimized — Reverse Half (O(1) space)

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # negatives, and numbers ending in 0 (except 0) can't be palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted = 0
        while x > reverted:                      # stop at the midpoint
            reverted = reverted * 10 + x % 10    # append x's last digit to reverted
            x = x // 10                          # drop x's last digit (integer division)

        # even digits: x == reverted
        # odd digits:  x == reverted // 10 (drop the middle digit)
        return x == reverted or x == reverted // 10
```

**Time:** O(n)　**Space:** O(1)

## Java vs Python Notes

- Integer division: Python `//` vs Java `/` (Python `/` returns a float).
- Logical operators: Python `and` / `or` vs Java `&&` / `||`.
- Booleans: Python `True` / `False` vs Java `true` / `false`.
- String reversal: Python `s[::-1]` (slicing) is unique; Java needs `new StringBuilder(s).reverse().toString()`.

## Related Problems

- 234. Palindrome Linked List
- 125. Valid Palindrome
- 7. Reverse Integer
