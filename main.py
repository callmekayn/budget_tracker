from functions import show_budget,calculate_balance
#Developed by Kenan Abbaszade
def main():

    gelir = 1000
    xercler = []

    print("--- Budget Tracker v1.0 ---")
    while True:
        print("\n=== Budget Planner ===")
        print("1. Xerc daxil edin")
        print("2. Kommunal Ödənişlər")
        print("3. Xercleri göstərin")
        print("4. Balansı yoxla")
        print("5. Çıxış")

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
            try:
                kommunal = input("Kommunal daxil edin: ")
                xercler.append({"kommunal":kommunal})
                print("Ayliq Kommunal xərci uğurla daxil edildi!")
            except ValueError:
                print("Error: Zəhmət olmasa düzgün daxil edildiyini yoxlayin")
        elif secim == "3":
            show_budget(xercler)
        elif secim == "4":
            balans,toplam = calculate_balance(gelir,xercler)
            print(f"\nÜmumi Gəlir: {gelir} AZN")
            print(f"Toplam Xərc: {toplam} AZN")
            print(f"Cari Balans: {balans} AZN")
        elif secim == "5":
            print("Programdan cixilir sagolun!")
            break
        else:
            print("Səhv seçim! Yenidən yoxlayın.")


if __name__ == "__main__":
    main()