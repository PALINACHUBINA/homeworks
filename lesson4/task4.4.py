string = 'Петя ел Еленину кофету, а Елена съела его суп.'

count = 0
for word in string.split():
    if word.startswith('е'):
        count += 1
print(f"В строке {count} слова начинающихся на букву 'е'.")