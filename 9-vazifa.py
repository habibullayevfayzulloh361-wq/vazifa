import asyncio

async def kichik():
    ism = input("Ism: ")

    if ism.lower():
        print(ism.lower())
    else:
        print(ism)
asyncio.run(kichik())
