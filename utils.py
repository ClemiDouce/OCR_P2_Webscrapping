import csv
import requests

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
    with open(f'csv/{filename}.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['title','desc', 'img_url', 'upc', 'price_excl', 'price_incl', 'available', 'category', 'rating', 'page_url'])
        writer.writeheader()
        for book in book_list:
            writer.writerow(book)

def get_img(img_url, filename="picture"):
    response = requests.get(img_url)
    with open(f"img/{filename}.png", "wb") as file:
        file.write(response.content)
        file.close()

if __name__ == "__main__":
    get_img("https://books.toscrape.com/media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg", "attic")