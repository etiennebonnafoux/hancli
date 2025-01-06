import httpx


class HackerNewsAPI:
    def __init__(self):
        self.base_url = "https://hacker-news.firebaseio.com"

    def get_top(self, limit: int = 10) -> list[int]:
        """Load the ids of the top stories

        Args:
            limit (int, optional): The number of wanted stories. Defaults to 10.

        Returns:
            list[int]: _description_
        """
        with httpx.Client() as client:
            response = client.get(f"{self.base_url}/v0/topstories.json")
            return response.json()[:limit]

    def get_item(self, id: int):
        with httpx.Client() as client:
            response = client.get(f"{self.base_url}/v0/item/{id}.json")
            return response.json()


if __name__ == "__main__":
    hn_client = HackerNewsAPI()
    print(hn_client.get_top())
