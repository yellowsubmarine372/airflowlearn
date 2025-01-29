def get_sftp():
    print("get_sftp")
    
def regist(name, sex, *args):
    print(f"name: {name}, sex: {sex}, etc: {args}")
    
def regist2(name, sex, *args, **kwargs):
    print(f"name: {name}")
    print(f"sex: {sex}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
    
    email = kwargs.get("email") or ''
    print(f"email: {email}")
    
    phone = kwargs.get("phone") or ''
    print(f"phone: {phone}")
    
    