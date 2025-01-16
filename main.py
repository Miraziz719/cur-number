from users import UserManagement
from sales import SalesManagement
from number import NumberManagement


# Dasturni ishga tushirish
if __name__ == "__main__":
    numbers = NumberManagement("numbers.json")
    users = UserManagement("users.json")
    sales = SalesManagement("sales.json")

    # admin login qigan
    admin = False
    # user login qigan
    user = False
    # admin paroli 
    admin_password = '0000'

    # Dastur doimiy ishlab turadi chiqilmaguncha
    while True:
        if admin:
            print("\nAdmin menyusi:")
            print("1. Raqam qo'shish")
            print("2. Raqamni tahrirlash")
            print("3. Raqamni o'chirish")
            print("4. Mavjud raqamlarni ko'rish")
            print("5. Raqam sotish")
            print("6. Sotuvlarni ko'rish")
            print("7. Foydalanuvchi qo'shish")
            print("8. Foydalanuvchilarni ko'rish")
            print("9. Foydalanuvchi menyusiga o'tish")
        else:
            print("\nFoydalanuvchi menyusi:")
            print("1. Sotuvdagi raqamlarni ko'rish")
            print("2. Raqam harid qilish")
            print("3. Mening raqamlarim")
            print("4. Login")
            print("5. logout")
            print("6. Admin menyuga o'tish")

        print("0. Dasturdan chiqish")

        #  tanlov qabul qilish
        choice = input("Tanlang: ")

        if admin: 
            if choice == "1":
                number = input("Raqamni kiriting: ")
                price = int(input("Narxni kiriting: "))
                numbers.add_number(number, price)
            elif choice == "2":
                number_id = int(input("Tahrirlanadigan raqam ID raqamini kiriting: "))
                new_number = input("Yangi raqamni kiriting (bo'sh qoldirish - o'zgarmaydi): ") or None
                new_price = input("Yangi narxni kiriting (bo'sh qoldirish - o'zgarmaydi): ") or None
                new_price = int(new_price) if new_price else None
                numbers.edit_number(number_id, new_number, new_price)
            elif choice == "3":
                number_id = int(input("O'chiriladigan raqam ID raqamini kiriting: "))
                numbers.delete_number(number_id)
            elif choice == "4":
                numbers.view_numbers()
            elif choice == "5":
                user_id = int(input("Foydalanuvchi ID raqamini kiriting: "))
                number_id = int(input("Sotilayotgan raqam ID raqamini kiriting: "))
                for user in users.users:
                    if user["id"] == user_id:
                        user_name = user["name"]
                        sale = numbers.sell_number(number_id, user_id, user_name)
                        if sale:
                            users.add_purchase(user_id, sale)
                            sales.add_sale(sale)
                        break
                else:
                    print("Foydalanuvchi topilmadi!")
            elif choice == "6":
                sales.view_sales()
            elif choice == "7":
                name = input("Foydalanuvchi ismini kiriting: ")
                address = input("Manzilni kiriting: ")
                users.add_user(name, address)
            elif choice == '8':
                users.view_users()  
            elif choice == '9':
                admin = False
            elif choice == "0":
                print("Dasturdan chiqildi.")
                break
            else:
                print("Noto'g'ri tanlov! Iltimos, qaytadan urinib ko'ring.")
        else:
            if choice == "1":
                numbers.view_numbers()

            elif choice == "2":
                if not user:
                    print('Oldin login qilishingiz kerak')
                else:
                    number_id = int(input("Sotilayotgan raqam ID raqamini kiriting: "))
                    for user in users.users:
                        if user["id"] == user_id:
                            user_name = user["name"]
                            sale = numbers.sell_number(number_id, user_id, user_name)
                            if sale:
                                users.add_purchase(user_id, sale)
                                sales.add_sale(sale)
                            break
  
            elif choice == "3":
                if not user:
                    print('Oldin login qilishingiz kerak')
                else:
                    users.view_purchases(user)
            elif choice == "4":
                name = input("Ismini kiriting: ")
                user_id = users.find_or_add_user(name)
                user = user_id
                print('Login qilindi')
            elif choice == "5":
                user = False
                print('Logout qilindi')
            elif choice == '6':
                password = input('Admin parolini kirgazing: ')
                if password == admin_password:
                    admin = True
                else:
                    print("Parol notog'ri")

            elif choice == "0":
                print("Dasturdan chiqildi.")
                break
            else:
                print("Noto'g'ri tanlov! Iltimos, qaytadan urinib ko'ring.")
            
            
