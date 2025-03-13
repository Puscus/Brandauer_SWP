def print_message(message):
    """Gibt die übergebene Nachricht aus."""
    print(f"Message: {message}")

def process_args(*args):
    """Verarbeitet und gibt die Positionsargumente aus."""
    if args:
        print("Args:", args)
        print("Sum of args:", sum(args))  # Falls args numerisch sind

def process_kwargs(**kwargs):
    """Verarbeitet und gibt die benannten Argumente aus."""
    if kwargs:
        print("Kwargs:", kwargs)
        if 'name' in kwargs:
            print(f"Hello, {kwargs['name']}!")

def inner_function(*args, **kwargs):
    print("Inner function is called!")
    process_args(*args)
    process_kwargs(**kwargs)

def outer_function(message, *args, **kwargs):
    """Hauptmethode, die alle Teilmethoden aufruft."""
    print_message(message)
    process_args(*args)
    process_kwargs(**kwargs)
    def inner_function(*args, **kwargs):
     print("Inner function is called!")
     process_args(*args)
     process_kwargs(**kwargs)
    inner_function(*args, **kwargs)

# Beispielaufruf mit verschiedenen Parametern
outer_function("Demo-Aufruf", 1, 2, 3, name="Alice", age=30)
