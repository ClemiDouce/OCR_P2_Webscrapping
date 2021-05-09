import argparse
import re
from search_product import (
    search_product,
    search_products_by_category,
    search_all,
    get_all_categories,
)
from utils import dict_to_csv, zip_files
import settings


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
    parser.add_argument(
        "-i", "--image", help="Download image of each product", action="store_true"
    )
    parser.add_argument("-z", "--zip", help="Zip img and csv", action="store_true")
    args = parser.parse_args()
    settings.download_image_option = args.image
    settings.zip_option = args.zip

    if args.all:
        book_list = search_all()
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
            categorie_choice = list_categories[choice]["label"]
            dict_to_csv(result, f"{categorie_choice}_books")
            if settings.zip_option:
                zip_files(f"{categorie_choice}_results")
        except IndexError:
            print("Le chiffre entrée n'existe pas")
        except ValueError as err:
            print("Vous n'avez pas entré un chiffre")
    elif args.product:
        if args.product != "":
            if re.search(
                r"^(https:[/]{2}books.toscrape.com[/]catalogue[/])[\w\W]*(index.html)$",
                args.product,
            ):
                product = [search_product(args.product)]
                product_title = product[0]["title"][:10]
                dict_to_csv(product, product[0]["title"][:10] + ".csv")
                if settings.zip_option:
                    zip_files(product_title)
            else:
                print("Vous n'avez pas envoyé un lien de book.toscrape")
        else:
            print("Vous n'avez pas entré d'url")
    else:
        print("Vous avez entré aucun argument")
