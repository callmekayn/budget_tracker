from functions import show_budget,calculate_balance,reset_budget
import datetime

#Developed by Kenan Abbaszade
def main():

    global gelir
    xercler = []
    gelirler = []

    print("--- Budget Tracker v1.0 ---")
    while True:
        print("\n=== Budget Planner ===")
        print("1. Xerc daxil edin")
        print("2. Ayliq Gəlir daxil edin")
        print("3. Kommunal Ödənişlər")
        print("4. Xercleri göstərin")
        print("5. Balansı yoxla")
        print("6. Reset Budget")
        print("7. Çıxış")

        secim = input("\nSeciminizi edin 1-4 : ")

        if secim == "1":
            ad = input("Xercin adi : ")
            try:
                date = datetime.datetime.now()
                mebleg = float(input("Meblegi : "))
                xercler.append({"ad":ad,"mebleg":mebleg,"date":date})
                print("Ugurla elave edildi!")
            except ValueError:
                print("Səhv: Zəhmət olmasa rəqəm daxil edin.")
        elif secim == "2":
            ad = input("Gelir Növünün daxil edin: : ")
            try:
                gelir = float(input("Geliri daxil edin  : "))
                gelirler.append({"ad":ad,"gelir":gelir})
            except ValueError:
                print("Error: Zəhmət olmasa Rəqəm daxil edin.")
        elif secim == "3":
            ad = input("Kommunal xercin adi : ")
            try:
                date = datetime.datetime.now()
                mebleg = float(input("Kommunal xercin meblegini daxil edin: "))
                xercler.append({"ad":ad,"mebleg":mebleg,"date":date})
                print("Ayliq Kommunal xərci uğurla daxil edildi!")
            except ValueError:
                print("Error: Zəhmət olmasa düzgün daxil edildiyini yoxlayin")
        elif secim == "4":
            show_budget(xercler)
        elif secim == "5":
            balans,toplam = calculate_balance(gelir,xercler)
            print(f"\nÜmumi Gəlir: {gelir} AZN")
            print(f"Toplam Xərc: {toplam} AZN")
            print(f"Cari Balans: {balans} AZN")
        elif secim == "6":
            reset_budget(xercler)
        elif secim == "7":
            print("Programdan cixilir sagolun!")
            break
        else:
            print("Səhv seçim! Yenidən yoxlayın.")


if __name__ == "__main__":
    main()