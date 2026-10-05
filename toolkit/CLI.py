import argparse
from toolkit.calc import calculate
from toolkit.values import translate

def main():
    parser = argparse.ArgumentParser(
        prog="toolkit",
        description="Утилиты: калькулятор и конвертер единиц"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- calc ---
    calc_parser = subparsers.add_parser("calc", help="Вычислить выражение")
    calc_parser.add_argument("expression", type=str, help="Математическое выражение")

    # --- convert ---
    conv_parser = subparsers.add_parser("convert", help="Конвертация единиц")
    conv_parser.add_argument("value", type=float, help="Число")
    conv_parser.add_argument("--from", dest="from_unit", required=True, help="Исходная единица")
    conv_parser.add_argument("--to", dest="to_unit", required=True, help="Целевая единица")

    args = parser.parse_args()

    if args.command == "calc":
        result = calculate(args.expression)
        print(result)

    elif args.command == "convert":
        result = translate(args.value, args.from_unit, args.to_unit)
        print(result)