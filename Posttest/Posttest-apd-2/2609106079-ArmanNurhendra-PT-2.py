admin = 15_000
komponen = [120_000, 135_000, 150_000, 175_000, 200_000, 220_000]
nim = 79

total_biaya = 0
for item in komponen:
    total_biaya = total_biaya + item

rata_rata = total_biaya / len(komponen)
total_biaya = total_biaya + admin
bolean = nim != rata_rata

for i in range(len(komponen)):
    print("komponen", i + 1, "=", komponen[i])

print("total_biaya =", total_biaya)
print("rata_rata =", rata_rata)
print("nim =", nim)
print("bolean =", bolean)
