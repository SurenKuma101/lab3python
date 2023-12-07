print("WELCOME TO THE AMANDO SHOPPING SITE")
print("1.Add a product to the cart. ")
print("2.Search for a product. ")
print("3.Delete a product from the cart.")
print("4.Display the contents of the cart.")
print("5.Purchase items.")
print("6.Quit.")

a=(input("product name"))
b=int(input("price of the product"))
c=(input("enter the brand name"))
 
Cart={}
if Cart>=5:
  print("cart is full")
