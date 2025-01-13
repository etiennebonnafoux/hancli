import httpx

from models import Item,ItemType,StoryType
from datetime import datetime


class HackerNewsAPI:
    def __init__(self):
        self.base_url = "https://hacker-news.firebaseio.com"


    def get_stories(self,story_type: StoryType, limit =10 ) -> list[int]:
        """
        Load the ids of the stories

        Args:
            limit (int, optional): The number of the stories. Default to 10
            story_type (StoryType): the type of story to get

        Returns:
            list[int]: the ids of the ask
        """
        with httpx.Client() as client:
            response = client.get(f"{self.base_url}/v0/{story_type.value}.json")
            return response.json()[:limit]

    def get_item(self, id: int):
        with httpx.Client() as client:
            response = client.get(f"{self.base_url}/v0/item/{id}.json")
            data : dict = response.json()

            return Item(id=data["id"],
                        deleted=data.get("delected",False),
                        type_item=ItemType.Story,
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
    print(hn_client.get_stories())
