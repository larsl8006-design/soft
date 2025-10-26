import os
import time
import random
import sys
from datetime import datetime

class CameraHackSystem:
    def __init__(self):
        self.found_cameras = []
        self.current_target = None
        self.session_id = f"SESSION_{random.randint(1000, 9999)}"
        self.desktop_path = self.get_desktop_path()
        
    def get_desktop_path(self):
        """Получаем путь к рабочему столу"""
        if os.name == 'nt':  # Windows
            desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        else:  # Linux/Mac
            desktop = os.path.join(os.path.expanduser("~"), "Desktop")
            if not os.path.exists(desktop):
                desktop = os.path.join(os.path.expanduser("~"), "Рабочий стол")
        return desktop
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_banner(self):
        banner = f"""
================================================================================
|                                                                              |
|   ██████ ███████ ███    ███ ██████  ███████ ██████  ███████ ████████         |
|  ██      ██      ████  ████ ██   ██ ██      ██   ██ ██         ██            |
|  ██      █████   ██ ████ ██ ██████  █████   ██████  ███████    ██            |
|  ██      ██      ██  ██  ██ ██   ██ ██      ██   ██      ██    ██            |
|   ██████ ███████ ██      ██ ██████  ███████ ██   ██ ███████    ██            |
|                                                                              |
|                      СИСТЕМА ВЗЛОМА КАМЕР v2.5.1                            |
|                         РАЗРАБОТЧИК: MRLADER                                |
|                         СЕССИЯ: {self.session_id}                           |
|                    ПУТЬ СОХРАНЕНИЯ: {os.path.basename(self.desktop_path)}    |
|                                                                              |
================================================================================
"""
        print(banner)
    
    def type_effect(self, text, delay=0.03):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def loading_animation(self, text, duration=3):
        print(f"{text} ", end="", flush=True)
        start_time = time.time()
        while time.time() - start_time < duration:
            for char in '|/-\\':
                print(f'\b{char}', end='', flush=True)
                time.sleep(0.1)
        print('\b ', end='', flush=True)
        print()
    
    def generate_ip_range(self):
        base_ips = ["192.168.1", "10.0.0", "172.16.1", "192.168.0"]
        return f"{random.choice(base_ips)}.1-255"
    
    def scan_network(self):
        self.clear_screen()
        print("=" * 80)
        print("МОДУЛЬ СКАНИРОВАНИЯ СЕТИ")
        print("=" * 80)
        print()
        
        ip_range = self.generate_ip_range()
        print(f"[ИНФО] Сканируемый диапазон: {ip_range}")
        print("[ИНФО] Портs: 80,443,554,8000,8080")
        print()
        
        # Симуляция сканирования
        total_hosts = 254
        found_count = 0
        
        for i in range(total_hosts):
            progress = (i / total_hosts) * 100
            sys.stdout.write(f"\r[СКАНИРОВАНИЕ] Прогресс: [{'#' * int(progress/2)}{' ' * (50 - int(progress/2))}] {progress:.1f}%")
            sys.stdout.flush()
            
            # Случайное обнаружение камер
            if random.random() < 0.07:
                found_count += 1
                ip_base = ip_range.split('.')[0:3]
                ip = f"{'.'.join(ip_base)}.{random.randint(1, 254)}"
                port = random.choice([80, 443, 554, 8000, 8080])
                
                camera_brands = [
                    ("HikVision", "DS-2CD2143", "УЛИЧНАЯ"),
                    ("Dahua", "IPC-HDW2230", "ВНУТРЕННЯЯ"),
                    ("Axis", "M3045", "ПАРКОВКА"),
                    ("Sony", "SNC-EM600", "ОФИС"),
                    ("Bosch", "FLEXIDOME", "КОРИДОР")
                ]
                brand, model, location = random.choice(camera_brands)
                
                status = "УЯЗВИМА" if random.random() > 0.5 else "ЗАЩИЩЕНА"
                
                camera_data = {
                    'ip': ip,
                    'port': port,
                    'brand': brand,
                    'model': model,
                    'location': location,
                    'status': status,
                    'credentials': "admin:admin" if status == "УЯЗВИМА" else "ПОЛЬЗОВАТЕЛЬСКИЕ"
                }
                
                self.found_cameras.append(camera_data)
                
                print(f"\n[НАЙДЕНО] {ip}:{port} | {brand} {model} | {location} | {status}")
            
            time.sleep(0.02)
        
        print(f"\n\n[СКАНИРОВАНИЕ] Завершено! Найдено камер: {found_count}")
        
        # Автоматическое сохранение результатов сканирования
        if found_count > 0:
            self.save_scan_results()
        
        return found_count
    
    def save_scan_results(self):
        """Сохраняет результаты сканирования на рабочий стол"""
        if not self.found_cameras:
            return
            
        filename = f"scan_results_{self.session_id}.txt"
        filepath = os.path.join(self.desktop_path, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"РЕЗУЛЬТАТЫ СКАНИРОВАНИЯ СЕТИ\n")
            f.write(f"Сессия: {self.session_id}\n")
            f.write(f"Разработчик: MrLader\n")
            f.write(f"Дата сканирования: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 60 + "\n\n")
            
            for i, camera in enumerate(self.found_cameras, 1):
                f.write(f"КАМЕРА #{i}\n")
                f.write(f"IP-адрес: {camera['ip']}:{camera['port']}\n")
                f.write(f"Производитель: {camera['brand']}\n")
                f.write(f"Модель: {camera['model']}\n")
                f.write(f"Расположение: {camera['location']}\n")
                f.write(f"Статус безопасности: {camera['status']}\n")
                f.write(f"Учетные данные: {camera['credentials']}\n")
                f.write("-" * 40 + "\n\n")
        
        print(f"[СОХРАНЕНИЕ] Результаты сканирования сохранены: {filepath}")
    
    def display_cameras(self):
        if not self.found_cameras:
            print("[ОШИБКА] Камеры не найдены. Сначала выполните сканирование сети.")
            return
        
        print("\n" + "=" * 80)
        print("ОБНАРУЖЕННЫЕ КАМЕРЫ")
        print("=" * 80)
        
        for i, camera in enumerate(self.found_cameras, 1):
            status_color = "УЯЗВИМА" if camera['status'] == "УЯЗВИМА" else "ЗАЩИЩЕНА"
            print(f"{i}. {camera['ip']}:{camera['port']}")
            print(f"   Модель: {camera['brand']} {camera['model']}")
            print(f"   Расположение: {camera['location']}")
            print(f"   Статус: {status_color}")
            print(f"   Учетные данные: {camera['credentials']}")
            print()
    
    def connect_to_camera(self):
        if not self.found_cameras:
            print("[ОШИБКА] Нет доступных камер для подключения.")
            return
        
        self.display_cameras()
        
        try:
            choice = int(input("[ВВОД] Выберите камеру для подключения (номер): "))
            if 1 <= choice <= len(self.found_cameras):
                self.current_target = self.found_cameras[choice-1]
                print(f"[ПОДКЛЮЧЕНИЕ] Попытка подключения к {self.current_target['ip']}:{self.current_target['port']}")
                
                # Симуляция подключения
                self.loading_animation("[АУТЕНТИФИКАЦИЯ] Установка соединения", 2)
                
                if self.current_target['status'] == "УЯЗВИМА":
                    print("[УСПЕХ] Соединение установлено с учетными данными по умолчанию")
                    return True
                else:
                    print("[ОШИБКА] Подключение отклонено - требуется аутентификация")
                    return False
            else:
                print("[ОШИБКА] Неверный выбор")
                return False
        except ValueError:
            print("[ОШИБКА] Неверный ввод")
            return False
    
    def brute_force_credentials(self):
        if not self.current_target:
            print("[ОШИБКА] Целевая камера не выбрана")
            return False
        
        print(f"[ПОДБОР] Запуск атаки на подбор учетных данных для {self.current_target['ip']}")
        
        common_credentials = [
            ("admin", "admin"),
            ("admin", "12345"),
            ("admin", "password"),
            ("root", "root"),
            ("admin", ""),
            ("service", "service")
        ]
        
        for username, password in common_credentials:
            print(f"[ПОПЫТКА] {username}:{password}", end="")
            self.loading_animation("", 1)
            
            if random.random() > 0.7:  # 30% шанс успеха
                print(f"[УСПЕХ] Найдены верные учетные данные: {username}:{password}")
                self.current_target['credentials'] = f"{username}:{password}"
                self.current_target['status'] = "УЯЗВИМА"
                
                # Сохраняем успешный подбор
                self.save_bruteforce_result(username, password)
                return True
        
        print("[ОШИБКА] Подбор учетных данных не удался")
        return False
    
    def save_bruteforce_result(self, username, password):
        """Сохраняет результат успешного подбора на рабочий стол"""
        filename = f"bruteforce_success_{self.session_id}.txt"
        filepath = os.path.join(self.desktop_path, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"УСПЕШНЫЙ ПОДБОР УЧЕТНЫХ ДАННЫХ\n")
            f.write(f"Сессия: {self.session_id}\n")
            f.write(f"Разработчик: MrLader\n")
            f.write(f"Время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 50 + "\n\n")
            f.write(f"Целевая камера: {self.current_target['ip']}:{self.current_target['port']}\n")
            f.write(f"Производитель: {self.current_target['brand']} {self.current_target['model']}\n")
            f.write(f"Найденные учетные данные:\n")
            f.write(f"  Логин: {username}\n")
            f.write(f"  Пароль: {password}\n")
            f.write(f"  Полный доступ: ДА\n")
        
        print(f"[СОХРАНЕНИЕ] Учетные данные сохранены: {filepath}")
    
    def stream_camera(self):
        if not self.current_target:
            print("[ОШИБКА] Камера не выбрана")
            return
        
        if self.current_target['status'] != "УЯЗВИМА":
            print("[ОШИБКА] Камера не уязвима. Сначала выполните подбор учетных данных.")
            return
        
        print(f"[ТРАНСЛЯЦИЯ] Запуск видеопотока с {self.current_target['ip']}")
        print("[ИНФО] Протокол трансляции: RTSP/H.264")
        print("[ИНФО] Разрешение: 1920x1080")
        print()
        
        # Симуляция видеопотока
        try:
            frame_count = 0
            while True:
                current_time = datetime.now().strftime("%H:%M:%S")
                
                # Простая ASCII анимация кадра
                frame = f"""
                +----------------------------------------------------+
                |               ПРЯМАЯ ТРАНСЛЯЦИЯ                  |
                |    {self.current_target['brand']} {self.current_target['model']}     |
                |          {self.current_target['ip']}:{self.current_target['port']}          |
                |                                                    |
                |    Время: {current_time}                        |
                |    Кадр: {frame_count:06d}                             |
                |                                                    |
                |    [############## LIVE FEED ##############]       |
                |                                                    |
                |    Статус: ТРАНСЛЯЦИЯ                             |
                |    Протокол: RTSP                                 |
                |    Скорость: 2.5 Мбит/с                           |
                |    Разработчик: MrLader                           |
                +----------------------------------------------------+
                """
                
                print("\033[H\033[J", end="")  # Очистка экрана
                print(frame)
                print("Нажмите Ctrl+C для остановки трансляции")
                
                frame_count += 1
                time.sleep(0.5)
                
        except KeyboardInterrupt:
            print("\n[ОСТАНОВ] Трансляция прервана")
    
    def exploit_vulnerabilities(self):
        if not self.current_target:
            print("[ОШИБКА] Целевая камера не выбрана")
            return
        
        print(f"[ЭКСПЛУАТАЦИЯ] Сканирование {self.current_target['ip']} на уязвимости")
        
        vulnerabilities = [
            "CVE-2021-36260 - HikVision Инъекция команд",
            "CVE-2018-9995 - Dahua Раскрытие учетных данных", 
            "CVE-2017-7921 - Axis Camera Обход аутентификации",
            "CVE-2022-30563 - CCTV DVR Удаленное выполнение кода",
            "Слабая аутентификация RTSP",
            "Учетные данные по умолчанию включены"
        ]
        
        found_vulns = []
        for vuln in vulnerabilities:
            print(f"[ПРОВЕРКА] Проверка {vuln.split(' - ')[0]}", end="")
            self.loading_animation("", 1)
            
            if random.random() > 0.5:
                found_vulns.append(vuln)
                print(" - УЯЗВИМА")
            else:
                print(" - НЕ УЯЗВИМА")
        
        if found_vulns:
            print("\n[НАЙДЕНЫ УЯЗВИМОСТИ]:")
            for vuln in found_vulns:
                print(f"  - {vuln}")
            
            # Сохраняем найденные уязвимости
            self.save_vulnerabilities(found_vulns)
        else:
            print("\n[ИНФО] Критические уязвимости не найдены")
    
    def save_vulnerabilities(self, vulnerabilities):
        """Сохраняет найденные уязвимости на рабочий стол"""
        filename = f"vulnerabilities_{self.session_id}.txt"
        filepath = os.path.join(self.desktop_path, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"ОТЧЕТ ПО УЯЗВИМОСТЯМ\n")
            f.write(f"Сессия: {self.session_id}\n")
            f.write(f"Разработчик: MrLader\n")
            f.write(f"Время сканирования: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Целевая камера: {self.current_target['ip']}:{self.current_target['port']}\n")
            f.write("=" * 60 + "\n\n")
            
            f.write("НАЙДЕННЫЕ УЯЗВИМОСТИ:\n")
            for i, vuln in enumerate(vulnerabilities, 1):
                f.write(f"{i}. {vuln}\n")
        
        print(f"[СОХРАНЕНИЕ] Отчет по уязвимостям сохранен: {filepath}")
    
    def save_session(self):
        if not self.found_cameras:
            print("[ОШИБКА] Нет данных для сохранения")
            return
        
        filename = f"full_session_{self.session_id}.txt"
        filepath = os.path.join(self.desktop_path, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"ПОЛНЫЙ ОТЧЕТ СЕССИИ ВЗЛОМА КАМЕР\n")
            f.write(f"Сессия: {self.session_id}\n")
            f.write(f"Разработчик: MrLader\n")
            f.write(f"Дата начала: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Путь сохранения: {self.desktop_path}\n")
            f.write("=" * 70 + "\n\n")
            
            f.write("ОБНАРУЖЕННЫЕ КАМЕРЫ:\n")
            f.write("=" * 50 + "\n")
            for i, camera in enumerate(self.found_cameras, 1):
                f.write(f"\nКАМЕРА #{i}\n")
                f.write(f"IP-адрес: {camera['ip']}:{camera['port']}\n")
                f.write(f"Производитель: {camera['brand']}\n")
                f.write(f"Модель: {camera['model']}\n")
                f.write(f"Расположение: {camera['location']}\n")
                f.write(f"Статус безопасности: {camera['status']}\n")
                f.write(f"Учетные данные: {camera['credentials']}\n")
                f.write("-" * 40 + "\n")
            
            if self.current_target:
                f.write(f"\nТЕКУЩАЯ ЦЕЛЕВАЯ КАМЕРА:\n")
                f.write(f"IP: {self.current_target['ip']}:{self.current_target['port']}\n")
                f.write(f"Модель: {self.current_target['brand']} {self.current_target['model']}\n")
                f.write(f"Статус: {self.current_target['status']}\n")
        
        print(f"[СОХРАНЕНИЕ] Полный отчет сессии сохранен: {filepath}")
        print(f"[ИНФО] Все файлы сохраняются на рабочий стол: {self.desktop_path}")
    
    def print_menu(self):
        menu = """
================================================================================
|                                ГЛАВНОЕ МЕНЮ                                 |
================================================================================
| 1. Сканировать сеть на наличие камер                                        |
| 2. Показать обнаруженные камеры                                             |
| 3. Подключиться к камере                                                    |
| 4. Подобрать учетные данные                                                 |
| 5. Запустить видеопоток                                                     |
| 6. Найти уязвимости                                                         |
| 7. Сохранить полный отчет сессии                                            |
| 8. Выход                                                                    |
================================================================================
"""
        print(menu)
    
    def run(self):
        while True:
            self.clear_screen()
            self.print_banner()
            self.print_menu()
            
            try:
                choice = input("[ВЫБОР] Выберите опцию (1-8): ")
                
                if choice == '1':
                    self.scan_network()
                elif choice == '2':
                    self.display_cameras()
                elif choice == '3':
                    self.connect_to_camera()
                elif choice == '4':
                    self.brute_force_credentials()
                elif choice == '5':
                    self.stream_camera()
                elif choice == '6':
                    self.exploit_vulnerabilities()
                elif choice == '7':
                    self.save_session()
                elif choice == '8':
                    print("[ВЫХОД] Завершение сессии...")
                    print(f"[ИНФО] Файлы сессии сохранены на рабочем столе")
                    print("[ИНФО] Разработано MrLader - Только для образовательных целей")
                    break
                else:
                    print("[ОШИБКА] Выбрана неверная опция")
                
                if choice != '8':
                    input("\n[ВВОД] Нажмите Enter для продолжения...")
                    
            except KeyboardInterrupt:
                print("\n\n[ВЫХОД] Сессия прервана пользователем")
                break

if __name__ == "__main__":
    try:
        hacker = CameraHackSystem()
        hacker.run()
    except Exception as e:
        print(f"[ОШИБКА] Сбой системы: {e}")
