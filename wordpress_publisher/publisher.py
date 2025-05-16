import os
import requests
from dotenv import load_dotenv

load_dotenv()

def publish_to_wordpress(article):
    wp_url = os.getenv("WORDPRESS_URL")
    wp_user = os.getenv("WORDPRESS_USER")
    wp_app_password = os.getenv("WORDPRESS_APP_PASSWORD")

    auth = (wp_user, wp_app_password)
    headers = {"Content-Type": "application/json"}
   data = {
    "title": article["title"],
    "content": f"<a href='{article['link']}'>Прочитај ја целата статија</a>",
    "status": "publish",
    "categories": [https://streamer-tv.great-site.net/wp-admin/term.php?taxonomy=category&tag_ID=271&post_type=post&wp_http_referer=%2Fwp-admin%2Fedit-tags.php%3Ftaxonomy%3Dcategory%26post_type%3Dpost%26s%3D%25D0%259C%25D0%2590%25D0%259A%25D0%2595]
       
}

    }

    response = requests.post(f"{wp_url}/wp-json/wp/v2/posts", json=data, auth=auth, headers=headers)
    print("Posted to WordPress:", response.status_code, response.text)
