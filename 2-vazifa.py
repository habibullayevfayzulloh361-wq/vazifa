import asyncio

async def m():
    matn = input("matn kiriitng: ")

    if len(matn) > 10:
        i = 0
        while i < 10:
            print(matn[i], end="")
            i += 1
    else:
        print(matn)


asyncio.run(m())
