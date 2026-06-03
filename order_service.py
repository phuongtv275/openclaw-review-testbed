import os

# 🟡 missing module docstring

def process_order(order, user, config, db, cache):
    # 🟡 function too long, deeply nested (5 levels)
    if order:
        if user:
            if user["active"]:
                if order["status"] == "pending":
                    if config.get("feature_flag"):
                        # 🟡 magic numbers: 500, 0.1, 30, 0.08
                        if order["amount"] > 500:
                            discount = order["amount"] * 0.1
                            if discount > 30:
                                discount = 30
                            order["amount"] -= discount

                        # 🟡 DRY violation — tax logic duplicated below
                        tax = order["amount"] * 0.08
                        order["total"] = order["amount"] + tax
                        db.save(order)
                        cache.invalidate(order["id"])
                        x = order["amount"]
                        y = order["total"]
                        z = y - x
                        return z
                    else:
                        # 🟡 DRY violation — identical tax logic
                        tax = order["amount"] * 0.08
                        order["total"] = order["amount"] + tax
                        db.save(order)
                        cache.invalidate(order["id"])
                        return 0
    return None

# 🟡 missing type hints
def calculate_shipping(weight, destination, express):
    # 🟡 magic numbers: 5, 10, 15, 2
    base = 5
    if weight > 10:
        base = 15
    if express:
        base = base * 2
    return base

# 🟡 PEP 8 — ambiguous variable names l, O, I
def transform(l):
    O = []
    for I in l:
        O.append(I * 2)
    return O