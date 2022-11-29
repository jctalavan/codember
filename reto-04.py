def get_passwords(min_limit, max_limit) -> list:

    iterator_number = min_limit
    passwords_with_at_least_two_fives = list()

    # - It's a 5-digit password.
    # - The password has the number 5 repeated at least two times.
    while iterator_number <= max_limit:
        number_of_fives = 0
        for digit in str(iterator_number):
            if digit == '5':
                number_of_fives += 1

        if number_of_fives >= 2:
            passwords_with_at_least_two_fives.append(str(iterator_number))

        iterator_number += 1

    # - The number to the right is always greater than or equal to the one on the left.
    possible_passwords = list()
    for password in passwords_with_at_least_two_fives:
        i = 0
        j = 1
        correct_password = True
        while correct_password and j < len(password):
            digit_left = int(password[i])
            digit_right = int(password[j])
            if digit_right < digit_left:
                correct_password = False

            i+=1
            j+=1
        
        if correct_password:
            possible_passwords.append(password)

    return possible_passwords

if __name__ == "__main__":
    min_limit = 11098
    max_limit = 98123

    possible_passwords = get_passwords(min_limit, max_limit)

    print(f"{len(possible_passwords)}-{possible_passwords[55]}")
