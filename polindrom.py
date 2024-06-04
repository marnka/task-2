import sys

def is_palindrome(s):
    # Видаляємо всі пробіли і перетворюємо рядок у нижній регістр
    s = s.replace(" ", "").lower()
    # Перевіряємо, чи дорівнює рядок своєму зворотному вигляду
    return s == s[::-1]

def main():
    try:
        input_str = input().strip()
        if is_palindrome(input_str):
            print(True)
            return 0
        else:
            print(False)
            return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
