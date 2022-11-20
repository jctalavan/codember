import requests

def process_response_content(lines):
    users = list()
    current_user_data = ""

    for line in lines:
        if (line == ""):
            users.append(current_user_data)
            current_user_data = ""
        else:
            current_user_data += f" {line}"

    return users

def filter_valid_users(users):
    valid_users = list()
    for user in users:
        if (check_valid_user(user)):
            valid_users.append(user)

    return valid_users

def check_valid_user(user) -> bool:
    required_info_for_valid_user = get_required_info_for_valid_user()

    user_data = user.split(' ')
    for current_data in user_data:
        current_data_parts = current_data.split(":")
        if (len(current_data_parts) != 2):
            continue
        current_data_key = current_data_parts[0]
        if (current_data_key in required_info_for_valid_user):
            required_info_for_valid_user[current_data_key] = True

    return all(required_info_for_valid_user.values())

def get_required_info_for_valid_user() -> dict:
    return {
        'usr': False,
        'eme': False,
        'psw': False,
        'age': False,
        'loc': False,
        'fll': False,
    }

def get_user_name(user) -> str:
    user_name = ""
    user_data = user.split(' ')
    for current_data in user_data:
        current_data_parts = current_data.split(":")
        if (len(current_data_parts) != 2):
            continue
        if (current_data_parts[0] == "usr"):
            user_name = current_data_parts[1]
    
    return user_name

response = requests.get('https://codember.dev/users.txt')
lines = response.text.split('\n')

if __name__ == "__main__":
    users = process_response_content(lines)
    valid_users = filter_valid_users(users)

    #Number of correct users and last user name
    valid_users_count = len(valid_users)
    last_valid_user = valid_users[-1]
    last_valid_user_name = get_user_name(last_valid_user)

    print(f"{valid_users_count}{last_valid_user_name}")
