import tkinter as tk

def show_result():
    # Kullanıcı girdilerini al
    x = int(var_gender.get())
    y = int(var_type.get())
    z = int(var_typeee.get())

    # Kullanıcı girdilerine göre doğrudan doğru elemanı yazdır
    index = (x - 1) * 4 + (y - 1) * 2 + (z - 1)
    result_var.set(myList[index])

# Ana Tkinter penceresi
root = tk.Tk()
root.title("Favori kokunu keşfet !")

# myList
myList = ["CALVIN KLEIN - Euphoria Woman", "CHLOÉ - Love Story", "VERSACE - Crystal Noir", "ARMANI - Si", "VERSACE - Versace Eros", "YVES SAINT LAURENT - MYSLF","BURBERRY - Burberry Hero","DOLCE & GABBANA - K By Dolce&Gabbana" ]

# Kullanıcı girdileri için etiketler ve seçenekler
tk.Label(root, text="Hangi parfümleri incelemek istersiniz ?").grid(row=0, column=0, sticky="w")
var_gender = tk.StringVar(value="1")
tk.Radiobutton(root, text="Kadın", variable=var_gender, value="1").grid(row=1, column=0, sticky="w")
tk.Radiobutton(root, text="Erkek", variable=var_gender, value="0").grid(row=2, column=0, sticky="w")

tk.Label(root, text="Genelde hangi kokular ilginizi çeker ?").grid(row=3, column=0, sticky="w")
var_type = tk.StringVar(value="1")
tk.Radiobutton(root, text="Ferah", variable=var_type, value="1").grid(row=4, column=0, sticky="w")
tk.Radiobutton(root, text="Odunsu", variable=var_type, value="2").grid(row=5, column=0, sticky="w")

tk.Label(root, text="Kullandığınız kokuların ne kadar fark edilir olmasını tercih edersiniz ?").grid(row=6, column=0, sticky="w")
var_typeee = tk.StringVar(value="1")
tk.Radiobutton(root, text="Yoğun, baskın kokular severim", variable=var_typeee, value="1").grid(row=7, column=0, sticky="w")
tk.Radiobutton(root, text="Baskın olmasın, fark edilsin", variable=var_typeee, value="2").grid(row=8, column=0, sticky="w")

# Sonuç gösterme
result_var = tk.StringVar()
tk.Label(root, textvariable=result_var).grid(row=9, columnspan=3, sticky="w")

# Butonu ekle ve sonucu göster
tk.Button(root, text="Hadi keşfedelim", command=show_result).grid(row=10, columnspan=3, sticky="w")
# Pencereyi aç
root.mainloop()
