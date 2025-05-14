# tests/test_reader.py

import pytest
from readers.reader import CSVReader
from employees.employee import Employee

def test_read(tmp_path):
    content = (
        "id,email,name,department,hours_worked,salary\n"
        "1,alice@example.com,Alice,Marketing,160,50\n"
    )
    file = tmp_path / "tests.csv"
    file.write_text(content, encoding="utf-8")
    employees = CSVReader.read(str(file))
    assert len(employees) == 1
    assert employees[0] == Employee(
        id=1,
        email="alice@example.com",
        name="Alice",
        department="Marketing",
        hours_worked=160.0,
        hourly_rate=50.0
    )

def test_read_with_rate_column(tmp_path):
    content = (
        "id,email,name,department,hours_worked,rate\n"
        "2,bob@example.com,Bob,Design,150,40\n"
    )
    file = tmp_path / "test2.csv"
    file.write_text(content, encoding="utf-8")
    employees = CSVReader.read(str(file))
    assert employees[0].hourly_rate == 40.0

def test_read_with_hourly_rate_column(tmp_path):
    content = (
        "id,email,name,department,hours_worked,hourly_rate\n"
        "3,carol@example.com,Carol,Design,170,60\n"
    )
    file = tmp_path / "test3.csv"
    file.write_text(content, encoding="utf-8")
    employees = CSVReader.read(str(file))
    assert employees[0].hourly_rate == 60.0

def test_read_missing_rate_column(tmp_path):
    content = (
        "id,email,name,department,hours_worked\n"
        "4,dave@example.com,Dave,Sales,100\n"
    )
    file = tmp_path / "test4.csv"
    file.write_text(content, encoding="utf-8")
    with pytest.raises(ValueError):
        CSVReader.read(str(file))