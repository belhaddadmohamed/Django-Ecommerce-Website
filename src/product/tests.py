from django.test import TestCase

# Create your tests here.


# ===========================================================================
# import csv
# from datetime import datetime
# import models 

# def import_products_from_csv(file_path):
#     with open(file_path, 'r') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             models.Product.objects.create(
#                 prdName=row['name'],
#                 prdDesc=row['description'],
#                 prdPrice=float(row['price']),
#                 prdCost=float(row['cost']),
#                 prdCreated=datetime.strptime(row['created'], '%Y-%m-%d').date()
#             )

# if __name__ == '__main__':
#     csv_file_path = "C:/Users/Sc/Desktop/Projects/Web-Sites/Site3 (Django_Ecommerce)/BelStore/products.csv"  
#     import_products_from_csv(csv_file_path)
# ===========================================================================
