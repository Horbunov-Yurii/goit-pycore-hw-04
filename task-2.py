def get_cats_info(path: str) -> list:
    cats_list = []
    try:
        with open(path, encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
            
                if len(parts) == 3:
                    cat_id, name, age = parts
                    cats_list.append({"id": cat_id, "name": name, "age": age})
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")
    
    return cats_list


cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)
      