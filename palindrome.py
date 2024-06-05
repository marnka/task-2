import sys
import re

def is_palindrome(s):

    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    # Видаляємо всі пробіли і перетворюємо рядок у нижній регістр
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    # Перевіряємо, чи дорівнює рядок своєму зворотному вигляду
    return s == s[::-1]

def main():

    try:
        input_str = sys.stdin.readline().strip()

        if not input_str:
            raise ValueError("Input cannot be empty") 

        if is_palindrome(input_str):
            print(True)
            sys.exit(0)
            
        else:
            print(False)
            sys.exit(0)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
