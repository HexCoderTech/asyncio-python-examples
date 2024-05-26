import asyncio

async def worker(event):
    print("Worker is waiting...")
    await event.wait()
    # TODO : conditions
    print("Worker is done!")

async def main():
    # Create an event
    print("Creating an event")
    event = asyncio.Event()

    # Start the worker task
    print("Starting the worker task")
    task = asyncio.create_task(worker(event))

    # Sleep for 2 seconds
    await asyncio.sleep(2)

    # Set the event
    print("Setting the event")
    event.set()

    # Wait for the worker task to complete
    print("Waiting for the worker task to complete")
    await task

asyncio.run(main())