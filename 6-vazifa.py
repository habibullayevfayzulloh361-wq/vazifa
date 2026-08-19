import asyncio

async def a_b():
    soz = input("So'z kiriting: ")

    result = ""
    i = 0
    while i < len(soz):
        if i + 1 < len(soz) and soz[i] == "a" and soz[i + 1] == "b":
            result += "#"
            i += 2
        else:
            result += soz[i]
            i += 1
    print(result)

asyncio.run(a_b())






















