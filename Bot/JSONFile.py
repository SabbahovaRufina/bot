import json
from typing import List


class JSONFile:
    def __init__(self):
        self.path = "users.json"

    async def open_load(self):
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data

    async def open_dump(self, data):
        with open(self.path, "w", encoding="utf-8") as outfile:
            json.dump(data, outfile, indent=4, ensure_ascii=False)

    async def get_new_data(self, message_id, n):
        data = await self.open_load()
        for i, x in enumerate(data):
            if message_id == x["chat_id"]:
                new_data = data[i]
                del data[i]
                new_data["working_bool"] = n
                data.append(new_data)
                break
        await self.open_dump(data)

    async def get_all_users(self) -> List[int]:
        data = await self.open_load()
        return [x["chat_id"] for x in data]

    async def get_work_users(self) -> List[int]:
        data = await self.open_load()
        return [x["chat_id"] for x in data if x["working_bool"]]

