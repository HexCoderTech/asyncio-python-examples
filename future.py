import asyncio

async def my_coroutine(future):
    await asyncio.sleep(1)
    future.set_result('Hello, future!')
    await asyncio.sleep(3)
    return 'Hello, return!'
    

async def main():
    loop = asyncio.get_event_loop()
    # Create a future object
    future = loop.create_future()

    # Schedule the coroutine to run and set the result of the future
    t = asyncio.create_task(my_coroutine(future))

    # Wait for the future to complete and get the result
    result = await future
    print(result)
    print(await t)

# Run the main function
asyncio.run(main())