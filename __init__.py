from dao import DAO
from users import User

def main() -> None:
    firebase_dao = DAO("https://loginsystem-2be11-default-rtdb.firebaseio.com", "users")

if __name__ == "__main__":
    main()
