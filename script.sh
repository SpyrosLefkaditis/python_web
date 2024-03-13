#!/bin/bash

read -p "Enter the type of business you want to scrape: " business_type
read -p "Enter the number of sites you want to scrape: " site_num

# Replace spaces in the business type with '+' cause of the logic of the links
business_type=$(echo "$business_type" | sed 's/ /+/g')
pagenum=$((site_num / 19))
pagenum_mod=$((site_num % 19))

# Example usage
url_to_scrape='https://www.xo.gr/search/'

function scrape_from_container {
    container_url="$1?what=$business_type&lang=en&container_id=$2&page=$3"
    echo "$container_url"
    html_content=$(wget -qO- "$container_url")
    website_match=$(echo "$html_content" | grep -oP '<div class="listingWhiteArea" id="listingContainer'$2'".*?<a class="et-v2-additional" .*? href="\K[^"]+' | head -n 1)

    if [ -n "$website_match" ]; then
        echo "Container $2 Page: $3 Website: $website_match"
    else
        echo "Container $2 Page: $3 Website link not found on the page."
    fi
}

if [ "$site_num" -le 19 ]; then
    for (( container_id=1; container_id<=site_num; container_id++ )); do
        scrape_from_container "$url_to_scrape" "$container_id" 1
    done
else
    for (( x=1; x<=pagenum; x++ )); do
        if [ "$x" -eq 1 ]; then
            start_page=1
        else
            start_page=2
        fi

        for (( container_id=1; container_id<=19; container_id++ )); do
            scrape_from_container "$url_to_scrape" "$container_id" "$start_page"
        done
    done

    if [ "$pagenum_mod" -gt 0 ]; then
        for (( container_id=1; container_id<=pagenum_mod; container_id++ )); do
            scrape_from_container "$url_to_scrape" "$container_id" "$((pagenum+1))"
        done
    fi
fi
