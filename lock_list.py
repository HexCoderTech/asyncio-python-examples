import asyncio

async def append_to_list(lock, my_list, item):
    async with lock:
        my_list.append(item)
        print(f"Item {item} appended to the list")

async def main():
    my_list = []
    lock = asyncio.Lock()

    tasks = []
    for i in range(5):
        task = asyncio.create_task(append_to_list(lock, my_list, i))
        tasks.append(task)

    await asyncio.gather(*tasks)

    print("Final list:", my_list)

if __name__ == "__main__":
    asyncio.run(main())