from math import ceil


class PhotoAlbum:

    MAX_PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for x in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(ceil(photos_count / cls.MAX_PHOTOS_PER_PAGE))

    def add_photo(self, label):
        for page in range(len(self.photos)):
            if len(self.photos[page]) < self.MAX_PHOTOS_PER_PAGE:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"

        return "No more free slots"

    def display(self):
        output = ["-" * 11]
        for row in self.photos:
            output.append(("[] " * len(row)).rstrip())
            output.append("-" * 11)

        return '\n'.join(output)


album = PhotoAlbum(2)
print(album.photos)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
