from  createstd import generate_random_string,adminlogin,create_std


def test():
        adminlogin()
        create()
def test1(num):
    for i in range(num):
     create()

def create():
    rm = generate_random_string(3)
    rm1 = generate_random_string(1)     
    rm2 = generate_random_string(8)
    sname = "Student"+rm
    email = "std" + rm + "@nclex.com"
    contact = "98"+ rm2
    pan = rm2
    exp = rm1
    rollno = rm
    password = "adminadmin"
    create_std(sname,contact,pan,email,password,exp,rollno)
    
if __name__ == "__main__":
    test()
    num = 2  
    # here n=2 denotes the number of time the student is created
    # if you want to create n student then you should have to place value n-1 because  above function creates 1 default std.
    test1(num)
