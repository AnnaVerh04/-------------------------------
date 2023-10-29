import urllib.request
import argparse
import concurrent.futures

# Функция для загрузки изображений по URL-адресу
def download_image(url):
    # Извлекаем имя файла из URL-адреса
    filename = url.split("/")[-1]
    
    try:
        # Скачиваем изображение
        urllib.request.urlretrieve(url, filename)
        print(f"Загружено изображение {filename}")
    except Exception as e:
        print(f"Ошибка при загрузке изображения {filename}: {e}")

def main():
    # Создаем парсер аргументов командной строки
    parser = argparse.ArgumentParser(description="Загрузка изображений из списка URL-адресов")
    parser.add_argument("urls", nargs="+", help="URL-адреса изображений")
    
    # Парсим аргументы командной строки
    args = parser.parse_args()
    urls = args.urls
    
    # Используем ThreadPoolExecutor для распараллеливания загрузки изображений
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Запускаем задачи параллельно
        executor.map(download_image, urls)
    
    print("Загрузка завершена")

if __name__ == "__main__":
    main()