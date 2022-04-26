import json, random, string, uuid
from requests import get, post, patch, delete

class DAO:
    """ 
        url: firebase database url
        path: path to data node

        Example:
            firebase_dao = DAO("https://firebase..../", "user_logs")
    """

    def __init__(self, url: str, path: str):
        self.url = url
        self.path = path
    
    def add(self, obj) -> None:
        """
            Example:
            dao.add(json.dumps({
                "username": "user1",
                "password": "super_secret_password"
            }))
        """

        post(f"{self.url}/{self.path}.json", json.dumps(obj))
    
    def get(self) -> dict:
        """
            Example:
            dao.get()

            Returns all the data from firebaseDB into a dict
        """

        return json.loads(get(f"{self.url}/{self.path}.json").text)

    def update(self, id: str, new_data: dict) -> None:
        """
            Example:
            dao.update("-8745h2ha8dfacv2-a", json.dumps({
                "username": "user1",
                "password": "super_secret_password_updated"
            }))
        """

        patch(f"{self.url}/{self.path}/{id}.json", json.dumps(new_data))

    def delete(self, id: str) -> None:
        """
            Example:
            dao.delete("-8745h2ha8dfacv2-a")

            Deletes the user we created in the example
        """
        delete(f"{self.url}/{self.path}/{id}.json")
