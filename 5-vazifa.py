import asyncio

async def unli():
    matn = input("matn kiriting: ")

    i = 0
    while i < len(matn):
        if matn[i].lower() in "aeiouAEIOU":
            print(matn[i], end="")
        i += 1
asyncio.run(unli())























