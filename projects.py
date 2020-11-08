import functions


def pro_page():
     print("………………………………………………………………………|")
     print(f"*** Welcome in Projects ***|{functions.name}")
     print("………………………………………………………………………|")

     st=input("Enter --- create --- for create projects\nEnter --- view --- for view all projects\nEnter --- edit --- for edit projects\nEnter --- delete --- for delete projects\nEnter --- search --- for search for projects\n………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………\n")

     while not functions.is_alpha(st) or not functions.have_value(st):
          print("Please Enter your choise")
          st=input("Enter --- create --- for create projects\nEnter --- view --- for view all projects\nEnter --- edit --- for edit projects\nEnter --- delete --- for delete projects\nEnter --- search --- for search for projects\n………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………\n")


     if st=="create":
          functions.Create_Pro()

     elif st=="view":
          functions.View_Pro()

     elif st=="delete":
          functions.delete_Pro()

     elif st=="edit":
          functions.edit_Pro()
     
     elif st=="search":
          functions.search_date()