Point values in brackets.

## Interview questions

Three interview questions.

Choose one set for the entire cohort.

### Set 1

1. When is the ALU activated in the CPU?

   * [1] student lists 1 of "math" or "comparisons"

   * [2] student lists both of them

2. Why is a CPU stack useful in assembly language?

   * [1] Mentions AT LEAST ONE: return addresses, storing temporary values, or
     passing arguments to subroutines

   * [2] Mentions MULTIPLE of the level 2 answers OR mentions that higher-level
     languages use stacks extensively

3. Convert the 8-bit binary number 0bXXXXXXXX (PM's choice) to hex.

   * [1] student can do it with code/calc/google

   * [2] student can do it by hand

### Set 2 (EU3)

1. The CALL instruction doesn't allow you to pass any arguments. What are some
   ways to effectively get arguments to a subroutine?

   * [1] student mentions "stack", "registers" or "memory/RAM".

   * [2] student mentions "stack and registers" or "memory/RAM and registers".

2. What's the result of bitwise-AND between `0b110` and `0b011`?

   * [1] student can do it with code/calc (answer: `0b010`)

   * [2] student can do it by hand

3. Convert the 8-bit binary number 0bXXXXXXXX (PM's choice) to hex.

   * [1] student can do it with code/calc/google

   * [2] student can do it by hand

## LS-8 CMP, JMP, JEQ, JNE

_**Note:** student answers might vary. Points depend on working functionality,
not on the details of how it was implemented._

Changes to `cpu.py`:

* Add `FL` register to `cpu class`.
* Add `FLAG_EQ` `variable (constant)`.
* Add `ALU_CMP` `opcode to the alu function`.
* Add `variables`s for new instructions.
* Add `CMP` support to `alu()`.
* Add new instructions to `if cascade / branch table`.

Points:

* [3] `JMP` working
* [6] `CMP` working
* [3] `JNE` working
* [3] `JEQ` working

## Scoring

Total possible: 21

| Total | Result |
|:-----:|:------:|
| 0-13  |    1   |
| 14-19 |    2   |
|  20+  |    3   |
