import csv

# top selling analysis
def topSellingAnalysis():
    sales_data = []
    with open('supermarket_sales.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            sales_data.append(row)
    
    list_len = len(sales_data)
    product_id = []
    x = 1
    
    while x < list_len:
        if sales_data[x][2] not in product_id:
            product_id.append(sales_data[x][2])
        x = x + 1

    product_sales = []
    len_product_id = len(product_id)
    count = 0
    
    while count < len_product_id:
        innerCount = 1
        totalSales = 0
        testList = []
        
        while innerCount < list_len:
            if product_id[count] == sales_data[innerCount][2]:
                totalSales = totalSales + float(sales_data[innerCount][7])
            innerCount = innerCount + 1
        
        testList.insert(0, product_id[count])
        testList.insert(1, totalSales)
        product_sales.append(testList)
        count = count + 1

    sorted_products_id_sales = sorted(product_sales, key=lambda x: x[1], reverse=True)
    sorted_top_id = []
    sorted_count = 0
    
    while sorted_count < 5:
        sorted_top_id.insert(sorted_count, sorted_products_id_sales[sorted_count][0])
        sorted_count = sorted_count + 1

    # output the value
    print(sorted_top_id)

# product performance analysis
def productperAnalysis():
    sales_data = []
    with open('supermarket_sales.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            sales_data.append(row)

    list_len = len(sales_data)
    product_id = []
    x = 1
    
    while x < list_len:
        if sales_data[x][2] not in product_id:
            product_id.append(sales_data[x][2])
        x = x + 1

    product_qty = []
    len_product_id = len(product_id)
    count = 0
    
    while count < len_product_id:
        innerCount = 1
        totalQty = 0
        testList = []
        
        while innerCount < list_len:
            if product_id[count] == sales_data[innerCount][2]:
                totalQty = totalQty + float(sales_data[innerCount][4])
            innerCount = innerCount + 1
        
        testList.insert(0, product_id[count])
        testList.insert(1, totalQty)
        product_qty.append(testList)
        count = count + 1

    print(product_qty)

# customer behavior analysis
def customerAnalysis():
    sales_data = []
    with open('supermarket_sales.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            sales_data.append(row)

    list_len = len(sales_data)
    customer_id = []
    x = 1
    
    while x < list_len:
        if sales_data[x][1] not in customer_id:
            customer_id.append(sales_data[x][1])
        x = x + 1

    customer_totAmount = []
    len_customer_id = len(customer_id)
    count = 0
    
    while count < len_customer_id:
        innerCount = 1
        totalSales = 0
        testList = []
        
        while innerCount < list_len:
            if customer_id[count] == sales_data[innerCount][1]:
                totalSales = totalSales + float(sales_data[innerCount][7])
            innerCount = innerCount + 1
        
        testList.insert(0, customer_id[count])
        testList.insert(1, totalSales)
        customer_totAmount.append(testList)
        count = count + 1

    print(customer_totAmount)
#application start
while True:
    print("*********************************  Main Menu  ****************************************")
    print("1. Top-selling Product Analysis")
    print("2. Product Performance Analysis")
    print("3. Customer Behavior Analysis")
    print("4. Exit the system")
    
    choice = int(input("=====Enter Category: "))
    
    if choice == 1:
        topSellingAnalysis()
    elif choice == 2:
        productperAnalysis()
    elif choice == 3:
        customerAnalysis()
    elif choice == 4:
        print("See you again")
        break  # Exit the loop and exit the system
    else:
        print("Invalid entry")
