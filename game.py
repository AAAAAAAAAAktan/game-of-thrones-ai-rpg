import time
import sys

# Функция для имитации "печатной машинки" (атмосферный вывод текста)
def print_slow(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Класс, описывающий состояние игры
class GameState:
    def __init__(self):
        self.player_name = "Брандон Старк"
        self.stark_loyalty = 100
        self.lannister_threat = 50
        self.gold = 500
        self.army_size = 2000
        self.is_running = True

# Класс для персонажей (Генерация имен и диалогов ИИ)
class Character:
    def __init__(self, name, title, description):
        self.name = name
        self.title = title
        self.description = description

    def speak(self, dialogue):
        print(f"\n--- {self.name.upper()}, {self.title.upper()} ---")
        print_slow(dialogue)

# --- ИНИЦИАЛИЗАЦИЯ ДАННЫХ (Часть, которую может генерировать ИИ) ---

# Статические данные персонажей (соответствуют сгенерированным картинкам)
hoster_stark = Character(
    "Хостер Старк",
    "Кастелян Винтерфелла",
    "Старый, умудренный опытом человек, чье лицо покрыто шрамами от старых битв. Его глаза серьезны." # См. image_1.png
)

lyanna_mormont = Character(
    "Лианна Мормонт",
    "Леди Медвежьего Острова",
    "Молодая, но суровая воительница. Ее взгляд пронзителен, а воля несгибаема." # См. image_2.png
)

# --- ИГРОВАЯ ЛОГИКА ---

def show_intro():
    print("\n" + "="*60)
    print("      GAME OF THRONES: WINTER'S WRATH (AI EDITION)")
    print("="*60 + "\n")
    print_slow("На дворе — суровая зима. Королевская Гавань далеко.")
    print_slow("Винтерфелл стоит твердо, но тени Львов Ланнистеров сгущаются...")
    print("\n[Используйте image_0.png как фон для этой сцены]")
    time.sleep(1)

def show_status(state):
    print("\n" + "-"*30)
    print(f"СТАТУС: {state.player_name}")
    print(f"Лояльность Севера: {state.stark_loyalty}%")
    print(f"Угроза Ланнистеров: {state.lannister_threat}%")
    print(f"Золото в казне: {state.gold}")
    print(f"Размер армии: {state.army_size}")
    print("-"*30 + "\n")

def scene_1_great_hall(state):
    print("\n[Вход в сцену: Великий Чертог Винтерфелла. См. image_0.png]")
    time.sleep(1)
    hoster_stark.speak(
        f"Добро пожаловать, {state.player_name}. Время пришло. Мои вороны докладывают,\n"
        f"что Ланнистеры собирают войска у Трезубца. Наш долг — защитить Север."
    )
    
    # ПРИМЕР: ИИ может генерировать эти варианты выбора в реальном времени
    print("\nВаши действия, Лорд?")
    print("1. [СТРАТЕГИЯ] Собрать знамена и укрепить Ров Кайлин (+Лояльность, -Золото)")
    print("2. [ДИПЛОМАТИЯ] Отправить ворона с предложением мира (Риск, но экономия ресурсов)")
    print("3. [ШПИОНАЖ] Послать лазутчиков в Утес Кастерли (+Интерес, -Золото)")

    choice = input("\nВедите номер выбора (1-3): ")

    if choice == "1":
        print_slow("\nВы отдаете приказ собрать знамена. Север откликается на зов!")
        state.stark_loyalty += 15
        state.gold -= 200
        state.army_size += 1000
    elif choice == "2":
        print_slow("\nВаше письмо улетело. Но Ланнистеры не знают чести...")
        state.lannister_threat += 10
    elif choice == "3":
        print_slow("\nВаши шпионы отправляются на юг. Интеллект — это сила.")
        state.gold -= 100
        # ИИ может сгенерировать событие успеха шпионажа позже
    else:
        print_slow("\nВы медлите. Секунды стоят жизней.")

def scene_2_mormont_arrival(state):
    print("\n[Вход в сцену: Через Чертог проходит Капитан Лианна. См. image_2.png]")
    time.sleep(1)
    lyanna_mormont.speak(
        "Мой Лорд! Медвежий Остров с вами. Но мы не можем просто ждать.\n"
        "Ланнистеры подкупают горные кланы. Нам нужно действовать агрессивно."
    )

    print("\nВаше решение?")
    print("1. [АТАКА] Позволить Лианне возглавить авангард и ударить по кланам (+Слава, Риск армии)")
    print("2. [ЗАЩИТА] Укрепить стены Винтерфелла и ждать зимы (+Безопасность, -Лояльность Мормонтов)")

    choice = input("\nВедите номер выбора (1-2): ")

    if choice == "1":
        print_slow("\nЛианна улыбается. 'Они узнают мощь Медведя!' Она уходит.")
        state.army_size -= 200 # Потери
        state.lannister_threat -= 15
    elif choice == "2":
        print_slow("\nЛианна хмурится. 'Выбор Лорда — закон. Но Север запомнит это.'")
        state.stark_loyalty -= 10
    else:
        print_slow("\nВыбор не сделан.")

# --- ОСНОВНОЙ ЦИКЛ ИГРЫ ---

def main():
    state = GameState()
    show_intro()
    
    while state.is_running:
        show_status(state)
        
        # Первая сцена
        scene_1_great_hall(state)
        show_status(state)
        time.sleep(1)
        
        # Вторая сцена
        scene_2_mormont_arrival(state)
        
        # Простая проверка условий окончания
        if state.stark_loyalty < 50:
            print_slow("\nСевер отвернулся от вас. Игра окончена.")
            state.is_running = False
        elif state.lannister_threat < 20:
            print_slow("\nВы сокрушили угрозу Львов! Победа за Волками.")
            state.is_running = False
        else:
            # ПРИМЕР: Здесь ИИ мог бы сгенерировать следующую уникальную сцену
            print_slow("\nЗима близко. Война продолжается...")
            break # Пока прервем цикл для демонстрации

if __name__ == "__main__":
    main()