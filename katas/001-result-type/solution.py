from typing import Protocol, TypeVar

# Abstraction

T = TypeVar("T")
E = TypeVar("E")

class Result(Protocol[T, E]):
    def is_ok(self):
        pass

    def unwrap(self):
        pass


class Ok():
    def __init__(self, input_value):
        self.value = input_value

    def is_ok(self):
        return True 

    def unwrap(self):
        return self.value

class Err():
    def __init__(self, input_value):
        self.value = input_value

    def is_ok(self):
        return False

    def unwrap(self):
        exception_message = f"Cannot unwrap Err: {self.value}"
        raise RuntimeError(exception_message)



# Implementation

def divide (a: float, b: float) -> Result[float, str]:
    if b == 0:
        result = Err("Cannot divide by zero")
        return result 
    else:
        result = Ok(a/b)
        return result

if __name__ == "__main__":
    ten_per_two = divide(10, 2)
    print("Can I divide 10 by 2?")
    print("is_ok:", ten_per_two.is_ok())
    print("value:", ten_per_two.unwrap())
    assert ten_per_two.is_ok() is True
    assert ten_per_two.unwrap() == 5.0

    ten_per_zero = divide(10, 0)
    print("Can I divide 10 by 0?")
    print("is_ok:", ten_per_zero.is_ok())
    assert ten_per_zero.is_ok() is False

    try:
        ten_per_zero.unwrap()
    except RuntimeError as error:
        print("error:", error)
    else:
        raise AssertionError("Expected RuntimeError")
