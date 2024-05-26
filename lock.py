import asyncio
import time

order_price = 0
lock = asyncio.Lock()

async def make_coffee():
    global order_price
    print("Making coffee")
    # await asyncio.sleep(3)
    async with lock:
        print("changing price for coffee")
        order_price += 2
        await asyncio.sleep(2)
    print("Coffee is ready")
    return "coffee"


async def make_toast():
    global order_price
    print("Making toast")
    # await asyncio.sleep(2)
    async with lock:
        print("changing price for toast")
        order_price += 1
        await asyncio.sleep(1)
    print("Toast is ready")
    return "toast"


async def apply_butter():
    global order_price
    print("Applying butter")
    # await asyncio.sleep(1)
    async with lock:
        print("changing price for butter")
        order_price -= 20
        await asyncio.sleep(1)
    print("Butter is applied")
    return "toast with butter"


async def make_eggs():
    global order_price
    print("Making eggs")
    # await asyncio.sleep(1)
    async with lock:
        print("changing price for eggs")
        order_price += 18
        await asyncio.sleep(2)
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

    print(f"Total price: {order_price}")

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f"Time taken: {(end - start):2f}")