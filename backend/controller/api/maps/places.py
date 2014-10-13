from googleplaces import GooglePlaces, types, lang

YOUR_API_KEY = 'AIzaSyBqQJdkBvJy1RY1gzGU4UeIszEIFGfWnj0'

google_places = GooglePlaces(YOUR_API_KEY)
term = 'Local Yogurt'
# You may prefer to use the text_search API, instead.
query_result = google_places.nearby_search(
        location='Durham, NC', keyword=term, name=term,
        radius=20000)

if query_result.has_attributions:
    print query_result.html_attributions


for place in query_result.places:
    # Returned places from a query are place summaries.
    print place.name
    print place.geo_location
    print place.reference


