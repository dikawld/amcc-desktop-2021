# data indexing
x = ['Emilia-tan', 20, 'Dekstop Programing', 3.9, 'true']
x.append("AMCC") # menambah data dalam list
x.remove(20) # menghapus data dalam list
# print(x)

angka = [1,2,3,4,5]
angka.reverse() #membalik list
angka.sort()
#print(angka)

# data indexing tuple, data tidak bisa diubah-ubah
x = ('Dekstop programing', 20, 'emilia-tan', 3,99)
#print (len(x[0]))

y = [2,5,4,6,7,8,9,8,1,11] 
#print(max(y))
#print(min(y))

#data indexing set
z = {2,6,2,2,1,4,5,5,8,7,7,9,9}
#print(type(z))
#z.discard(3)
#z.remove(2)
#z.add(77)
#z.update('jancok')
#print(z)

# data dictionary
a = {'name':'emilia-tan','division':'halfelf', 'age':'200','IP':'3,55'}
#a.pop('IP')
#a.clear()
#print(a.get('division'))
#print(a)

# input output
# panjang = input('masukan nilai panjnag: ')
# lebar = input('masukan nilai lebar: ')
# penghitungan
# luas = int(panjang)* int(lebar)
#print('luas =', luas) 

#  function
def halo_dunia():
    print('halo pyton! halo dunia!')

halo_dunia()

def perkenalan(nama, asal):
    print("perkenalan saya", nama,"dari",asal)

perkenalan("emilia","re:zero")