import csv
import os
import requests
from zipfile import ZipFile
import settings

def format_rating(rating):
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

def dict_to_csv(book_list, filename="book"):
    final_filename = f'{filename}.csv'
    if not os.path.exists('csv/'):
        os.mkdir('csv/')
    with open(f'csv/{final_filename}', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['title','desc', 'img_url', 'upc', 'price_excl', 'price_incl', 'available', 'category', 'rating', 'page_url'])
        writer.writeheader()
        for book in book_list:
            writer.writerow(book)
    settings.to_zip['csv'].append(final_filename)

def get_img(img_url, filename="picture"):
    final_filename = f"{filename}.png"
    response = requests.get(img_url)
    if not os.path.exists('img/'):
        os.mkdir('img/')
    with open(f"img/{final_filename}", "wb") as file:
        file.write(response.content)
        file.close()
    settings.to_zip['img'].append(final_filename)

def zip_files(filename="books"):
    if not os.path.exists('zip/'):
        os.mkdir('zip/')
    with ZipFile(f'zip/{filename}.zip', 'w') as zipObj:
        for directory, files in settings.to_zip.items():
            for file in files:
                zipObj.write(f"{directory}/{file}")

if __name__ == "__main__":
    # get_img("https://books.toscrape.com/media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg", "attic")
    zip_files('csv', ['Crime_books.csv'])