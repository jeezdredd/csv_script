# tests/test_reports.py

import pytest
from reports.reports import PayoutReport, ReportFactory
from employees.employee import Employee

def test_payout_report():
    employees = [
        Employee(1, "a@a", "A", "D", 10, 100),
        Employee(2, "b@b", "B", "D", 20, 50),
    ]
    report = PayoutReport()
    result = report.generate(employees)
    assert result == {
        "payouts": [
            {"id": 1, "name": "A", "department": "D", "payout": 1000.0},
            {"id": 2, "name": "B", "department": "D", "payout": 1000.0},
        ]
    }

def test_payout_report_multiple_departments():
    employees = [
        Employee(1, "a@a", "A", "D1", 10, 100),
        Employee(2, "b@b", "B", "D2", 20, 50),
    ]
    report = PayoutReport()
    result = report.generate(employees)
    assert result == {
        "payouts": [
            {"id": 1, "name": "A", "department": "D1", "payout": 1000.0},
            {"id": 2, "name": "B", "department": "D2", "payout": 1000.0},
        ]
    }

def test_report_factory_unknown_type():
    with pytest.raises(ValueError):
        ReportFactory.create("unknown")