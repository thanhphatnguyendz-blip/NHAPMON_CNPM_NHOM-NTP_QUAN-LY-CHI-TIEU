print("================================")
print(" QUAN LY CHI TIEU SINH VIEN")
print("================================")

thu_nhap = float(input("Nhap thu nhap: "))
chi_tieu = float(input("Nhap chi tieu: "))

so_du = thu_nhap - chi_tieu

print("Tong thu nhap:", thu_nhap)
print("Tong chi tieu:", chi_tieu)
print("So du hien tai:", so_du)
if so_du < 0:
    print("Canh bao: Ban dang tieu qua tay!")