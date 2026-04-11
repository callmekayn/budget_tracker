def show_budget(data):
    print("\n----Xerc-Siyahisi----")
    if not data:
        print("Hələ heç bir xərc yoxdur")
    else:
        for i, xerc in enumerate(data, 1):
            tarix_format = xerc["date"].strftime("%d.%m.%Y %H:%M")
            print(f"{i}. {xerc["ad"]} - {xerc["mebleg"]}AZN - {tarix_format} ")
        print("---------------------------")

def calculate_balance(gelir,data):
    toplam_xerc = sum(xerc["mebleg"] for xerc in data)
    balans = gelir - toplam_xerc
    return balans, toplam_xerc

def reset_budget(data):
    confirmation = input("Butun siyahını temizlemeyi tesdiqleyirsinizmi No/Yes : ")
    if confirmation == "Yes":
        data.clear()
        print("Bütün xərclər silindi. Proqram sıfırlandı.")
    else:
        print("Sıfırlama Ləğv edildi")
