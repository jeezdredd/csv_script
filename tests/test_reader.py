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