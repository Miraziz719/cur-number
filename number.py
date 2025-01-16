from datetime import datetime
from utils import write_json, read_json

class NumberManagement:
    def __init__(self, file_name):
        self.file_name = file_name
        self.numbers = read_json(file_name)

    def add_number(self, number, price):
        max_id = max((num["id"] for num in self.numbers), default=0)
        new_number = {
            "id": max_id + 1,
            "number": number,
            "price": price,
            "status": "mavjud"
        }
        self.numbers.append(new_number)
        write_json(self.file_name, self.numbers)
        print("Raqam muvaffaqiyatli qo'shildi!")

    def view_numbers(self):
        print("Mavjud raqamlar ro'yxati:")
        for number in self.numbers:
            if number["status"] == "mavjud":
                print(f"ID: {number['id']}, Raqam: {number['number']}, Narx: {number['price']} so'm")

    def edit_number(self, number_id, new_number=None, new_price=None):
        for number in self.numbers:
            if number["id"] == number_id:
                if new_number:
                    number["number"] = new_number
                if new_price:
                    number["price"] = new_price
                write_json(self.file_name, self.numbers)
                print("Raqam muvaffaqiyatli tahrirlandi!")
                return
        print("Raqam topilmadi!")

    def delete_number(self, number_id):
        for number in self.numbers:
            if number["id"] == number_id:
                self.numbers.remove(number)
                write_json(self.file_name, self.numbers)
                print("Raqam muvaffaqiyatli o'chirildi!")
                return
        print("Raqam topilmadi!")

    def sell_number(self, number_id, user_id, user_name):
        for number in self.numbers:
            if number["id"] == number_id and number["status"] == "mavjud":
                number["status"] = "sotilgan"
                write_json(self.file_name, self.numbers)
                return {
                    "number": number["number"],
                    "price": number["price"],
                    "date": str(datetime.now().date()),
                    "user_id": user_id,
                    "user_name": user_name
                }
        print("Raqam topilmadi yoki allaqachon sotilgan!")
        return None
