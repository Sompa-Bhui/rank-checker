# from flask import Flask, request, jsonify
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# app = Flask(__name__)

# @app.route("/api/rank")
# def rank_api():
#     keyword = request.args.get("keyword")
#     domain = request.args.get("domain")

#     if not keyword or not domain:
#         return jsonify({"error": "keyword and domain required"})

#     options = webdriver.ChromeOptions()
#     driver = webdriver.Chrome(options=options)

#     driver.get("https://www.google.com")

#     time.sleep(2)

#     # 🔍 Search
#     search = driver.find_element(By.NAME, "q")
#     search.send_keys(keyword)
#     search.send_keys(Keys.RETURN)

#     print("\n👉 STEP 1: CAPTCHA solve karo (agar aaye)")
#     print("👉 STEP 2: Page ko thoda scroll karo (important)")
#     print("👉 STEP 3: Jab results clearly dikh jaye → ENTER dabao")

#     input("👉 READY ho jao phir ENTER dabao...")

#     time.sleep(2)

#     results = driver.find_elements(By.CSS_SELECTOR, "div.tF2Cxc")

#     rank = -1
#     count = 0

#     for result in results:
#         try:
#             link = result.find_element(By.TAG_NAME, "a")
#             href = link.get_attribute("href")

#             if href and domain in href:
#                 rank = count + 1
#                 break

#             count += 1

#         except:
#             continue

#     driver.quit()

#     return jsonify({
#         "keyword": keyword,
#         "domain": domain,
#         "rank": rank
#     })

# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, request, jsonify
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# app = Flask(__name__)

# @app.route("/api/rank")
# def rank_api():
#     keyword = request.args.get("keyword")
#     domain = request.args.get("domain")

#     options = webdriver.ChromeOptions()
#     driver = webdriver.Chrome(options=options)

#     driver.get("https://www.google.com")

#     time.sleep(2)

#     search = driver.find_element(By.NAME, "q")
#     search.send_keys(keyword)
#     search.send_keys(Keys.RETURN)

#     print("👉 CAPTCHA solve karo + scroll karo")

#     input("👉 READY ho jao phir ENTER dabao...")

#     rank = -1
#     current_position = 0

#     for page in range(5):  # 🔥 5 pages = top 50 results

#         time.sleep(3)

#         results = driver.find_elements(By.CSS_SELECTOR, "div.tF2Cxc")

#         for result in results:
#             try:
#                 link = result.find_element(By.TAG_NAME, "a")
#                 href = link.get_attribute("href")

#                 current_position += 1

#                 if domain in href:
#                     rank = current_position
#                     driver.quit()
#                     return jsonify({
#                         "keyword": keyword,
#                         "domain": domain,
#                         "rank": rank
#                     })

#             except:
#                 continue

#         # 🔥 Next page
#         try:
#             next_btn = driver.find_element(By.ID, "pnnext")
#             next_btn.click()
#         except:
#             break

#     driver.quit()

#     return jsonify({
#         "keyword": keyword,
#         "domain": domain,
#         "rank": -1
#     })


# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, request, jsonify
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# app = Flask(__name__)
# app.config['JSON_SORT_KEYS'] = False


# def get_rank(driver, keyword, domain):
#     try:
#         search = driver.find_element(By.NAME, "q")
#         search.clear()
#         search.send_keys(keyword)
#         search.send_keys(Keys.RETURN)

#         print("👉 CAPTCHA solve karo + scroll karo")
#         input("👉 READY ho jao phir ENTER dabao...")

#         current_position = 0

#         for page in range(5):  # top 50
#             time.sleep(5)

#             results = driver.find_elements(By.CSS_SELECTOR, "div.tF2Cxc")

#             if not results:
#                 print("⚠️ Results load nahi hue, retrying...")
#                 time.sleep(3)
#                 continue

#             for result in results:
#                 try:
#                     link = result.find_element(By.TAG_NAME, "a")
#                     href = link.get_attribute("href")

#                     current_position += 1

#                     if href and domain in href:
#                         return current_position

#                 except:
#                     continue

#             try:
#                 next_btn = driver.find_element(By.ID, "pnnext")
#                 next_btn.click()
#             except:
#                 break

#         return "Above 50"

#     except Exception as e:
#         print("❌ ERROR:", e)
#         return "API Failed"


# @app.route("/api/rank")
# def rank_api():
#     keyword = request.args.get("keyword")
#     domain = request.args.get("domain")
#     location = request.args.get("location")  # NEW 🔥

#     options = webdriver.ChromeOptions()
#     driver = webdriver.Chrome(options=options)

#     try:
#         # 🌍 LOCATION MAP
#         if location.lower() == "india":
#             url = "https://www.google.com/?hl=en&gl=in"
#         elif location.lower() == "usa":
#             url = "https://www.google.com/?hl=en&gl=us"
#         elif location.lower() == "canada":
#             url = "https://www.google.com/?hl=en&gl=ca"
#         else:
#             return jsonify({
#                 "error": "Invalid location (choose India, USA, Canada)"
#             })

#         driver.get(url)
#         time.sleep(2)

#         rank = get_rank(driver, keyword, domain)

#     except Exception as e:
#         print("❌ DRIVER ERROR:", e)
#         rank = "API Failed"

#     driver.quit()

#     return jsonify({
#         "keyword": keyword,
#         "domain": domain,
#         "location": location,
#         "rank": rank
#     })


# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, request, jsonify
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# app = Flask(__name__)
# app.config['JSON_SORT_KEYS'] = False


# def get_rank(driver, domain):
#     try:
#         current_position = 0

#         for page in range(5):  # top 50
#             time.sleep(4)

#             results = driver.find_elements(By.CSS_SELECTOR, "div.tF2Cxc")

#             if not results:
#                 time.sleep(2)
#                 continue

#             for result in results:
#                 try:
#                     link = result.find_element(By.TAG_NAME, "a")
#                     href = link.get_attribute("href")

#                     current_position += 1

#                     if href and domain in href:
#                         return current_position

#                 except:
#                     continue

#             try:
#                 next_btn = driver.find_element(By.ID, "pnnext")
#                 next_btn.click()
#             except:
#                 break

#         return "Above 50"

#     except:
#         return "API Failed"


# @app.route("/api/rank")
# def rank_api():
#     keyword = request.args.get("keyword")
#     domain = request.args.get("domain")
#     location = request.args.get("location")

#     options = webdriver.ChromeOptions()

#     # ✅ REAL USER SIMULATION
#     options.add_argument("--start-maximized")
#     options.add_argument(
#         "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
#         "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
#     )

#     options.add_argument(r"user-data-dir=C:/chrome-profile")

#     driver = webdriver.Chrome(options=options)

#     try:
#         keyword_encoded = keyword.replace(" ", "+")

#         # ✅ SINGLE LOCATION SEARCH
#         if location.lower() == "india":
#             url = f"https://www.google.com/search?q={keyword_encoded}&hl=en&gl=in&pws=0"
#         elif location.lower() == "usa":
#             url = f"https://www.google.com/search?q={keyword_encoded}&hl=en&gl=us&pws=0"
#         elif location.lower() == "canada":
#             url = f"https://www.google.com/search?q={keyword_encoded}&hl=en&gl=ca&pws=0"
#         else:
#             return jsonify({"error": "Invalid location (india/usa/canada)"})

#         driver.get(url)

#         print("👉 CAPTCHA solve karo + scroll karo")
#         input("👉 ENTER dabao")

#         rank = get_rank(driver, domain)

#     except Exception as e:
#         print("ERROR:", e)
#         rank = "API Failed"

#     driver.quit()

#     return jsonify({
#         "keyword": keyword,
#         "domain": domain,
#         "location": location,
#         "rank": rank
#     })


# if __name__ == "__main__":
#     app.run(debug=True)





# from flask import Flask, request, jsonify
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# app = Flask(__name__)
# app.config['JSON_SORT_KEYS'] = False


# def get_rank(driver, keyword, domain):
#     try:
#         search = driver.find_element(By.NAME, "q")
#         search.clear()
#         search.send_keys(keyword)
#         search.send_keys(Keys.RETURN)

#         print("👉 CAPTCHA solve karo + scroll karo")
#         input("👉 READY ho jao phir ENTER dabao...")

#         current_position = 0

#         for page in range(5):  # top 50
#             time.sleep(5)

#             results = driver.find_elements(By.CSS_SELECTOR, "div.tF2Cxc")

#             if not results:
#                 print("⚠️ Results load nahi hue, retrying...")
#                 time.sleep(3)
#                 continue

#             for result in results:
#                 try:
#                     link = result.find_element(By.TAG_NAME, "a")
#                     href = link.get_attribute("href")

#                     current_position += 1

#                     if href and domain in href:
#                         return current_position

#                 except:
#                     continue

#             try:
#                 next_btn = driver.find_element(By.ID, "pnnext")
#                 next_btn.click()
#             except:
#                 break

#         return "Above 50"

#     except Exception as e:
#         print("❌ ERROR:", e)
#         return "API Failed"


# @app.route("/api/rank")
# def rank_api():
#     keyword = request.args.get("keyword")
#     domain = request.args.get("domain")
#     location = request.args.get("location")  # NEW 🔥

#     options = webdriver.ChromeOptions()
#     driver = webdriver.Chrome(options=options)

#     try:
#         # 🌍 LOCATION MAP
#         if location.lower() == "india":
#             url = "https://www.google.com/?hl=en&gl=in"
#         elif location.lower() == "usa":
#             url = "https://www.google.com/?hl=en&gl=us"
#         elif location.lower() == "canada":
#             url = "https://www.google.com/?hl=en&gl=ca"
#         else:
#             return jsonify({
#                 "error": "Invalid location (choose India, USA, Canada)"
#             })

#         driver.get(url)
#         time.sleep(2)

#         rank = get_rank(driver, keyword, domain)

#     except Exception as e:
#         print("❌ DRIVER ERROR:", e)
#         rank = "API Failed"

#     driver.quit()

#     return jsonify({
#         "keyword": keyword,
#         "domain": domain,
#         "location": location,
#         "rank": rank
#     })


# if __name__ == "__main__":
#     app.run(debug=True)


# import requests

# API_KEY = "e8468c5e9a056abf61106e2ff915b4a19213d8d53cfa2a4397ab525b57fa8c18"

# def get_rank(keyword, domain):
#     url = "https://serpapi.com/search.json"

#     params = {
#         "q": keyword,
#         "location": "Canada",
#         "gl": "ca",
#         "hl": "en",
#         "engine": "google",
#         "num": 20,
#         "api_key": API_KEY
#     }

#     response = requests.get(url, params=params)

#     if response.status_code != 200:
#         print("API Error:", response.status_code)
#         print(response.text)
#         return -1

#     data = response.json()
#     results = data.get("organic_results", [])

#     print("\n--- DEBUG RESULTS ---")
#     for r in results:
#         print(r.get("position"), r.get("link"))

#     for result in results:
#         link = result.get("link", "")
#         position = result.get("position", 0)

#         if domain.lower() in link.lower():
#             return position

#     return "Not found"


# # 🔥 TEST (Facebook)
# print("\nFacebook Rank:", get_rank("facebook login", "facebook.com"))


# import requests

# API_KEY = "e8468c5e9a056abf61106e2ff915b4a19213d8d53cfa2a4397ab525b57fa8c18"

# def get_rank(keyword, domain):
#     url = "https://serpapi.com/search.json"

#     params = {
#         "q": keyword,
#         "location": "Florida, United States",  # 🇺🇸 USA specific
#         "gl": "us",
#         "hl": "en",
#         "engine": "google",
#         "num": 100,
#         "api_key": API_KEY
#     }

#     response = requests.get(url, params=params)

#     if response.status_code != 200:
#         print("API Error:", response.status_code)
#         print(response.text)
#         return -1

#     data = response.json()
#     results = data.get("organic_results", [])

#     print("\n--- DEBUG (Top Results) ---")
#     for r in results[:20]:
#         print(r.get("position"), r.get("link"))

#     for result in results:
#         link = result.get("link", "")
#         position = result.get("position", 0)

#         if domain.lower() in link.lower():
#             return position

#     return "Not found"


# # 🔥 TEST
# print("\nRank:", get_rank("boat injury expert witness Florida", "almaritimeexperts.com"))





# from flask import Flask, request, jsonify, render_template
# import requests

# app = Flask(__name__)

# API_KEY = "YOUR_API_KEY_HERE"  # 👈 apni SerpApi key daal

# def get_rank(keyword, domain):
#     url = "https://serpapi.com/search.json"

#     params = {
#         "q": keyword,
#         "location": "India",   # change kar sakti hai
#         "gl": "in",
#         "hl": "en",
#         "engine": "google",
#         "num": 100,
#         "api_key": API_KEY
#     }

#     response = requests.get(url, params=params)

#     if response.status_code != 200:
#         print("API Error:", response.status_code)
#         print(response.text)
#         return -1

#     data = response.json()
#     results = data.get("organic_results", [])

#     for result in results:
#         link = result.get("link", "")
#         position = result.get("position", 0)

#         if domain.lower() in link.lower():
#             return position

#     return "Not found"


# # 👇 homepage (HTML serve karega)
# @app.route("/")
# def home():
#     return render_template("index.html")


# # 👇 API route
# @app.route("/api/rank")
# def rank():
#     keyword = request.args.get("keyword")
#     domain = request.args.get("domain")

#     result = get_rank(keyword, domain)

#     return jsonify({
#         "keyword": keyword,
#         "domain": domain,
#         "rank": result
#     })


# if __name__ == "__main__":
#     app.run(debug=True)




# from flask import Flask, request, jsonify, render_template
# import requests

# app = Flask(__name__)

# API_KEY = "e8468c5e9a056abf61106e2ff915b4a19213d8d53cfa2a4397ab525b57fa8c18"  


# def get_rank(keyword, domain):
#     url = "https://serpapi.com/search.json"

#     params = {
#         "q": keyword,
#         "location": "India",
#         "gl": "in",
#         "hl": "en",
#         "engine": "google",
#         "num": 100,
#         "api_key": API_KEY
#     }

#     try:
#         response = requests.get(url, params=params)

#         if response.status_code != 200:
#             return "API Error"

#         data = response.json()
#         results = data.get("organic_results", [])

#         for result in results:
#             link = result.get("link", "")
#             position = result.get("position", 0)

#             if domain.lower() in link.lower():
#                 return position

#         return "Not found"

#     except Exception as e:
#         print("Error:", e)
#         return "Error"


# # ✅ homepage
# @app.route("/")
# def home():
#     return render_template("index.html")


# # ✅ API route
# @app.route("/api/rank")
# def rank():
#     keyword = request.args.get("keyword")
#     domain = request.args.get("domain")

#     if not keyword or not domain:
#         return jsonify({"error": "keyword and domain required"})

#     result = get_rank(keyword, domain)

#     return jsonify({
#         "keyword": keyword,
#         "domain": domain,
#         "rank": result
#     })


# app = app




# from flask import Flask, request, jsonify, render_template
# import requests
# import os

# app = Flask(__name__)

# SERP_API_KEY = os.environ.get("e8468c5e9a056abf61106e2ff915b4a19213d8d53cfa2a4397ab525b57fa8c18")

# # simple usage counter (reset on deploy)
# usage_count = 0

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/api/rank")
# def get_rank():
#     global usage_count
#     usage_count += 1

#     keyword = request.args.get("keyword")
#     domain = request.args.get("domain")
#     location = request.args.get("location")
#     device = request.args.get("device")

#     url = "https://serpapi.com/search.json"

#     params = {
#         "q": keyword,
#         "api_key": SERP_API_KEY,
#         "location": location,
#         "device": device
#     }

#     res = requests.get(url, params=params)
#     data = res.json()

#     rank = "Not found"

#     if "organic_results" in data:
#         for i, result in enumerate(data["organic_results"], start=1):
#             if domain in result.get("link", ""):
#                 rank = i
#                 break

#     return jsonify({
#         "rank": rank,
#         "usage": usage_count
#     })

# if __name__ == "__main__":
#     app.run()


from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# 🔑 DataForSEO credentials
LOGIN = "YOUR_EMAIL"
PASSWORD = "YOUR_PASSWORD"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/rank")
def get_rank():
    keyword = request.args.get("keyword")
    domain = request.args.get("domain")
    location = request.args.get("location")

    url = "https://api.dataforseo.com/v3/serp/google/organic/live/regular"

    payload = [{
        "keyword": keyword,
        "location_name": location,
        "language_code": "en",
        "depth": 100
    }]

    try:
        response = requests.post(url, json=payload, auth=(LOGIN, PASSWORD))
        data = response.json()

        rank = "Not found"

        results = data["tasks"][0]["result"][0]["items"]

        position = 1

        for item in results:
            link = item.get("url", "")
            if domain.lower() in link.lower():
                rank = position
                break
            position += 1

        return jsonify({"rank": rank})

    except Exception as e:
        return jsonify({"error": str(e)})


app = app