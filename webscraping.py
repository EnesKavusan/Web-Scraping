import json
from selenium import webdriver
from selenium.webdriver.common.by import By

# WebDriver'ı başlatın
driver = webdriver.Chrome()  # Chrome için örnek olarak kullanıldı, diğer tarayıcılar için uygun WebDriver'ı seçin

# Web sitesine gidin
driver.get("https://www.doktorsitesi.com/uzmanlik-alanlari/kadin-hastaliklari-ve-dogum/istanbul")  # Scraping yapmak istediğiniz web sitesinin URL'sini buraya ekleyin

# Hedef verileri çekin
h2_elements = driver.find_elements(By.CSS_SELECTOR, "h2.expert-card-title")
div_cities = driver.find_elements(By.CSS_SELECTOR, "div.card-city")
div_addresses = driver.find_elements(By.CSS_SELECTOR, "div.ta-address-explain")
div_branches = driver.find_elements(By.CSS_SELECTOR, "div.card-branch")
div_expert_points = driver.find_elements(By.CSS_SELECTOR, "div.expert-point")
div_feedbacks = driver.find_elements(By.CSS_SELECTOR, "div.feedback-text")

# Verileri saklamak için bir liste oluşturun
data = []

# Verileri döngüye alın ve listeye ekleyin
for h2_element, city, address, branch, expert_point, feedback in zip(h2_elements, div_cities, div_addresses, div_branches, div_expert_points, div_feedbacks):
    feedback_text = feedback.text.replace("Değerlendirme", "").strip()  # "Değerlendirme" yazısını kaldırın
    try:
        feedback_value = int(feedback_text)  # Geribildirim değerini int türüne dönüştürün
    except ValueError:
        feedback_value = None  # Dönüşüm yapılamazsa None olarak ayarlayın
    doctor_data = {
        "name": h2_element.text,
        "place": city.text,
        "address": address.text,
        "profession": branch.text,
        "star": expert_point.text,
        "commentCount": feedback_value
    }
    data.append(doctor_data)

# WebDriver'ı kapatın
driver.quit()

# Verileri JSON formatında bir metin dosyasına yazdırın
with open("veriler.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Veriler başarıyla JSON dosyasına yazıldı.")
