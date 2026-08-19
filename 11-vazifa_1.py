import asyncio

async def a():
    parol = str(input("Parol kiriting: "))

    result = ""
    i = 0
    while i < len(parol):
        if not parol[i].isdigit():
            result += parol[i]
        i += 1
    print(result)
asyncio.run(a())

































