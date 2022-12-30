from requests_html import HTMLSession

def get_source(url):
    session = HTMLSession()
    response = session.get(url)
    return response

def scrape_google(query):

    response = get_source("https://www.google.co.in/search?q=" + query)

    links = list(response.html.absolute_links)
    google_domains = ('https://www.google.',
                      'https://google.',
                      'https://webcache.googleusercontent.',
                      'http://webcache.googleusercontent.',
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')

    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)
    return links  # Returns a list of search results

def query_func(data):
    search_text = data['queryResult']['parameters']['any'].split(" ")
    query = ''
    for i in range(len(search_text)):
        if i != len(search_text)-1:
            query += str(search_text[i])+'+'
        else:
            query += str(search_text[i])
    links = scrape_google(query)
    output = 'Below are your search results.\n\n\n------------------\n\n\n'
    for i in links[:5]:
        output += f"{i}\n\n"

    result = {
        'fulfillmentText': output
    }
    print(search_text)
    return result

