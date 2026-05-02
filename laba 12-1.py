import json
for p in json.load(open("products.json", "r", encoding="utf-8"))["products"]:
    print(f"Название: {p['name']}\nЦена: {p['price']}\nВес: {p['weight']}\n{'В наличии' if p['available'] else 'Нет в наличии!'}\n")