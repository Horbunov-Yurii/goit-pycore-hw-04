def total_salary(path: str) -> tuple:
    with open(path, mode="r", encoding="utf-8") as file:
        lines = file.readlines()
        total = 0
        for line in lines:
            res = line.split(',')
            res1 = int(res[1].strip())
            total += res1
            
           


    return total, total / len(lines)



total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
