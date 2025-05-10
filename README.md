# FRACTRAN

Online Interpreter: [https://tjwei.github.io/Fractran/](https://tjwei.github.io/Fractran/)

## Swap
Task: write a program that swaps register $2$ with register $3$ (i.e given $2^k$, return $3^k$).

Code:

```2/3```

## Addition

Task: write a program that takes two inputs in registers $2$ and $3$, and adds them, placing the result in register $5$ (i.e. given $2^k$ and $3^\ell$, return $5^{k+\ell}$).

Code:
```5/2 5/3```

## Multiplication

Task: write a program that takes two inputs in registers $2$ and $3$, and multiplies them, placing the result in register $5$ (i.e. given $2^k$ and $3^\ell$, return $5^{k+\ell}$).

Code:
```5/2 5/3```

## Fibonacci

Task: write a one line program that takes one input in registers $23$, and returns the $n$-th Fibonacci number in register $2$.
Note: we multiply the input by a fixed constant $C = 3\cdot13\cdot17 = 663.$

Code:
```455/39 1/13 51/34 51/85 1/17 2/7 221/23```

## Modulo

Task: write a program that takes two inputs in registers $2$ and $3,$ and returns the number in register $2$ modulo the number in register $3$.
