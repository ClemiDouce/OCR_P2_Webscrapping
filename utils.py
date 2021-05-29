import csv
import os
import requests
from zipfile import ZipFile
import settings


def format_rating(rating: str) -> int:
    """
    Return an int formatted rating
    """
    if rating == "Five":
        return 5
    elif rating == "Four":
        return 4
    elif rating == "Three":
        return 3
    elif rating == "Two":
        return 2
    else:
        return 1


def dict_to_csv(book_list: list, filename: str = "book"):
    """
    Save a booklist on CSV format
    """
    final_filename = f'{filename}.csv'
    if not os.path.exists('data/csv/'):
        os.mkdir('data/csv/')
    with open(f'data/csv/{final_filename}', 'w', newline='', encoding='utf-8_SIG') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['title', 'desc', 'img_url', 'upc', 'price_excl', 'price_incl',
                                                     'available',
                                                    'category', 'rating', 'page_url'])
        writer.writeheader()
        for book in book_list:
            writer.writerow(book)

    settings.to_zip['csv'].append(final_filename)


def get_img(img_url: str, filename: str, categorie: str = 'none'):
    """
    Save an img from an URL
    """
    final_filename = f"{filename}.png"
    if categorie != 'none':
        final_filename = categorie + '/' + final_filename
    response = requests.get(img_url)
    if not os.path.exists('data/img/'):
        os.mkdir('data/img/')
    else:
        if categorie != 'none' and not os.path.exists(f"data/img/{categorie}/"):
            os.mkdir(f"data/img/{categorie}/")

    with open(f"data/img/{final_filename}", "wb") as file:
        file.write(response.content)
        file.close()
    settings.to_zip['img'].append(final_filename)


def zip_files(filename: str = "books"):
    """
    Zip all files registered in the option file
    """
    if not os.path.exists('data/zip/'):
        os.mkdir('data/zip/')
    with ZipFile(f'data/zip/{filename}.zip', 'w') as zipObj:
        for directory, files in settings.to_zip.items():
            for file in files:
                zipObj.write(f"data/{directory}/{file}")
