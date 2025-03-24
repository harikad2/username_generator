import random
import string
adjectives = ["Happy", "Cool", "Brave", "Clever", "Mighty", "Fierce", "Jolly"]
nouns = ["Dragon", "Tiger", "Wizard", "Knight", "Phoenix", "Panda", "Wolf"]
def generate_username(add_number=False, add_special=False):
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adj + noun

    if add_number:
        username += str(random.randint(10, 99))  # Add a random number

    if add_special:
        username += random.choice(string.punctuation)  # Add a special character

    return username
def get_user_preferences():
    add_number = input("Include numbers? (yes/no): ").strip().lower() == "yes"
    add_special = input("Include special characters? (yes/no): ").strip().lower() == "yes"
    return add_number, add_special
def save_to_file(username):
    with open("usernames.txt", "a") as file:
        file.write(username + "\n")
def main():
    print("Welcome to the Random Username Generator!")
    
    add_number, add_special = get_user_preferences()
    username = generate_username(add_number, add_special)
    
    print(f"Generated Username: {username}")
    
    save_to_file(username)
    print("Username saved to usernames.txt!")

if __name__ == "__main__":
    main()
