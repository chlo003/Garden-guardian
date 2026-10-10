def garden_operations(operation_number: int) -> None:
    data = 2
    if operation_number == 0:
        data = int("abc")
    elif operation_number == 1:
        data = data / 0
        raise ZeroDivisionError
    elif operation_number == 2:
        data = open("/non/existent/file", "r")
        raise FileNotFoundError
    elif operation_number == 3:
        data = "string" + 7
        raise TypeError
    else:
        return


def test_error_types() -> None:
    print("Testing operation 0...")
    try:
        garden_operations(0)
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    print("Testing operation 1...")
    try:
        garden_operations(1)
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    print("Testing operation 2...")
    try:
        garden_operations(2)
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    print("Testing operation 3...")
    try:
        garden_operations(3)
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    print("Testing operation 4...")
    print("Operation completed successfully")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print()
    print("All error types tested succesfully!")
