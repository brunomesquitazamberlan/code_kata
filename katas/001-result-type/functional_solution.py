from typing import Literal, TypeAlias


OkResult: TypeAlias = tuple[Literal["ok"], object]
ErrResult: TypeAlias = tuple[Literal["err"], object]
Result: TypeAlias = OkResult | ErrResult


def ok(value: object) -> Result:
    return ("ok", value)


def err(error: object) -> Result:
    return ("err", error)


def is_ok(result: Result) -> bool:
    tag, _ = result
    return tag == "ok"


def unwrap(result: Result) -> object:
    tag, value = result

    if tag == "ok":
        return value

    raise RuntimeError(f"Cannot unwrap Err: {value}")


def divide(a: float, b: float) -> Result:
    if b == 0:
        return err("Cannot divide by zero")

    return ok(a / b)


if __name__ == "__main__":
    ten_per_two = divide(10, 2)
    print("Can I divide 10 by 2?")
    print("is_ok:", is_ok(ten_per_two))
    print("value:", unwrap(ten_per_two))

    ten_per_zero = divide(10, 0)
    print("Can I divide 10 by 0?")
    print("is_ok:", is_ok(ten_per_zero))

    try:
        unwrap(ten_per_zero)
    except RuntimeError as error:
        print("error:", error)
