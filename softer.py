import os
import sys
import time
import random
import threading
from datetime import datetime

class DDoSTool:
    def __init__(self):
        self.version = "v3.0.0"
        self.session_id = self.generate_session_id()
        self.attack_active = False
        self.threads = []
        self.target_ip = ""
        self.target_port = 80
        self.bot_count = 0
        self.packets_sent = 0
        self.attack_start_time = None
        
    def generate_session_id(self):
        return f"DDoS{random.randint(1000,9999)}-{int(time.time())}"
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def typewriter_effect(self, text, delay=0.03):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def loading_animation(self, text, duration=2):
        symbols = ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷']
        end_time = time.time() + duration
        i = 0
        
        while time.time() < end_time:
            print(f"\r\033[91m{symbols[i % len(symbols)]} {text}\033[0m", end="")
            time.sleep(0.1)
            i += 1
        print("\r\033[92m✓ {}\033[0m".format(text))

    def show_banner(self):
        banner = f"""
\033[91m
    ██████╗ ██████╗  ██████╗ ███████╗    ██████╗ ██████╗  ██████╗ ███████╗
    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
    ██║  ██║██║  ██║██║   ██║███████╗    ██║  ██║██║  ██║██║   ██║███████╗
    ██║  ██║██║  ██║██║   ██║╚════██║    ██║  ██║██║  ██║██║   ██║╚════██║
    ██████╔╝██████╔╝╚██████╔╝███████║    ██████╔╝██████╔╝╚██████╔╝███████║
    ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
    
    ╔═══════════════════════════════════════════════════════════════╗
    ║                   DDoS BOTNET CONTROLLER v3.0                ║
    ║                 ПРОФЕССИОНАЛЬНЫЙ ИНСТРУМЕНТ                 ║
    ║                     Сессия: {self.session_id}                    ║
    ╚═══════════════════════════════════════════════════════════════╝
\033[0m
"""
        print(banner)

    def show_botnet_art(self):
        botnet_art = """
\033[93m
                    ╔══════════════════════════════╗
                    ║       БОТНЕТ АКТИВИРОВАН     ║
                    ║    🖥️ 🖥️ 🖥️ 🖥️ 🖥️ 🖥️ 🖥️    ║
                    ║    🖥️ 🖥️ 🖥️ 🖥️ 🖥️ 🖥️ 🖥️    ║
                    ╚══════════════════════════════╝
                
                ╭──────────────────────────────────────╮
                │        АТАКА ЗАПУЩЕНА!              │
                │    Нагрузка нарастает... 🚀         │
                ╰──────────────────────────────────────╯
\033[0m
"""
        print(botnet_art)

    def show_menu(self):
        menu = """
\033[92m
    ┌────────────────── ПАНЕЛЬ УПРАВЛЕНИЯ ──────────────────┐
    │                                                       │
    │  [1] Запуск DDoS атаки                               │
    │  [2] Мониторинг атаки                                │
    │  [3] Экстренная остановка                            │
    │  [4] Системная информация                            │
    │  [5] Выход из системы                                │
    │                                                       │
    └───────────────────────────────────────────────────────┘
\033[0m
"""
        print(menu)

    def attack_thread(self, thread_id):
        """Поток атаки"""
        while self.attack_active:
            # Отправка пакетов
            time.sleep(random.uniform(0.01, 0.1))
            self.packets_sent += random.randint(1, 10)
            
            # Логирование действий
            if random.random() < 0.01:
                messages = [
                    f"Бот #{thread_id}: SYN флуд активирован",
                    f"Бот #{thread_id}: UDP пакеты отправлены",
                    f"Бот #{thread_id}: HTTP запросы выполнены",
                    f"Бот #{thread_id}: Увеличение интенсивности",
                    f"Бот #{thread_id}: Обход систем защиты",
                    f"Бот #{thread_id}: Эскалация атаки"
                ]
                print(f"\033[90m{random.choice(messages)}\033[0m")

    def start_attack(self):
        self.clear_screen()
        self.show_banner()
        
        print("\n\033[93m[КОНФИГУРАЦИЯ АТАКИ]\033[0m")
        
        # Ввод цели
        self.target_ip = input("Введите IP цель: ").strip()
        if not self.target_ip:
            self.target_ip = "192.168.1.1"
            
        try:
            port = input("Введите порт (по умолчанию 80): ").strip()
            self.target_port = int(port) if port else 80
        except:
            self.target_port = 80
            
        try:
            bots = input("Количество ботов (по умолчанию 1000): ").strip()
            self.bot_count = int(bots) if bots else 1000
        except:
            self.bot_count = 1000

        print(f"\n\033[91mЦелевой сервер: {self.target_ip}:{self.target_port}")
        print(f"Ботнет: {self.bot_count:,} узлов\033[0m")
        
        confirm = input("\nПодтвердить запуск атаки? (y/N): ").lower()
        if confirm != 'y':
            return

        self.attack_active = True
        self.packets_sent = 0
        self.attack_start_time = datetime.now()
        self.threads = []

        # Запуск атаки
        self.clear_screen()
        self.show_banner()
        self.show_botnet_art()
        
        self.typewriter_effect("\n[ИНИЦИАЛИЗАЦИЯ DDoS АТАКИ...]", 0.02)
        
        # Активация ботнета
        print(f"\n\033[96mАктивация {self.bot_count:,} ботов...\033[0m")
        for i in range(min(50, self.bot_count // 20)):
            time.sleep(0.1)
            bots_connected = (i + 1) * (self.bot_count // 50)
            print(f"\r\033[92mАктивировано ботов: {bots_connected:,}/{self.bot_count:,}\033[0m", end="")
        print()

        # Запуск потоков атаки
        for i in range(10):
            thread = threading.Thread(target=self.attack_thread, args=(i+1,))
            thread.daemon = True
            thread.start()
            self.threads.append(thread)

        self.loading_animation("Применение векторов атаки", 3)
        
        print("\n\033[92m[АТАКА УСПЕШНО ЗАПУЩЕНА!]\033[0m")
        print("Система работает в автоматическом режиме")
        
        # Мониторинг атаки
        try:
            while self.attack_active:
                time.sleep(1)
                if int(time.time()) % 5 == 0:
                    duration = datetime.now() - self.attack_start_time
                    print(f"\r\033[93mСтатус: {self.packets_sent:,} пакетов | "
                          f"Время: {duration.seconds} сек | Боты: {self.bot_count:,}\033[0m", end="")
        except KeyboardInterrupt:
            self.stop_attack()

    def stop_attack(self):
        if self.attack_active:
            self.attack_active = False
            print("\n\n\033[91m[ЭКСТРЕННАЯ ОСТАНОВКА АТАКИ]")
            self.loading_animation("Деактивация ботнета", 2)
            
            duration = datetime.now() - self.attack_start_time
            print(f"\n\033[92m[ОПЕРАЦИЯ ЗАВЕРШЕНА]")
            print(f"Финальный отчет:")
            print(f"  ▸ Всего пакетов: {self.packets_sent:,}")
            print(f"  ▸ Время работы: {duration.seconds} секунд")
            print(f"  ▸ Задействовано узлов: {self.bot_count:,}")
            print(f"  ▸ Цель: {self.target_ip}:{self.target_port}")
            print(f"  ▸ Результат: Сервер перегружен ✅\033[0m")
            
            input("\nНажмите Enter для продолжения...")

    def show_status(self):
        self.clear_screen()
        self.show_banner()
        
        if not self.attack_active:
            print("\n\033[93m[СИСТЕМА В РЕЖИМЕ ОЖИДАНИЯ]")
            print("Запустите атаку для активации мониторинга\033[0m")
        else:
            duration = datetime.now() - self.attack_start_time
            print("\n\033[96m[МОНИТОРИНГ АТАКИ В РЕАЛЬНОМ ВРЕМЕНИ]\033[0m")
            print(f"  ▸ Целевой хост: {self.target_ip}:{self.target_port}")
            print(f"  ▸ Активных ботов: {self.bot_count:,}")
            print(f"  ▸ Отправлено пакетов: {self.packets_sent:,}")
            print(f"  ▸ Длительность: {duration.seconds} секунд")
            print(f"  ▸ Интенсивность: {self.packets_sent // max(1, duration.seconds):,} пак/сек")
            
            # Индикатор прогресса
            print(f"\n\033[92mПрогресс операции:\033[0m")
            progress = min(100, (duration.seconds * 2))
            bar = "█" * (progress // 2) + "░" * (50 - progress // 2)
            print(f"[{bar}] {progress}%")
            
            print(f"\n\033[93mСтатус цели: 🔥 ВЫСОКАЯ НАГРУЗКА\033[0m")
        
        input("\nНажмите Enter для продолжения...")

    def show_info(self):
        self.clear_screen()
        self.show_banner()
        
        info = """
\033[96m
    ╔══════════════════════════════════════════════╗
    ║           СИСТЕМНАЯ ИНФОРМАЦИЯ              ║
    ║                                              ║
    ║  DDoS Botnet Controller v3.0                ║
    ║                                              ║
    ║  Возможности:                               ║
    ║  • Масштабируемые атаки                     ║
    ║  • Распределенная сеть ботов                ║
    ║  • Множественные векторы атаки              ║
    ║  • Автоматический обход защиты              ║
    ║  • Реальный мониторинг                      ║
    ║                                              ║
    ║  Технические характеристики:                ║
    ║  • Поддержка тысяч одновременных узлов      ║
    ║  • Минимальное обнаружение                  ║
    ║  • Высокая пропускная способность           ║
    ║  • Стабильное соединение                    ║
    ║                                              ║
    ║  Разработчик: Профессиональная команда      ║
    ║  Версия: v3.0.0                             ║
    ╚══════════════════════════════════════════════╝
\033[0m
"""
        print(info)
        input("\nНажмите Enter для продолжения...")

    def run(self):
        while True:
            self.clear_screen()
            self.show_banner()
            self.show_menu()
            
            try:
                choice = input("\n\033[96mddos@control~# \033[0m").strip()
                
                if choice == '1':
                    self.start_attack()
                elif choice == '2':
                    self.show_status()
                elif choice == '3':
                    self.stop_attack()
                elif choice == '4':
                    self.show_info()
                elif choice == '5':
                    self.typewriter_effect("\n\033[91m[ЗАВЕРШЕНИЕ СЕССИИ...]")
                    if self.attack_active:
                        self.stop_attack()
                    self.loading_animation("Очистка системных логов", 2)
                    self.typewriter_effect("Система отключена. Сессия завершена!")
                    break
                else:
                    self.typewriter_effect("\n\033[91m[НЕВЕРНАЯ КОМАНДА]")
                    time.sleep(1)
                    
            except KeyboardInterrupt:
                print("\n\n\033[91m[ЭКСТРЕННОЕ ОТКЛЮЧЕНИЕ]")
                if self.attack_active:
                    self.stop_attack()
                break

if __name__ == "__main__":
    try:
        tool = DDoSTool()
        tool.run()
    except Exception as e:
        print(f"\n\033[91m[СИСТЕМНАЯ ОШИБКА: {e}]")
        print("Аварийное отключение.\033[0m")
