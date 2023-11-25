products = ["flour","apple","punnet of raspberries","bread", "apple"]
print(products)
print(products[3])
print(products[-5])
print((products[3][4]))
print(len(products))
print(len(products[2]))
products.append("orange")
print(products)
product_detail = ["flour", "3.59","aisle 1","storeroom aisle A", 34]
print(product_detail)
print("item: "+products[0]+" costs: £"+str(product_detail[1])+" can be found at␣
,→"+product_detail[2])
print("item: "+product_detail[0]+" costs: £",product_detail[1]," can be found␣
,→at "+product_detail[2])
print("item: "+products[-6]+" costs: £"+str(product_detail[1])+" can be found␣
,→at "+product_detail[3]+" there are "+str(product_detail[4])+" in stock")
