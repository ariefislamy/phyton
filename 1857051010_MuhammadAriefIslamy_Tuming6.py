class Karyawan: #class dengan nama karyawan 
    #constructor
    #self merupakan variabel menyatakan kelas itu sendiri
    def _init_(self, nama_depan, nama_belakang, nip, umur, gaji,jabatan): #atribut didalam tanda kurung parameter
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nip = nip
        self.umur = umur
        self.jabatan = jabatan
        self._gaji = gaji #atribut private _
    
    #method untuk mencetak nama lengkap terdiri dari nama depan dan nama belakang 
    def nama_lengkap(self):
        return(self.nama_depan + ' '+self.nama_belakang)

    #method umur
    def umurkar(self):
        return (self.umur)

    #method jabatan
    def jabatankar(self):
        return (self.jabatan)

    #method email, merupakan gabungan dari nama lengkap 
    def emailkar(self):
        return self.nama_depan +'.'+self.nama_belakang+'@employee.ac.id'

    def set__gaji(self, gaji): #method setter gaji
        self.__gaji = gaji
    def get__gaji(self): #method getter gaji
        return self.__gaji

nama_depan = input("Masukkan Nama Depan : ")
nama_belakang = input("Masukkan Nama Belakang : ")
nip = int(input("Masukkan NIP : "))
set__gaji = int(input("Masukkan Gaji Bersih : "))
jabatan = input("Masukkan Jabatan : ")
umur = int(input("Masukkan Umur : "))

#instance objek krywn1
krywn1 = Karyawan(nama_depan, nama_belakang,nip,umur,set__gaji,jabatan)

#print/cetak isi class yang telah diinput
print("Nama Karyawan : "+krywn1.nama_lengkap())
print("NIP : ", krywn1.nip)
print("Umur : ",krywn1.umurkar())
print("Gaji : ",krywn1.get__gaji())
print("Jabatan : " + krywn1.jabatankar())
print("email : "+ krywn1.emailkar())