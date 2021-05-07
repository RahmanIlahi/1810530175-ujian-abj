ulang = "ya"
while ulang == "ya":
    pilih = input("Input data trunk interfaces baru (yes/no): ")
    if pilih == "yes":
        interfaces = input("Masukkan hostname switch : ")
        file = open("db-interfaces.txt",'a')
        file.write("\n"+"Masukkan hostname switch : " + interfaces)
        interfaces = input("MAsukkan nama interfaces : ")
        file = open("db-interfaces.txt",'a')
        file.write("\n"+"Masukkan hostname switch : " + interfaces)
    else:
         file = open("db-interfaces.txt",'r')
         print(file.read())
         break

