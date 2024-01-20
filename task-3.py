def password_strength(password):
    length = len(password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special_char = any(not char.isalnum() for char in password)

    strength = 0
    if length >= 8:
        strength += 1
    if has_uppercase and has_lowercase:
        strength += 1
    if has_digit:
        strength += 1
    if has_special_char:
        strength += 1

    if strength <= 2:
        return "Weak"
    elif strength == 3:
        return "Moderate"
    else:
        return "Strong"

password = input("Enter your password: ")
print(" Feedback : Your password strength is", password_strength(password))
