class Company:
    def __init__(self, employee_list) -> None:
        self.employee = employee_list

    def __str__(self) -> str:
        return "-> " + ", ".join(self.employee) + " <-"
    
    def __repr__(self) -> str:
        return "[ " + ", ".join(self.employee) + " ]"


company = Company(['harry', 'hermione', 'ron'])
# 调用 __str__ 魔法函数
print(company)                                  # -> harry, hermione, ron <-
print(str(company))                             # -> harry, hermione, ron <-
# 调用 __repr__ 魔法函数
print(repr(company))                            # [ harry, hermione, ron ]