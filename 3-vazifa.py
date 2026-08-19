import asyncio

async def ism():
    ism1 = input("ism kiriting: ")

    result = ""
    i = 0
    while i < len(ism1):
        if not ism1[i].isdigit():
            result += ism1[i]
        i += 1
    print(result)
asyncio.run(ism())
























