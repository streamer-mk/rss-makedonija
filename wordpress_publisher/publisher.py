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
    "categories": [https://streamer-tv.great-site.net/wp-admin/term.php?taxonomy=category&tag_ID=271]
       
}

    }

    response = requests.post(f"{wp_url}/wp-json/wp/v2/posts", json=data, auth=auth, headers=headers)
    print("Posted to WordPress:", response.status_code, response.text)
