# Unit-3 Challenge 1
def linear_search_product(products, target_product):
    indices = []
    for i, product in enumerate(products):
        if product == target_product:
            indices.append(i)
    return indices
product_list = ["apple", "banana", "apple", "orange", "grape", "apple"]
target = "apple"
result = linear_search_product(product_list, target)
if result:
    print(f"The product '{target}' was found at indices: {result}")
else:
    print(f"The product '{target}' was not found in the list.")