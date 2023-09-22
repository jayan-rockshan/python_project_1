import csv
import unittest

def productperAnalysis():
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

    product_qty = []
    len_product_id = len(product_id)
    count = 0
    while(count < len_product_id):
        innerCount = 1
        totalQty = 0
        testList = []
        while (innerCount < list_len):
            if(product_id[count] == sales_data[innerCount][2]):
                totalQty = totalQty + float(sales_data[innerCount][4])
            innerCount = innerCount + 1
        testList.insert(0, product_id[count])
        testList.insert(1, totalQty)
        product_qty.append(testList)
        count = count + 1

    return product_qty

class TestProductPerAnalysis(unittest.TestCase):
    def test_analyze_product_per_sales(self):
        # Calculate the expected result
        expected_result = [['109', 281.0], ['100', 288.0], ['104', 255.0], ['102', 335.0], ['108', 437.0], ['103', 290.0], ['105', 288.0], ['101', 211.0], ['106', 266.0], ['107', 240.0]]
        result = productperAnalysis()
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
