import urllib.request
import re

business_type = str(input("Enter the type of business you want to scrape: "))
site_num = int(input("Enter the number of sites you want to scrape: "))
# Replace spaces in the business type with '+' cause of the logic of the links
business_type = business_type.replace(' ', '+')
pagenum = int(site_num/ 19)
pagenum_mod = int(site_num  % 19)
# Example usage
url_to_scrape = 'https://www.xo.gr/search/'

def scrape_from_container(url, container_id,pagenum):
    try:
        
        # Modify the container ID in the URL
        container_url = f'{url}?what={business_type}&lang=en&container_id={container_id}&page={pagenum}'  # Adjust this part based on your actual URL structure
        print(container_url)
        # Open the URL and read the HTML content
        with urllib.request.urlopen(container_url) as response:
            html_content = response.read().decode('utf-8')

        # Modify the regex pattern to match the specific structure of the container
        website_match = re.search(r'<div class="listingWhiteArea" id="listingContainer' + str(container_id) + r'".*?<a class="et-v2-additional" .*? href="(.*?)" itemprop="url" .*?>', html_content, re.DOTALL)

        # Check if the match is found
        if website_match:
            website_link = website_match.group(1).strip()

            # Print the extracted website link
            print(f"Container {container_id} Page: {pagenum} Website: {website_link}")
        else:
            print(f"Container {container_id} Page: {pagenum} Website link not found on the page.")

    except Exception as e:
        print(f"Error: {e}")
if site_num <= 19 :
        x = 1
        for container_id in range(1, site_num+1):
            scrape_from_container(url_to_scrape, container_id,x)
else:
    for x in range(1, pagenum+1):
        for container_id in range(1, 19):
            scrape_from_container(url_to_scrape, container_id,x)
        
    
    

       
    