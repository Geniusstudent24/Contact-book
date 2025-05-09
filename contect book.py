class contact:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number 
        self.email = email 
        
    def display_info(self):
        print("name is   :: ", self.name)
        print("number is :: ", self.number)
        print("email is  :: ", self.email) 
        print("-" * 30)  
        
class contactbook:
    def __init__(self, filename = "con.txt"):
        self.contacts = []
        self.filename = filename
        self.load()
        
    def add(self):
        name = input("name :: ").strip()
        num = input("number :: ").strip()
        email = input("email :: ").strip()
        
        new_con = contact(name, num, email)
        
        self.contacts.append(new_con)
        print("added.....")
        
    def all(self):
        if not self.contacts:
            print("empty..")
        else :
            for con in self.contacts:
                con.display_info()   
    
    print("-" * 30)
    
    def search(self):
        sr = input("search name :: ")
        
        found_list = []
        
        for con in self.contacts:
            if sr in con.name.lower():
                found_list.append(con)
                
        if not  found_list:
            print("no found")
        else:
            print(len(found_list), "number found")
            for con in found_list:
                con.display_info()
        print("-" * 30)    
        
    def delete(self):
        self.all()
        count = len(self.contacts)
        dlt = input("name delete :: ").strip()
        
        for i in range((len(self.contacts) -1), -1, -1):
            con = self.contacts[i]
            
            if con.name.strip().lower() == dlt.lower():
                del self.contacts[i]
                print("deleted.....", dlt)
            
        if count == len(self.contacts):
            print("no item deleted...")    
        
    def save(self):
        with open(self.filename, "w") as f:
            for con in self.contacts:
                f.write(f"{con.name} | {con.number} | {con.email}\n")
            print("success....")    
    
    def load(self):
        with open(self.filename, "r")as f:
            for line in f:
                line = line.strip()
                
                if not line:
                    continue
                
                part = line.split("|")   
                
                if len(part) == 3:
                    name, num, email = part
                    
                    loadcont = contact(name, num, email)
                    self.contacts.append(loadcont)
    
def display_menu():
    print("1. addd...") 
    print("2. all....")
    print("3. search....")    
    print("4. delete...")    
    print("5. save....")  
    print("6. exit....")
    print("-"* 30)
        
        
        
my_book = contactbook("con.txt")     

while True:
    display_menu()
    
    userch = int(input("enter the choice :: "))
    
    if userch == 1:
        my_book.add()
        
    elif userch == 2:
        my_book.all()
        
    elif userch == 3:
        my_book.search()
        
    elif userch  == 4:
        my_book.delete()
        
    elif userch  == 5:
        my_book.save()
        
    else:
        my_book.save()
        print("saved....")
        break