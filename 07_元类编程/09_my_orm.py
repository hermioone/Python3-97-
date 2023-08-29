class Field:
    pass


class IntFiled(Field):
    def __init__(self, db_column, min_value: int = None, max_value: int = None):
        if min_value > max_value:
            raise ValueError("min_value must be smaller than max_value")
        self.db_column = db_column
        self.__min_value = min_value
        self.__max_value = max_value
        self.__value = None

    def __get__(self, instance, owner):
        return self.__value

    def __set__(self, instance, value: int):
        if value < self.__min_value or value > self.__max_value:
            raise ValueError("value must be between min_value and max_value")
        self.__value = value


class CharFiled(Field):

    def __init__(self, db_column, max_length: int):
        self.db_column = db_column
        self.__max_length = max_length
        self.__value = None

    def __get__(self, instance, owner):
        return self.__value

    def __set__(self, instance, value):
        if len(value) > self.__max_length:
            raise ValueError("Too long")
        self.__value = value


# 自定义元类，将 Model 中定义的所有字段和 meta 数据（db，table）都放入类的属性中
# 数据库字段都放入 cls._fields 这个字典中；Meta 放入 cls._meta 这个字典中
class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        _fields = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                _fields[key] = value
        meta = attrs.get("Meta", None)
        _meta = {}
        db_name = getattr(meta, "db_name")
        table_name = getattr(meta, "table_name")
        _meta["db"] = db_name
        _meta["table"] = table_name
        attrs["_meta"] = _meta
        attrs["_fields"] = _fields
        del attrs["Meta"]
        return super().__new__(cls, name, bases, attrs, **kwargs)


class ModelBase():

    def save(self):
        """
        保存到数据库
        """
        db = self._meta["db"]
        table = self._meta["table"]

        columns = []
        values = []
        for key, value in self._fields.items():
            columns.append(value.db_column)
            values.append(str(getattr(self, key)))
        columns_str = ','.join(columns)
        values_str = ','.join(values)

        sql = f"insert into {db}.{table}({columns_str}) value({values_str})"
        print(sql)


class User(ModelBase, metaclass=ModelMetaClass):

    name = CharFiled(db_column="name", max_length=10)
    age = IntFiled(db_column="age", min_value=0, max_value=100)

    class Meta:
        db_name = "demo"
        table_name = "user"


if __name__ == "__main__":
    user = User()
    user.name = "hermione"
    user.age = 16
    user.save()
