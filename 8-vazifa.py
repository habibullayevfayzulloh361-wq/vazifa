import asyncio

async def soz1():
    soz = input("So'z: ")

    orta = len(soz) // 2

    result = ""
    i = 0
    while i < len(soz):
        if i != orta:
            result += soz[i]
        i += 1
    print(result)
asyncio.run(soz1())