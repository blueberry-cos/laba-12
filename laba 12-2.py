import json
with open("products.json", "r", encoding="utf-8") as f:
    data = json.load(f)
data["products"].append({ "name": input("Название: "), "price": int(input("Цена: ")), "weight": int(input("Вес: ")), "available": input("В наличии? (да/нет): ").lower() == "да" })
json.dump(data, open("products.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
for p in data["products"]:
    print(f"\nНазвание: {p['name']}\nЦена: {p['price']}\nВес: {p['weight']}\n{'В наличии' if p['available'] else 'Нет в наличии!'}")