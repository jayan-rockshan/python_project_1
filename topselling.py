import csv
import unittest

def topSellingAnalysis():
    sales_data = []
    with open('supermarket_sales.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            sales_data.append(row)
    list_len = len(sales_data)
    product_id = []
    x = 1
    
    while(x < list_len):
        if(sales_data[x][2] not in product_id):
            product_id.append(sales_data[x][2])
        x = x + 1
    product_sales = []
    len_product_id = len(product_id)
    count = 0
    
    while(count < len_product_id):
        innerCount = 1
        totalSales = 0
        testList = []
        while(innerCount < list_len):
            if(product_id[count] == sales_data[innerCount][2]):
                totalSales = totalSales + float(sales_data[innerCount][7])
            innerCount = innerCount + 1
        testList.insert(0, product_id[count])
        testList.insert(1, totalSales)
        product_sales.append(testList)
        count = count + 1
    sorted_products_id_sales = sorted(product_sales, key=lambda x: x[1], reverse=True)
    sorted_top_id = []
    sorted_count = 0
    while(sorted_count < 5):
        sorted_top_id.insert(sorted_count, sorted_products_id_sales[sorted_count][0])
        sorted_count = sorted_count + 1
    return sorted_top_id

class TestCustomerSalesAnalysis(unittest.TestCase):
    def test_analyze_customer_sales(self):
   
    
        
        # Calculate the expected result
        expected_result = ['106', '104', '105', '108', '109']
        result = topSellingAnalysis()
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
