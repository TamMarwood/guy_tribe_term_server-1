class DbModelToDictMixin:
    # Function to convert to dict
    def dict(self):
        from sqlalchemy import inspect
        mapper = inspect(self.__class__)
        columns = [column.key for column in mapper.columns]
        return {column: getattr(self, column) for column in columns}