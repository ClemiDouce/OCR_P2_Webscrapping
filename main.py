import requests
import argparse
import re
from bs4 import BeautifulSoup
from search_product import (
    search_product,
    search_products_by_category,
    search_all,
    get_all_categories,
)
from utils import dict_to_csv


if __name__ == "__main__":
    # Parser
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--category", help="the category you want to search", action="store_true"
    )
    parser.add_argument(
        "-a", "--all", help="if you want to search all the site", action="store_true"
    )
    parser.add_argument("-p", "--product", help="Get all info for a product")
    args = parser.parse_args()

    if args.all:
        book_list = search_all()
        dict_to_csv(book_list, "all_books")
    elif args.category:
        list_categories = get_all_categories()
        for index, category in enumerate(list_categories):
            print(f"[{index}] {category['label']}")
        choice = input(
            "Choississez le numero de la categorie que vous voulez chercher : "
        )
        try:
            choice = int(choice)
            result = search_products_by_category(list_categories[choice]["url"])
            dict_to_csv(result, f"{list_categories[choice]['label']}_books")
        except IndexError:
            print("Le chiffre entrée n'existe pas")
        except ValueError as err:
            print("Vous n'avez pas entré un chiffre")
    elif args.product:
        if args.product != "":
            if re.search(r"^(https:\/\/books.toscrape.com\/catalogue\/)[\w\W]*(index.html)$", args.product):
                product = [search_product(args.product)]
                dict_to_csv(product, product[0]['title'][:10] + '.csv')
            else:
                print("Vous n'avez pas envoyé un lien de book.toscrape")
        else:
            print("Vous n'avez pas entré d'url")
