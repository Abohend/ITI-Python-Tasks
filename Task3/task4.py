# 4) Product Data Transformer (lambda, map, filter, zip)
#    - Ask user for a list of product names (comma-separated).
#    - Ask user for a list of product prices (comma-separated).
#    - Process them by:
#         - Pairing product with price.
#         - Filtering out items where price <= 0.
#         - Transforming each pair into a dictionary {"product": name, "price": price, "discounted": price * 0.9}.
#    - Save the final result as JSON into "products.json".
#    - Print a preview of the first 5 results.

# task4_product_transformer.py

import json

def transformProducts():
    while True:
        names_input = input("Enter product names (comma-separated): ").strip()
        product_names = [name.strip() for name in names_input.split(",") if name.strip()]
        if product_names:
            break
        print("Invalid input.")

    while True:
        prices_input = input("Enter product prices (comma-separated): ").strip()
        try:
            product_prices = [float(p.strip()) for p in prices_input.split(",")]
            if len(product_prices) != len(product_names):
                print("Number of prices must match number of products.")
            else:
                break
        except ValueError:
            print("Invalid price.")

    paired = list(zip(product_names, product_prices))

    # filter prices
    filtered = list(filter(lambda pair: pair[1] > 0, paired))

    # transform to dict
    transformed = list(map(lambda pair: {
        "product": pair[0],
        "price": round(pair[1], 2),
        "discounted": round(pair[1] * 0.9, 2)
    }, filtered))

    # to json
    with open("products.json", "w") as file:
        json.dump(transformed, file, indent=2)

    # print first 5 results
    print(f"\nPreview:")
    for item in transformed[:5]:
        print(f"  - {item}")