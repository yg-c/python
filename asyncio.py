async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)  # getting data from server
    print('done fetching')
    return {'data': 1}


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)


async def main():
    task1 = asyncio.create_task(fetch_data())  # we start task 1
    task2 = asyncio.create_task(print_numbers())  # we start taskt 2

    value = await task1  # we wait task1 to finish running
    print(value)
    await task2  # we wait for task2 to finish running


# because we have a delay (sleep) in fetch_data(), print_number() can start running.
# During the print_number() delay the program look if he can give the execution back to other task

asyncio.run(main())  # entry point