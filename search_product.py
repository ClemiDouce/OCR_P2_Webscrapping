import requests
from bs4 import BeautifulSoup

import settings
from utils import format_rating, dict_to_csv, get_img

URL = "https://books.toscrape.com"


def get_categories():
    """
    Return categories name in a list
    """
    url = f"{URL}/index.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    tag_list = soup.select("li > ul > li > a")
    list_category = []
    for tag in tag_list:
        list_category.append(
                {"label": tag.string.strip(), "url": url.replace("index.html", tag["href"])}
        )
    return list_category


def search_all():
    """
    Get all books in all categories of the book.toscrape site
    """
    list_category = get_categories()
    for category in list_category:
        result = search_products_by_category(category["url"], category["label"])
        dict_to_csv(result, category["label"])


def search_products_by_category(url: str, name: str) -> list:
    """
    Return product for a given category
    """
    product_list = []
    page_counter = 1
    base_url = url[:37]
    cat_page = requests.get(url)
    cat_soup = BeautifulSoup(cat_page.content, "html.parser")
    list_product = cat_soup("article", class_="product_pod")
    for product in list_product:
        product_url = base_url + product.a["href"][9:]
        product = search_product(product_url, name)
        product_list.append(product)
    while cat_soup.find("li", class_="next"):
        page_counter += 1
        next_url = url.replace("index.html", f"page-{page_counter}.html")
        cat_page = requests.get(next_url)
        cat_soup = BeautifulSoup(cat_page.content, "html.parser")
        list_product = cat_soup("article", class_="product_pod")
        for product in list_product:
            product_url = base_url + product.a["href"][9:]
            product = search_product(product_url, name)
            product_list.append(product)

    return product_list


def search_product(url: str, category: str = 'none') -> dict:
    """
    Return a product for a given url
    """
    prod_page = requests.get(url)
    prod_soup = BeautifulSoup(prod_page.content, "html.parser")
    # Titre, Desc, Img URL
    prod_title = prod_soup.h1.string
    if len(prod_soup.select("div#product_description + p")) > 0:
        prod_desc = prod_soup.select("div#product_description + p")[0].string
    else:
        prod_desc = "No Description"
    prod_img_url = f"{URL}/" + prod_soup.img["src"][6:]

    # UPC, Price, Count, Categorie
    prod_info_tab = map(lambda tag: tag.string, prod_soup("td"))
    (
        prod_upc,
        prod_category,
        prod_price_excl,
        prod_price_incl,
        _,
        prod_count,
        _,
    ) = prod_info_tab

    if settings.download_image_option:
        if category == 'none':
            filename = prod_upc
            get_img(prod_img_url, filename.lower())
        else:
            filename = f"{category}_{prod_upc}"
            get_img(prod_img_url,filename.lower(), category)

    # Format Available
    prod_count = "".join(filter(str.isdigit, prod_count))

    # Rating
    prod_rating = format_rating(prod_soup.find("p", class_="star-rating")["class"][-1])
    return {
        "page_url": url,
        "title": prod_title,
        "desc": prod_desc,
        "img_url": prod_img_url,
        "upc": prod_upc,
        "price_excl": prod_price_excl,
        "price_incl": prod_price_incl,
        "available": prod_count,
        "category": prod_category,
        "rating": prod_rating,
    }
