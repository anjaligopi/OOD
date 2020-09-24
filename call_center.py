# consider all nouns in the problem as candidates for class
# verbs -> methods
# is a relationship -> B inherits from A
# has a -> member variable of the class

# %%
from typing import List
from enum import Enum
import random

class EscalateCallException(Exception):
    pass

class EmpLevel(Enum):
    RESPONDENT = 0
    MANAGER = 1
    DIRECTOR = 2


class IncomingCall:
    def __init__(self) -> None:
        self.call_id: int = random.randint(0,10000)
        self.rank = EmpLevel.RESPONDENT
        self.handled = False

    def escalate(self):
        assert self.rank < EmpLevel.DIRECTOR
        self.rank += 1


class CallCenter:
    def __init__(self) -> None:
        self.respondents: List[Respondent] = []
        self.managers: List[Manager] = []
        self.directors: List[Director] = []

    def _get_first_available_employee_of_level(self, level:EmpLevel) -> Employee:
        for emp in self.respondents + self.managers + self.directors:
            if emp._free and emp.level == level:
                return emp   

    def dispatch_call(self, inc_call: IncomingCall):
        while not inc_call.handled:
            first_avail_emp = self._get_first_available_employee_of_level(inc_call.rank)
            assert first_avail_emp is not None
            try:
                first_avail_emp.handle_call(inc_call)
                inc_call.handled = True
            except EscalateCallException:
                inc_call.escalate()


class Employee:
    def __init__(self) -> None:
        self.level: EmpLevel = EmpLevel.RESPONDENT  # default level
        # use underscore if you need to restrict access to parent and child classes only.
        self._free: bool = True
        self._emp_id: int = random.randint(0,1000)

    def handle_call(self, inc_call: IncomingCall):
        self._free = False
        print(
            f"Emp ID: {self._emp_id} is handling the call ID : {self.inc_call.call_id}"
        )


class Respondent(Employee):
    def __init__(self) -> None:
        # to get the value of _free from Employee (parent class)
        super().__init__()
        self.level: EmpLevel = EmpLevel.RESPONDENT


class Manager(Employee):
    def __init__(self) -> None:
        super().__init__()
        self.level: EmpLevel = EmpLevel.MANAGER


class Director(Employee):
    def __init__(self) -> None:
        super().__init__()
        self.level: EmpLevel = EmpLevel.DIRECTOR


emp = Respondent()
print(emp._free)
# %%
