import csv

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

def dict_to_csv(book_list):
    with open('books.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['title','desc', 'img_url', 'upc', 'price_excl', 'price_incl', 'available', 'category', 'rating', 'page_url'])
        writer.writeheader()
        for book in book_list:
            writer.writerow(book)