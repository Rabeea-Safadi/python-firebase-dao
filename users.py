from dataclasses import dataclass

@dataclass
class User:
    username: str
    password: str

    def to_dict(self) -> dict:
        return {
            "username": self.username,
            "password": self.password
        }
