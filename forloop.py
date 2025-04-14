

# For-loop
# For kondisi:
#  aksi

a = 0
a += 1 # a = a + 1
print(a)
a += 1
print(a)
a += 1
print(a)

# perulangan dan list
angka_list = [0,1,4,8,10]
for i in angka_list: 
    print(f"i sekarang -> {i}")

# perulangan dan range
angka_range = range(5) # diulang 5 kali

for i in angka_range:
    print(f"i sekarang -> {i}")

print("ini ahkir for 2 \n")

angka_range = range(1, 10) # diulang 9/10
for i in angka_range:
    print(f"i sekarang -> {i}")

print("ini ahkir for 3 \n")

# Latihan
nama = "neymar"

for i in range(len(nama)):
    print(f"huruf ke-{i}: {nama[i]}")