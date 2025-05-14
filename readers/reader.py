from typing import List, Dict
from employees.employee import Employee

class CSVReader:
    @staticmethod
    def read(file_path: str) -> List[Employee]:
        with open(file_path, encoding="utf-8") as f:
            lines = f.readlines()
        header = [h.strip() for h in lines[0].strip().split(",")]
        data = []
        for line in lines[1:]:
            values = [v.strip() for v in line.strip().split(",")]
            row = dict(zip(header, values))
            data.append(CSVReader._row_to_employee(row))
        return data

    @staticmethod
    def _row_to_employee(row: Dict[str, str]) -> Employee:
        rate_key = next((k for k in row if k in ("hourly_rate", "rate", "salary")), None)
        if not rate_key:
            raise ValueError("Не найдена колонка с оплатой (hourly_rate, rate, salary)")
        return Employee(
            id=int(row["id"]),
            email=row["email"],
            name=row["name"],
            department=row["department"],
            hours_worked=float(row["hours_worked"]),
            hourly_rate=float(row[rate_key])
        )