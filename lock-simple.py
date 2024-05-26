import asyncio

async def task(lock):
    print('Acquiring lock...')
    async with lock:
        print('Lock acquired!')
        # Perform some critical section operations here
        await asyncio.sleep(1)
        print('Lock released!')

async def main():
    # Create a lock
    lock = asyncio.Lock()

    # Create multiple tasks that will compete for the lock
    tasks = [task(lock) for _ in range(5)]

    # Run the tasks concurrently
    await asyncio.gather(*tasks)

# Run the main function
asyncio.run(main())