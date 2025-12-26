def hello(name: str = "World") -> str:
    """
    Say hello to someone.
    
    Args:
        name (str): Name to greet. Defaults to "World".
    
    Returns:
        str: Greeting message.
    
    Examples:
        >>> hello()
        'Hello, World!'
        >>> hello("Alice")
        'Hello, Alice!'
    """
    return f"Hello, {name}!"


def goodbye(name: str = "World") -> str:
    """
    Say goodbye to someone.
    
    Args:
        name (str): Name to say goodbye to. Defaults to "World".
    
    Returns:
        str: Goodbye message.
    
    Examples:
        >>> goodbye()
        'Goodbye, World!'
        >>> goodbye("Bob")
        'Goodbye, Bob!'
    """
    return f"Goodbye, {name}!"


# Пример использования
if __name__ == "__main__":
    print(hello())
    print(hello("Python Developer"))