import asyncio

async def katta():
    matn = input("Matn kiriting: ")

    result = ""
    i = 0

    while i < len(matn):
        if matn[i] != " ":
            result += matn[i].lower()
        i += 1
    print(result)

asyncio.run(katta())

























