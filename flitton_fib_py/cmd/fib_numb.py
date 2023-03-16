import argparse

from flitton_fib_py import recurring_fibonacci_number

def fib_numb() -> None:
    parser = argparse.ArgumentPraser(
        description='Calculate Fibonacci numbers'
    )

    parser.add_argument('--number', action='store', type=int, require=True, help="Fibanocci number to be calculated")

    arg = parser.parse_args()
    print(f"Your fibonacci number is: " f"{recurring_fibonacci_number(number=arg.number)}")
