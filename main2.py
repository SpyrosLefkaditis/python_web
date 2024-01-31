import urllib.request
import re

business_type = str(input("Enter the type of business you want to scrape: "))
site_num = int(input("Enter the number of sites you want to scrape: "))

def scrape_from_container(url, container_id):
    try:
        # Replace spaces in the business type with '+' cause of the logic of the links
        modified_business_type = business_type.replace(' ', '+')

        # Modify the container ID in the URL
        container_url = f'{url}?what={modified_business_type}&lang=en&container_id={container_id}'  # Adjust this part based on your actual URL structure

        # Open the URL and read the HTML content
        with urllib.request.urlopen(container_url) as response:
            html_content = response.read().decode('utf-8')

        # Modify the regex pattern to match the specific structure of the container
        website_match = re.search(r'<div class="listingWhiteArea" id="listingContainer' + str(container_id) + r'".*?<a class="et-v2-additional" .*? href="(.*?)" itemprop="url" .*?>', html_content, re.DOTALL)

        # Check if the match is found
        if website_match:
            website_link = website_match.group(1).strip()

            # Print the extracted website link
            print(f"Container {container_id} Website: {website_link}")
        else:
            print(f"Container {container_id} Website link not found on the page.")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
url_to_scrape = 'https://www.xo.gr/search/'

# Loop through specified number of sites
for container_id in range(1, site_num+1):
    scrape_from_container(url_to_scrape, container_id)

#we need to use  this type of logic for seo test and make rpecentage def check_seo(url):
    # Create a Web3 object
   # w3 = web3.Web3()

    # Fetch SEO-related information for the given URL
   # seo_info = w3.fetch(url)

    # Print the SEO information
  #  print(f"SEO information for {url}:")
  #  print(f"Title: {seo_info.title}")
  #  print(f"Meta Description: {seo_info.meta_description}")
 #   print(f"Meta Keywords: {seo_info.meta_keywords}")
#    print(f"Headers: {seo_info.headers}")

# Example usage
#url_to_check = 'https://example.com'

# and we also need to  impelment the logic to jump to the next page 
#after al this pyautogui for us for commecila use we need to impement more search engines and we also need html css template and django and server and firebase for authencitncation strip payment

