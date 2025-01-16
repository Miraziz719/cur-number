from utils import write_json, read_json

class UserManagement:
    def __init__(self, file_name):
        self.file_name = file_name
        self.users = read_json(file_name)

    def add_user(self, name, address):
        max_id = max((user["id"] for user in self.users), default=0)
        new_user = {
            "id": max_id + 1,
            "name": name,
            "address": address,
            "purchased_numbers": []
        }
        self.users.append(new_user)
        write_json(self.file_name, self.users)
        print("Foydalanuvchi muvaffaqiyatli qo'shildi!")
        return new_user["id"]

    def add_purchase(self, user_id, purchase):
        for user in self.users:
            if user["id"] == user_id:
                user["purchased_numbers"].append(purchase)
                write_json(self.file_name, self.users)
                print("Xarid muvaffaqiyatli qo'shildi!")
                return
        print("Foydalanuvchi topilmadi!")

    def view_purchases(self, user_id):
        for user in self.users:
            if user["id"] == user_id:
                print(f"{user['name']} tomonidan xarid qilingan raqamlar:")
                for purchase in user["purchased_numbers"]:
                    print(f"Raqam: {purchase['number']}, Narx: {purchase['price']} so'm, Sana: {purchase['date']}")
                return
        print("Foydalanuvchi topilmadi!")

    def view_users(self):
        print("Barcha foydalanuvchilar ro'yxati:")
        for user in self.users:
            print(f"ID: {user['id']} Ism: {user['name']}, Manzil: {user['address']} Xaridlar soni: {len(user['purchased_numbers'])}")

    def find_or_add_user(self, name):
        for user in self.users:
            if user["name"].lower() == name.lower():
                return user["id"]
        print("Foydalanuvchi topilmadi, yangi foydalanuvchi qo'shiladi.")
        address = input(f"{name} uchun manzilni kiriting: ")
        return self.add_user(name, address)
        


