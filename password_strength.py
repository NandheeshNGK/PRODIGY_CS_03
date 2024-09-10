#PRODIGY_CS_03
#TASK 03


import re

def assess_password_strength(password):
    # Define criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[@#$%^&+=]', password) is not None
    
    # Assess strength based on criteria
    strength = 0
    if length_criteria:
        strength += 1
    if uppercase_criteria:
        strength += 1
    if lowercase_criteria:
        strength += 1
    if number_criteria:
        strength += 1
    if special_char_criteria:
        strength += 1
    
    # Provide feedback
    if strength == 5:
        return "Strong password: Meets all criteria."
    elif strength == 4:
        return "Good password: Meets most criteria."
    elif strength == 3:
        return "Average password: Meets some criteria. Consider adding more complexity."
    elif strength == 2:
        return "Weak password: Missing several criteria. Consider making improvements."
    else:
        return "Very weak password: Fails to meet basic criteria. Please choose a stronger password."

def main():
    print("Password Strength Assessment Tool")
    password = input("Enter your password to assess its strength: ")
    feedback = assess_password_strength(password)
    print(feedback)

if __name__ == "__main__":
    main()
