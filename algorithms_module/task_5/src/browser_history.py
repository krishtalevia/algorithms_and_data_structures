from __future__ import annotations
from datetime import datetime

class HistoryItem:

    def __init__(self, url: str, timestamp: datetime):
        self.__url = url
        self.__timestamp = timestamp

class Node:

    def __init__(self, history_item: HistoryItem):
        self.history_item = history_item
        self.next = None

class BrowserHistory:

    def __init__(self, history_stack: list[HistoryItem], current_index: int):
        self.__history_stack = []
        self.__current_index = current_index

    def visit(self, url: str, timestamp: datetime):
        history_item = HistoryItem(url, datetime.now())