# Week 1 Review — Control Flow and Input

These examples cover a few Week 1 foundations that students need before the
Week 2 task:

- comparison operators;
- `if`, `elif`, and `else`;
- `for` loops;
- `while` loops; and
- the `input()` function.

Run the lesson from the repository root:

```bash
python Week1_Review/control_flow_and_input.py
```

The file is intentionally small and can be edited during class. Ask students to
predict each output before running the program.

## Suggested Teaching Flow

| Step | Concept | Function |
| ---: | --- | --- |
| 1 | Compare values | `demonstrate_comparisons()` |
| 2 | Choose between branches | `demonstrate_conditionals()` |
| 3 | Repeat a known number of times | `demonstrate_for_loop()` |
| 4 | Repeat until a condition changes | `demonstrate_while_loop()` |
| 5 | Read a value from the user | `demonstrate_input()` |

## Quick Exercises

1. Change `x` and `y` in `demonstrate_comparisons()` and predict which values
   become `True`.
2. Update `score` in `demonstrate_conditionals()` to test each branch.
3. Change the `range()` values in `demonstrate_for_loop()` so it prints from
   `5` to `10`.
4. Change the `while` loop so it stops after printing `5`.
5. Ask for the user's age with `input()`, convert it to an integer, and print
   the age they will be next year.
