import json

class admin:
    def __init__(self):
        self.data = {}
        with open("book_list.json","r") as file:
            data = json.load(file)
            if data:
                self.data = data

    def display_books(self):
        for k,v in self.data.items():
            print("Book code------>",k)
            for i,j in v.items():
                print(i,"----->",j)

            print("-------------------------------------")

    def add_book(self):
        dict = {}
        dict["Book_name"] = input("Enter the Book title : ")
        dict["Author"] = input("Enter the name of author")
        dict["Price"] = int(input("Enter the price of the book"))
        dict["discount"] = int(input("Enter the discount available for the book : "))
        dict["Stock"] = int(input("Enter the stock of the book : "))

        keys = list(self.data.keys())
        if len(keys)>0:
            new_key = int(keys[-1]) + 1
        else:
            new_key = "01"
        self.data[str(new_key)] = dict

        with open("book_list.json","w") as file:
            json.dump(self.data,file)
            print("Book Added successfully!!!")        


    def update_book(self):
        key = input("Enter the unique key of book for updating it : ")
        parameter = input("Enter the parameter you want to update (Price, discount, Stock) : ")
        self.data[key][parameter] = int(input("Enter the new value"))

        with open("book_list.json","w") as file:
            json.dump(self.data,file)
            print("Book Updated successfully!!!") 

    def delete_book(self):
        key = input("Enter the unique key of book for deleting it : ")

        del self.data[key]

        with open("book_list.json","w") as file:
            json.dump(self.data,file)
            print("Book Deleted successfully!!!") 



class user:
    def __init__(self):
        self.data = {}
        with open("book_list.json","r") as file:
            data = json.load(file)
            if data:
                self.data = data

        self.user_data = {}
        with open("user_info.json","r") as file:
            data = json.load(file)
            if data:
                self.user_data = data

    def user_sign_in(self,email,password):
        flag = False
        for k,v in self.user_data:
            if v['email'] == email:
                if v['password'] == password:
                    flag =True
                    return True
        if flag == False:
            return False


    def user_signup(self):
        data = {}
        data['Name'] = input("Enter your name")
        data['email'] = input("Enter your email")
        data['Password'] = input("Create a strong password")
        with open("user_info.json","w") as file:
            keys = list(self.user_data.keys())
        if len(keys)>0:
            new_key = int(keys[-1]) + 1
        else:
            new_key = "01"
        self.user_data[str(new_key)] = data

        with open("user_info.json","w") as file:
            json.dump(self.user_data,file)
            print("Signed up successfully!!!") 
            
    def display_books(self):
        for k,v in self.data.items():
            print("Book code------>",k)
        for i,j in v.items():
            print(i,"----->",j)
            print("-------------------------------------")

    def add_to_cart(self):
        pass

    def order(self):
        pass

    def update_profile(self):
        pass

    def view_order_history(self):
        pass
