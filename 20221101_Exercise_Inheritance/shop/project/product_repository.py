class ProductRepository:
    products = []

    def add(self, product):
        ProductRepository.products.append(product)

    def find(self, product_name):
        for product in ProductRepository.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        for product in ProductRepository.products:
            if product.name == product_name:
                ProductRepository.products.remove(product)

    def __repr__(self):
        output = []
        for product in ProductRepository.products:
            output.append(f"{product}: {product.quantity}")
        return '\n'.join(output)
