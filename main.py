import argparse
import json
import sys

from employees.employee import Employee
from readers.reader import CSVReader
from reports.reports import ReportFactory

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
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()