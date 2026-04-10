from functions import show_budget,calculate_balance
#Developed by Kenan Abbaszade
def main():

    gelir = 1000
    xercler = []

    print("--- Budget Tracker v1.0 ---")
    while True:
        print("\n=== Budget Planner ===")
        print("1. Xerc daxil edin")
        print("2. Xercleri göstərin")
        print("3. Balansı yoxla")
        print("4. Çıxış")

        secim = input("\nSeciminizi edin 1-4 : ")

        if secim == "1":
            ad = input("Xercin adi : ")
            try:
                mebleg = float(input("Meblegi : "))
                xercler.append({"ad":ad,"mebleg":mebleg})
                print("Ugurla elave edildi!")
            except ValueError:
                print("Səhv: Zəhmət olmasa rəqəm daxil edin.")
        elif secim == "2":
            show_budget(xercler)
        elif secim == "3":
            balans,toplam = calculate_balance(gelir,xercler)
            print(f"\nÜmumi Gəlir: {gelir} AZN")
            print(f"Toplam Xərc: {toplam} AZN")
            print(f"Cari Balans: {balans} AZN")
        elif secim == "4":
            print("Programdan cixilir sagolun!")
            break
        else:
            print("Səhv seçim! Yenidən yoxlayın.")


if __name__ == "__main__":
    main()