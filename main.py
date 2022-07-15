class data_siswa :
    def __init__(informasi, nama, nim, jurusan):
        informasi.nama = nama
        informasi.nim = nim 
        informasi.jurusan = jurusan

    def pelengkap(abc):
        print("nama = " + abc.nama)
        print("nim = "+ abc.nim)
        print("jurusan = " + abc.jurusan)

input_nama = input("masukan nama  = ")
input_nim = input ("NIM = ")
input_jurusan = input("masukan jurusan = ") 
p1 = data_siswa(input_nama,input_nim,input_jurusan)
print("-----------------------------------------------")
p1.pelengkap()
    
