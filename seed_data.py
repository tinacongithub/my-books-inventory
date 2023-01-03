from my_books_inventory.models import Books
Books(title="Las malas", author="Camila Sosa Villada", year_published=2019).save()
Books(title="Syntactic Structures", author="Noam Chomsky", year_published=1957).save()
Books(title="New World Sourdough", author="Bryan Ford", year_published=2020).save()

print("test data successfully updated")