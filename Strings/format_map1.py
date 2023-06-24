txt="I want {itemno} pieces of item {quantity} for {price} dollars."
print(txt.format_map({'itemno':467, 'quantity':3, 'price':49.95}))
