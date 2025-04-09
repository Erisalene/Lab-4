text = "Python — це мова програмування, яка дозволяє швидко розробляти проєкти будь-якої складності. Вона є простою у вивченні, потужною у застосуванні та має велику спільноту."

# === Студент 1: Давиденко Федір ===
# Операції:
# - lower(): зниження регістру
# - count(): підрахунок символів
# - replace(): заміна слів
# - split(): поділ тексту на слова
# - find(): знайти позицію підрядка
# - startswith(): перевірка початку рядка

lower_text = text.lower()
count_u = lower_text.count("у")
replaced_text = lower_text.replace("python", "Пайтон")

print("=== Студент 1: Давиденко Федір ===")
print("Текст у нижньому регістрі:\n", lower_text)
print("Кількість символів 'у':", count_u)
print("Текст із заміною слова 'python':\n", replaced_text)


# === Студент 2: Давиденко Федір ===
# Операції:
# - split(): поділ тексту на слова
# - find(): знайти позицію підрядка
# - startswith(): перевірка початку рядка

words = text.split()
position = text.find("розробляти")
starts_with_python = text.startswith("Python")

print("=== Студент 2: Давиденко Федір ===")
print("Список слів:", words)
print("Позиція слова 'розробляти':", position)
print("Чи починається текст зі слова 'Python'?:", starts_with_python)
