from typing import List, TypedDict


class Task(TypedDict):
    id: int
    description: str
    completed: bool


TaskList = List[Task]
