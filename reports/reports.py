from typing import List, Dict, Any
from employees.employee import Employee

class Report:
    def generate(self, employees: List[Employee]) -> Any:
        raise NotImplementedError

class PayoutReport(Report):
    def generate(self, employees: List[Employee]) -> Dict[str, list]:
        payouts = []
        for emp in employees:
            payouts.append({
                "id": emp.id,
                "name": emp.name,
                "department": emp.department,
                "payout": round(emp.hours_worked * emp.hourly_rate, 2)
            })
        return {"payouts": payouts}

class ReportFactory:
    _reports = {
        "payout": PayoutReport,
    }

    @classmethod
    def create(cls, report_type: str) -> Report:
        if report_type not in cls._reports:
            raise ValueError(f"Неизвестный тип отчета: {report_type}")
        return cls._reports[report_type]()