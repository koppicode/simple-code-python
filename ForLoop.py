#list sebagai iterable
gorengan=['bakwan','tahu isi','tempe goreng','cireng','ubi goreng']

#looping di python begitu mudah
for g in gorengan:
    print(g)
    print(len(g))
print(30*'=')
#sting sebagai iterable
bakwan = "bakwan"

for i in bakwan:
    print(i)

#for di dalam for
gorengan=['bakwan','tahu isi','tempe goreng','cireng','ubi goreng']
buah =['apel','jeruk','jambu','semangka','manggis']
sayur =['kangkung','bayam','tomat','bawang','cabai']

daftar_belanja = [gorengan,buah,sayur]

for subDaftarBelanja in daftar_belanja:
    print(subDaftarBelanja)
    for komponen in subDaftarBelanja:
        print(komponen) 