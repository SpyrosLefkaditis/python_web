import urllib.request

def simple_web_scrape(url):
    try:
        # Open the URL and read the HTML content
        with urllib.request.urlopen(url) as response:
            html_content = response.read().decode('utf-8')

        # Simple string manipulation to extract data
        start_index = html_content.find('<li itemscope="" itemtype="https://schema.org/Hotel" class="span12 listing spListing links_list" data-label="14208" data-aid="4249" data-ltype="2"> <div class="listingWhiteArea" id="listingContainer1" data-adid="SAE805802873">') + len('<li itemscope="" itemtype="https://schema.org/Hotel" class="span12 listing spListing links_list" data-label="14208" data-aid="4249" data-ltype="2"> <div class="listingWhiteArea" id="listingContainer1" data-adid="SAE805802873">')
        end_index = html_content.find('</li>', start_index)
        title = html_content[start_index:end_index].strip()

        # Print the extracted data
        print(f"Title: {title}")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
url_to_scrape = 'https://www.xo.gr/search/?what=hotels&lang=en'
simple_web_scrape(url_to_scrape)
#to string pou kanei extract ta data tha allazei ana selida me to listingContainerX, pou x einai to kathe listing ana selida
#meta olo auto tha mpei se mia loopa opou tha koitaei gia kathe listing 
#free api SEO
#if (seo_rate < 0.6 ): fetch website, give info