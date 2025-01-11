import httpx

from models import Item,TypeItem
from datetime import datetime


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
            data : dict = response.json()

            return Item(id=data["id"],
                        deleted=data.get("delected",False),
                        type_item=TypeItem.Story,
                        by=data.get("by",None),
                        time=datetime.fromtimestamp(data["time"]),
                        text=data.get("text",""),
                        dead=data.get("dead",False),
                        parent=data.get("parent",None),
                        poll=data.get("poll",None),
                        kids=data.get("kids",None),
                        url=data.get("url",None),
                        score=data.get("score",None),
                        title=data.get("title",None),
                        parts=data.get("parts",None),
                        descendants=data.get("descendants",None))


if __name__ == "__main__":
    hn_client = HackerNewsAPI()
    print(hn_client.get_top())
