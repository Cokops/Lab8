def test_add():

    result = add(2, 3)
    assert result == 5, f"Ошибка: 2+3 должно быть 5, а получилось {result}"
    print("✓test_add прошел!")


def test_multiply():
    result = multiply(4, 5)
    assert result == 20, f"Ошибка: 4×5 должно быть 20, а получилось {result}"
    print("test_multiply прошел!")


def add(a, b):
    return a + b  


def multiply(a, b):
    return a * b  


if __name__ == "__main__":
    print("Запускаем TDD-тесты калькулятора...")
    
    try:
        test_add()
    except Exception as e:
        print(f"test_add упал: {e}")
    
    try:
        test_multiply()
    except Exception as e:
        print(f"test_multiply упал: {e}")
    
    print("\nГотово! Добавьте новые тесты и функции.")