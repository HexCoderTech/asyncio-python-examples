import asyncio
import time


async def make_coffee():
    print("Making coffee")
    # await asyncio.sleep(3)
    print("Coffee is ready")
    return "coffee"


async def make_toast():
    print("Making toast")
    await asyncio.sleep(2)
    print("Toast is ready")
    return "toast"


async def apply_butter():
    print("Applying butter")
    await asyncio.sleep(1)
    print("Butter is applied")
    return "toast with butter"


async def make_eggs():
    print("Making eggs")
    await asyncio.sleep(1)
    print("Eggs are ready")
    return "eggs"


async def main():
    # coffee = await make_coffee() # --> Coroutine
    # print(coffee)
    # taost = await make_toast()
    # print(taost)
    # eggs = await make_eggs()

    # coffee, toast, eggs = await asyncio.gather(
    #     make_coffee(), make_toast(), make_eggs(),
    # )
    # # print(await apply_butter())
    # print(coffee, toast, eggs)

    tasks = []
    async with asyncio.TaskGroup() as tg:
        tasks.append(tg.create_task(make_coffee()))
        tasks.append(tg.create_task(make_eggs()))
        tasks.append(tg.create_task(make_toast()))

    for task in tasks:
        print(task.result())


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f"Time taken: {(end - start):2f}")