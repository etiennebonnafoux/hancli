from dataclasses import dataclass
from datetime import date
from enum import Enum


class TypeItem(Enum):
    Job = 1
    Story = 2
    Comment = 3
    poll = 4
    pollopt = 5


@dataclass
class Item:
    id: int
    deleted: bool  # true if the item is deleted.
    type_item: (
        str  # The type of item. One of "job", "story", "comment", "poll", or "pollopt".
    )
    by: str  # The username of the item's author.
    time: date  # Creation date of the item, in Unix Time.
    text: str  # The comment, story or poll text. HTML.
    dead: bool  # true if the item is dead.
    parent: int  # The comment's parent: either another comment or the relevant story.
    poll: str  # The pollopt's associated poll.
    kids: list[int]  # The ids of the item's comments, in ranked display order.
    url: str  # The URL of the story.
    score: int  # The story's score, or the votes for a pollopt.
    title: str  # The title of the story, poll or job. HTML.
    parts: list[str]  # A list of related pollopts, in display order.
    descendants: int  # In the case of stories or polls, the total comment count.
