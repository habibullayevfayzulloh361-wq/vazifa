import asyncio

async def unli():
    soz = input("So'z: ")

    unlilar = "aeiou"
    i = 0
    faqat_unli = True
    while i < len(soz):
        if soz[i].lower() not in unlilar:
            faqat_unli = False
            break
        i += 1

    if faqat_unli:
        print(soz.upper())
    else:
        print("So'z faqat unlilardan iborat emas")
asyncio.run(unli())