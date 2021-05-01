import requests
from bs4 import BeautifulSoup
from utils import format_rating


def search_products_by_category(url):
    product_list = []
    base_url = url[:37]
    cat_page = requests.get(url)
    cat_soup = BeautifulSoup(cat_page.content, 'html.parser')
    list_product = cat_soup('article', class_="product_pod")
    for product in list_product:
        product_url = base_url + product.a['href'][9:]
        product_list.append(search_product(product_url))
    return product_list



def search_product(url):
    prod_page = requests.get(url)
    prod_soup = BeautifulSoup(prod_page.content, 'html.parser')
    # Titre, Desc, Img URL
    prod_title = prod_soup.h1.string
    prod_desc = prod_soup.select('div#product_description + p')[0].string
    prod_img_url = prod_soup.img['src']
    # print(
    #     f"Title : {prod_title} / Desc : {prod_desc[:40]}.. / Img Url : {prod_img_url}"
    # )

    # UPC, Price, Count, Categorie
    prod_info_tab = map(lambda tag: tag.string, prod_soup('td'))
    prod_upc, prod_category, prod_price_excl, prod_price_incl, prod_taxes, prod_count, prod_reviews_count = prod_info_tab

    # Format Available
    prod_count = ''.join(filter(str.isdigit, prod_count))

    # Rating
    prod_rating = format_rating(prod_soup.find(
        'p', class_="star-rating")['class'][-1])
    return {
        'page': prod_page.content,
        'title': prod_title,
        'desc': prod_desc,
        'img_url': prod_img_url,
        'upc': prod_upc,
        'price_excl': prod_price_excl,
        'price_incl': prod_price_incl,
        'available': prod_count,
        'category': prod_category,
        'rating': prod_rating
    }


if __name__ == "__main__":
    my_list = search_products_by_category("https://books.toscrape.com/catalogue/category/books/mystery_3/index.html")
    for book in my_list:
        print(book['title'])
    # product = search_product(
    #     "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
    # print(product["category"])
