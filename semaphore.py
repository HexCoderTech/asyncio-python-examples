import asyncio

async def worker(semaphore):
    async with semaphore:
        print("Worker acquired the semaphore")
        await asyncio.sleep(1)
        print("Worker released the semaphore")

async def main():
    # Create a semaphore with a maximum of 2 concurrent workers
    semaphore = asyncio.Semaphore(1)

    # Create a list of worker tasks
    tasks = [worker(semaphore) for _ in range(5)]

    # Run the worker tasks concurrently
    await asyncio.gather(*tasks)

# Run the main function
asyncio.run(main())