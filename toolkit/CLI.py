import argparse
from toolkit.calc import calculate, sort_station
from toolkit.values import translate


def main():
    parser = argparse.ArgumentParser(
        prog="toolkit",
        description="Утилиты: калькулятор и конвертер единиц"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    CALC_parser = subparsers.add_parser("calc=", help="вычеслить")
    calc_parser = subparsers.add_parser("calc", help="перевести выражение в постфикмсный вид")
    calc_parser.add_argument("expression", type=str, help="мат выражение")
    CALC_parser.add_argument("expression", type=str, help="мат выражение")

    conv_parser = subparsers.add_parser("convert", help="конвертация единиц")
    conv_parser.add_argument("value", type=str, help="число")
    conv_parser.add_argument("--to", default='st', dest="to_unit", required=False, help="в какую ед. переводим")
    conv_parser.add_argument("--from", default='', dest="from_unit", required=False, help="из какой ед. измерения переводим")

    args = parser.parse_args()

    try:
        if args.command == "calc":
            result = sort_station(args.expression)
            print(' '.join(map(str, result)))

        elif args.command == "calc=":
            result = calculate(args.expression)
            print(result)

    except ZeroDivisionError:
        print("Попытка деления на ноль")
    except (ValueError, TypeError):
        print("Неправильный ввод")
    except Exception as e:
        print(f"Ошибка: {e}")

    if args.command == "convert":
        result = translate(args.value+args.from_unit, args.to_unit)
        print(result)