import asyncio

async def teskari():
    matn = input("Raqamli matn: ")

    i = 0
    raqam = True
    while i < len(matn):
        if not matn[i].isdigit():
            raqam = False
            break
        i += 1

    if raqam:
        i = len(matn) - 1
        while i >= 0:
            print(matn[i], end="")
            i -= 1
    else:
        print("Barcha belgilar raqam emas")
asyncio.run(teskari())


















