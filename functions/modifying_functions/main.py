# Ορισμός της συνάρτησης για έκπτωση με προεπιλεγμένη τιμή 5%
def apply_discount(price, discount=0.05):
    return price * (1 - discount)

# Ορισμός της συνάρτησης για φόρο με προεπιλεγμένη τιμή 7%
def apply_tax(price, tax=0.07):
    return price * (1 + tax)

# Ορισμός της συνάρτησης για συνολικό κόστος με χρήση των παραπάνω
def calculate_total(price, discount=0.05, tax=0.07):
    discounted = apply_discount(price, discount)
    total = apply_tax(discounted, tax)
    return total

# Κλήση με προεπιλεγμένες τιμές
total_default = calculate_total(120)
print(f"Total cost with default discount and tax: ${total_default}")

# Κλήση με προσαρμοσμένες τιμές (μέσω keyword arguments)
total_custom = calculate_total(100, discount=0.10, tax=0.08)
print(f"Total cost with custom discount and tax: ${total_custom}")