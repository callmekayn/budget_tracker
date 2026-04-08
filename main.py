def main():
    print("--- Büdcə İzləyicisi v1.0 ---")

    try:
        gelir = float(input("Aylıq gəlirinizi daxil edin: "))
        xercli_ad = input("Xərcin adını yazın: ")
        xercli_mebleg = float(input("Xərcin məbləğini yazın: "))

        qaliq = gelir - xercli_mebleg
        print(f"\nHesabat: {xercli_ad} üçün {xercli_mebleg} AZN xərcləndi.")
        print(f"Qalan məbləğ: {qaliq} AZN")

    except ValueError:
        print("Xahiş olunur yalnız rəqəm daxil edin!")


if __name__ == "__main__":
    main()