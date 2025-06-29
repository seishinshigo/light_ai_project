import asyncio

_observer_queue: asyncio.Queue = asyncio.Queue()


class ObserverQueue:
    async def publish(self, payload: dict):
        await _observer_queue.put(payload)

    async def get(self):
        return await _observer_queue.get()
