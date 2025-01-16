from utils import write_json, read_json

class SalesManagement:
    def __init__(self, file_name):
        self.file_name = file_name
        self.sales = read_json(file_name)

    def add_sale(self, sale):
        self.sales.append(sale)
        write_json(self.file_name, self.sales)
        print("Sotuv muvaffaqiyatli amalga oshdi!")

    def view_sales(self):
        print("Barcha sotuvlar ro'yxati:")
        for sale in self.sales:
            print(f"Raqam: {sale['number']}, Narx: {sale['price']} so'm, Xaridor: {sale['user_name']}, Sana: {sale['date']}")
