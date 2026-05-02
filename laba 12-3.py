open("en-ru.txt", "w", encoding="utf-8").write("""cat - кошка
dog - собака
home - домашняя папка, дом
mouse - мышь, манипулятор мышь
to do - делать, изготавливать
to make - изготавливать""")
print("Файл en-ru.txt создан!")
ru_en = {}
for line in open("en-ru.txt", "r", encoding="utf-8"):
    if line.strip():
        en, ru = line.strip().split(" - ")
        for w in ru.split(", "):
            ru_en[w] = ru_en.get(w, []) + [en]
with open("ru-en.txt", "w", encoding="utf-8") as f:
    for ru in sorted(ru_en):
        f.write(f"{ru} – {', '.join(sorted(ru_en[ru]))}\n")
print("Файл ru-en.txt создан!")