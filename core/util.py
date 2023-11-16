class DbModelToDictMixin:
    # Function to convert to dict
    def dict(self):
        from sqlalchemy import inspect
        mapper = inspect(self.__class__)
        columns = [column.key for column in mapper.columns]
        return {column: getattr(self, column) for column in columns}

def get_rows_from_csv(csv_path):
    import csv
    from pathlib import Path
    rows: list[dict] = []
    csv_path = Path(csv_path)
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows