import asyncio

async def s():
    matn = input("Matn: ")

    result1 = ""
    i = 0
    while i < len(matn):
        if matn[i] not in result1:
            result1 += matn[i]
        i += 1
    print(result1)
asyncio.run(s())