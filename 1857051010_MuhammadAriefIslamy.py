def main():
    try:
        n1, n2 = eval(
            input("Masukkan 2 angka (pisahkan dengan koma) :")
        )
        r1 = n1 + n2
        r2 = n1 * n2
        r3 = n1 - n2
        r4 = n1 / n2
        print("Hasil penjumlahan :", r1, "\nHasil perkalian :", r2,
              "\nHasil pengurangan :", r3, "\nHasil pembagian :", r4)
    except ZeroDivisionError:
        print("Division by zero!")
    except SyntaxError:
        print("Inputkan dengan koma")
    except:
        print("Mohon inputkan dengan benar")
    else:
        print("No exceptions")
    finally:
        print("The finnaly clause is executed")


main()
