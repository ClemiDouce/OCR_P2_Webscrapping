import sys
import requests
import argparse
from bs4 import BeautifulSoup
from search_product import search_product



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help="Url of the product you search to scrap")
    parser.add_argument(
        "-c", "--category", help="the category you want to search", action="store_true")
    parser.add_argument(
        "-a", "--all", help="if you want to search all the site", action="store_true")
    args = parser.parse_args()


    if args.all:
        print('Recherche sur tout le site')
    elif args.category:
        print("Recherche par categorie")
    else:
        print("Recherche par Produit")
        product = search_product(sys.argv[1])
        print(product['img_url'])
