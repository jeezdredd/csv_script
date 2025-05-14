import argparse
import json
import sys
from collections import defaultdict

from tabulate import tabulate

from readers.reader import CSVReader
from reports.reports import ReportFactory


def print_grouped_payouts(payouts):
    grouped = defaultdict(list)
    for row in payouts:
        grouped[row["department"]].append(row)
    for dept, rows in grouped.items():
        print(f"\nОтдел: {dept}")
        print(tabulate(
            rows,
            headers={"id": "ID", "name": "Имя", "payout": "Выплата"},
            tablefmt="fancy_grid",
            stralign="center",
            numalign="center"
        ))


def main():
    parser = argparse.ArgumentParser(description="Генератор отчетов по сотрудникам")
    parser.add_argument("files", nargs="+", help="Пути к CSV-файлам с данными сотрудников")
    parser.add_argument("--report", required=True, help="Тип отчета (например, payout)")
    args = parser.parse_args()

    employees = []
    for file_path in args.files:
        try:
            employees.extend(CSVReader.read(file_path))
        except Exception as e:
            print(f"Ошибка при чтении файла {file_path}: {e}", file=sys.stderr)
            sys.exit(1)

    try:
        report = ReportFactory.create(args.report)
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)

    result = report.generate(employees)
    if "payouts" in result:
        print_grouped_payouts(result["payouts"])
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
