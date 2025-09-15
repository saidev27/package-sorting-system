def sort(width, height, length, mass):
    
    volume = width * height * length
    
    is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    
    is_heavy = mass >= 20
    
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

def main():
    
    test_cases = [
        (100, 50, 30, 10),      # STANDARD
        (200, 40, 20, 10),      # SPECIAL
        (120, 85, 98, 22),      # SPECIAL
        (160, 160, 200, 25),    # REJECTED
        (80, 80, 160, 19.5),    # SPECIAL
        (100, 100, 100, 30),    # SPECIAL
        (180, 10, 10, 25),      # REJECTED
    ]
    print("W(cm) H(cm) L(cm) Mass(kg) -> Stack")
    print("-" * 40)
    for width, height, length, mass in test_cases:
        stack = sort(width, height, length, mass)
        print(f"{width:<5} {height:<5} {length:<6} {mass:<8} -> {stack}")

if __name__ == '__main__':
    main()
