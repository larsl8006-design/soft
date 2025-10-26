import os
import sys
import time
import random
import threading
from datetime import datetime

class HackerTerminal:
    def __init__(self):
        self.session_id = self.generate_session_id()
        self.tor_connected = False
        self.vpn_active = False
        self.anonymity_level = 0
        
    def generate_session_id(self):
        return f"ANON{random.randint(1000,9999)}-{int(time.time())}"
    
    def type_effect(self, text, delay=0.03):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def loading_animation(self, text, duration=2):
        symbols = ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷']
        end_time = time.time() + duration
        i = 0
        
        while time.time() < end_time:
            print(f"\r\033[96m{symbols[i % len(symbols)]} {text}\033[0m", end="")
            time.sleep(0.1)
            i += 1
        print("\r\033[92m✓ {}\033[0m".format(text))
    
    def show_banner(self):
        banner = f"""
\033[91m
    ████████╗ ██████╗ ██████╗ 
    ╚══██╔══╝██╔═══██╗██╔══██╗
       ██║   ██║   ██║██████╔╝
       ██║   ██║   ██║██╔══██╗
       ██║   ╚██████╔╝██║  ██║
       ╚═╝    ╚═════╝ ╚═╝  ╚═╝
    
    DARKNET TERMINAL v3.1.4
    Session: {self.session_id}
    Status: {'CONNECTED' if self.tor_connected else 'OFFLINE'}
\033[0m
"""
        print(banner)
    
    def show_menu(self):
        menu = """
\033[92m
    ┌───────────────── DARKNET MENU ─────────────────┐
    │                                                │
    │  [1] Подключиться к TOR сети                   │
    │  [2] Проверить анонимность                    │
    │  [3] Сканирование сети                        │
    │  [4] Поиск уязвимостей                        │
    │  [5] Анонимный браузер                        │
    │  [6] Взлом Wi-Fi сетей                        │
    │  [7] DDoS атака                               │
    │  [8] Шифрование трафика                       │
    │  [9] Очистка логов                            │
    │  [10] Выход                                   │
    │                                                │
    └────────────────────────────────────────────────┘
\033[0m
"""
        print(menu)
    
    def connect_to_tor(self):
        self.type_effect("\n[INITIATING TOR CONNECTION...]", 0.01)
        self.loading_animation("Установка соединения с TOR сетью", 3)
        
        # Имитация подключения к TOR
        steps = [
            "Поиск TOR нод...",
            "Установка цепочки соединений...",
            "Рукопожатие с узлом A...",
            "Подключение к узлу B...",
            "Соединение с узлом C...",
            "Шифрование трафика...",
            "Проверка анонимности..."
        ]
        
        for step in steps:
            print(f"\033[96m⏳ {step}\033[0m")
            time.sleep(random.uniform(0.5, 1.5))
            
            # Случайные успешные/неуспешные попытки
            if random.random() > 0.2:
                print("\033[92m✓ Успешно\033[0m")
            else:
                print("\033[93m⚠ Повторная попытка...\033[0m")
                time.sleep(1)
        
        self.tor_connected = True
        self.anonymity_level = random.randint(85, 99)
        
        self.type_effect(f"\n\033[92m[TOR CONNECTION ESTABLISHED!]", 0.02)
        print(f"\033[96mУровень анонимности: {self.anonymity_level}%")
        print("IP адрес: 192.168." + ".".join(str(random.randint(1, 255)) for _ in range(2)))
        print("Локация: [СКРЫТО]")
        print("Трафик: ЗАШИФРОВАН\033[0m")
        
        input("\nНажмите Enter для продолжения...")
    
    def check_anonymity(self):
        if not self.tor_connected:
            self.type_effect("\n\033[91m[ERROR: TOR NOT CONNECTED!]", 0.01)
            return
        
        self.type_effect("\n[SCANNING ANONYMITY...]", 0.01)
        self.loading_animation("Проверка цифрового следа", 2)
        
        tests = [
            ("DNS утечки", random.randint(90, 100)),
            ("WebRTC утечки", random.randint(85, 100)),
            ("IP адрес", random.randint(88, 100)),
            ("Геолокация", random.randint(92, 100)),
            ("Браузерные отпечатки", random.randint(80, 95)),
            ("Тайминг атаки", random.randint(75, 90))
        ]
        
        print("\n\033[96mРЕЗУЛЬТАТЫ ПРОВЕРКИ:\033[0m")
        print("┌───────────────────┬───────────┐")
        print("│      ТЕСТ         │  РЕЗУЛЬТАТ │")
        print("├───────────────────┼───────────┤")
        
        for test, score in tests:
            status = "🟢 ЗАЩИЩЕНО" if score > 85 else "🟡 ЧАСТИЧНО" if score > 70 else "🔴 ОПАСНО"
            print(f"│ {test:<17} │ {score:>2}% {status} │")
            time.sleep(0.3)
        
        print("└───────────────────┴───────────┘")
        
        overall = sum(score for _, score in tests) // len(tests)
        print(f"\n\033[92mОбщий уровень анонимности: {overall}%\033[0m")
        
        input("\nНажмите Enter для продолжения...")
    
    def network_scan(self):
        self.type_effect("\n[NETWORK SCANNER ACTIVATED...]", 0.01)
        self.loading_animation("Сканирование локальной сети", 2)
        
        # Имитация сканирования сети
        devices = []
        for i in range(random.randint(5, 15)):
            device_types = ["Router", "PC", "Phone", "Tablet", "IoT", "Server"]
            os_types = ["Windows", "Linux", "Android", "iOS", "macOS", "Unknown"]
            
            devices.append({
                'ip': f"192.168.1.{random.randint(2, 254)}",
                'mac': ":".join([f"{random.randint(0,255):02x}" for _ in range(6)]),
                'type': random.choice(device_types),
                'os': random.choice(os_types),
                'ports': random.sample([21, 22, 23, 80, 443, 8080, 3389], random.randint(1, 4))
            })
        
        print("\n\033[96mОБНАРУЖЕННЫЕ УСТРОЙСТВА:\033[0m")
        print("┌─────────────────┬──────────────────┬────────────┬────────────┐")
        print("│       IP        │       MAC        │    ТИП     │    ПОРТЫ   │")
        print("├─────────────────┼──────────────────┼────────────┼────────────┤")
        
        for device in devices:
            ports = ", ".join(map(str, device['ports']))
            print(f"│ {device['ip']:<15} │ {device['mac']:<16} │ {device['type']:<10} │ {ports:<10} │")
            time.sleep(0.2)
        
        print("└─────────────────┴──────────────────┴────────────┴────────────┘")
        
        input("\nНажмите Enter для продолжения...")
    
    def vulnerability_scan(self):
        self.type_effect("\n[VULNERABILITY SCANNER...]", 0.01)
        self.loading_animation("Поиск уязвимостей в системе", 3)
        
        vulnerabilities = [
            ("CVE-2023-12345", "Критическая", "Удаленное выполнение кода", "Windows SMB"),
            ("CVE-2023-67890", "Высокая", "SQL инъекция", "Web Application"),
            ("CVE-2023-54321", "Средняя", "XSS уязвимость", "WordPress Plugin"),
            ("CVE-2023-98765", "Низкая", "Обход аутентификации", "FTP Server"),
            ("CVE-2023-11223", "Критическая", "Переполнение буфера", "Linux Kernel")
        ]
        
        print("\n\033[96mОБНАРУЖЕННЫЕ УЯЗВИМОСТИ:\033[0m")
        print("┌────────────────┬──────────┬──────────────────────┬─────────────────┐")
        print("│      CVE       │  УРОВЕНЬ │       ОПИСАНИЕ       │     СЕРВИС      │")
        print("├────────────────┼──────────┼──────────────────────┼─────────────────┤")
        
        for cve, level, desc, service in vulnerabilities:
            color = "\033[91m" if level == "Критическая" else "\033[93m" if level == "Высокая" else "\033[96m"
            print(f"│ {cve:<14} │ {color}{level:<8}\033[0m │ {desc:<20} │ {service:<15} │")
            time.sleep(0.4)
        
        print("└────────────────┴──────────┴──────────────────────┴─────────────────┘")
        
        input("\nНажмите Enter для продолжения...")
    
    def anonymous_browser(self):
        self.type_effect("\n[LAUNCHING ANONYMOUS BROWSER...]", 0.01)
        self.loading_animation("Запуск TOR браузера", 2)
        
        print("""
\033[94m
    🌐 АНОНИМНЫЙ БРАУЗЕР АКТИВИРОВАН
    
    Доступные onion сайты:
    • dreadytofatroptsdj6io7l3xptbet6onoyno2yv7jicoxknyazubrad.onion
    • facebookcorewwwi.onion
    • duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion
    • protonmailrmez3lotccipshtkleegetolb73uirgj7r4o4vfu7ozyd.onion
    
    Особенности:
    ✓ JavaScript отключен
    ✓ Cookies автоматически очищаются
    ✓ Trackers блокируются
    ✓ Геолокация скрыта
\033[0m
        """)
        
        input("Нажмите Enter для возврата...")
    
    def wifi_hack(self):
        self.type_effect("\n[WIFI PENETRATION TOOL...]", 0.01)
        self.loading_animation("Сканирование Wi-Fi сетей", 2)
        
        networks = [
            {"SSID": "Home_Network", "BSSID": "AA:BB:CC:DD:EE:FF", "Signal": "▇▇▇▇▇", "Security": "WPA2", "Channel": 6},
            {"SSID": "TP-Link_Office", "BSSID": "11:22:33:44:55:66", "Signal": "▇▇▇▇", "Security": "WPA2", "Channel": 11},
            {"SSID": "Free_WiFi", "BSSID": "99:88:77:66:55:44", "Signal": "▇▇", "Security": "WEP", "Channel": 1},
            {"SSID": "Neighbor_5G", "BSSID": "AB:CD:EF:12:34:56", "Signal": "▇▇▇", "Security": "WPA3", "Channel": 36},
            {"SSID": "AndroidAP", "BSSID": "78:9A:BC:DE:F0:12", "Signal": "▇▇▇▇", "Security": "WPA2", "Channel": 6}
        ]
        
        print("\n\033[96mОБНАРУЖЕННЫЕ СЕТИ WI-FI:\033[0m")
        print("┌──────────────────┬──────────────────┬─────────┬──────────┬─────────┐")
        print("│       SSID       │      BSSID       │ СИГНАЛ  │ ЗАЩИТА   │ КАНАЛ   │")
        print("├──────────────────┼──────────────────┼─────────┼──────────┼─────────┤")
        
        for network in networks:
            print(f"│ {network['SSID']:<16} │ {network['BSSID']:<16} │ {network['Signal']:<7} │ {network['Security']:<8} │ {network['Channel']:<7} │")
            time.sleep(0.3)
        
        print("└──────────────────┴──────────────────┴─────────┴──────────┴─────────┘")
        
        self.type_effect("\n[STARTING WPA2 HANDCAPTURE...]", 0.02)
        self.loading_animation("Перехват handshake", 3)
        
        print("\033[92m✓ Handshake перехвачен успешно!")
        print("✓ Запуск bruteforce атаки...\033[0m")
        
        input("\nНажмите Enter для продолжения...")
    
    def ddos_attack(self):
        self.type_effect("\n[DDoS BOTNET ACTIVATED...]", 0.01)
        
        target = input("Введите цель атаки: ").strip()
        if not target:
            target = "example.com"
        
        self.loading_animation(f"Координация атаки на {target}", 3)
        
        print(f"\n\033[91m🚀 ЗАПУСК DDoS АТАКИ НА: {target}\033[0m")
        
        bots = random.randint(500, 5000)
        print(f"🤖 Ботов в сети: {bots}")
        print("📊 Тип атаки: HTTP Flood + SYN Flood")
        print("⏱️ Длительность: 60 секунд")
        
        for i in range(10):
            packets = random.randint(1000, 10000)
            print(f"\r\033[93m📨 Отправлено пакетов: {packets * (i+1)}\033[0m", end="")
            time.sleep(0.5)
        
        print(f"\n\033[92m✓ Атака завершена! Цель {target} временно недоступна.\033[0m")
        
        input("\nНажмите Enter для продолжения...")
    
    def traffic_encryption(self):
        self.type_effect("\n[TRAFFIC ENCRYPTION MODULE...]", 0.01)
        self.loading_animation("Инициализация протоколов шифрования", 2)
        
        protocols = [
            ("AES-256", "Активен", "▇▇▇▇▇▇▇▇"),
            ("RSA-4096", "Активен", "▇▇▇▇▇▇▇"),
            ("ChaCha20", "Активен", "▇▇▇▇▇▇"),
            ("ECC", "Активен", "▇▇▇▇▇"),
            ("OTP", "Неактивен", "▇▇")
        ]
        
        print("\n\033[96mПРОТОКОЛЫ ШИФРОВАНИЯ:\033[0m")
        print("┌──────────────────┬──────────┬────────────┐")
        print("│    ПРОТОКОЛ      │  СТАТУС  │  МОЩНОСТЬ  │")
        print("├──────────────────┼──────────┼────────────┤")
        
        for protocol, status, strength in protocols:
            color = "\033[92m" if status == "Активен" else "\033[91m"
            print(f"│ {protocol:<16} │ {color}{status:<8}\033[0m │ {strength:<10} │")
            time.sleep(0.3)
        
        print("└──────────────────┴──────────┴────────────┘")
        
        self.type_effect("\n[ENCRYPTING ALL TRAFFIC...]", 0.02)
        print("\033[92m✓ Весь исходящий трафик зашифрован")
        print("✓ Ключи обновлены")
        print("✓ Steganography активирована\033[0m")
        
        input("\nНажмите Enter для продолжения...")
    
    def clear_logs(self):
        self.type_effect("\n[SYSTEM LOGS CLEANER...]", 0.01)
        self.loading_animation("Очистка системных логов", 2)
        
        logs_to_clear = [
            "Браузерная история",
            "DNS кэш",
            "Системные логи",
            "Журналы событий",
            "Временные файлы",
            "Кэш приложений"
        ]
        
        for log in logs_to_clear:
            print(f"\033[93m🗑️ Очистка: {log}...\033[0m", end="")
            time.sleep(0.5)
            print("\r\033[92m✓ Очищено: {}\033[0m".format(log))
        
        self.type_effect("\n[ALL LOGS SUCCESSFULLY CLEARED!]", 0.02)
        print("\033[92m✓ Цифровой след удален")
        print("✓ Восстановление невозможно")
        print("✓ Анонимность восстановлена\033[0m")
        
        input("\nНажмите Enter для продолжения...")
    
    def run(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.show_banner()
            self.show_menu()
            
            choice = input("\n\033[96mhacker@darknet~# \033[0m").strip()
            
            if choice == '1':
                self.connect_to_tor()
            elif choice == '2':
                self.check_anonymity()
            elif choice == '3':
                self.network_scan()
            elif choice == '4':
                self.vulnerability_scan()
            elif choice == '5':
                self.anonymous_browser()
            elif choice == '6':
                self.wifi_hack()
            elif choice == '7':
                self.ddos_attack()
            elif choice == '8':
                self.traffic_encryption()
            elif choice == '9':
                self.clear_logs()
            elif choice == '10':
                self.type_effect("\n\033[91m[SHUTTING DOWN...]", 0.01)
                self.loading_animation("Стирание следов", 2)
                self.type_effect("Система очищена. До свидания.", 0.03)
                break
            else:
                self.type_effect("\n\033[91m[INVALID COMMAND!]", 0.01)
                time.sleep(1)

if __name__ == "__main__":
    try:
        terminal = HackerTerminal()
        terminal.run()
    except KeyboardInterrupt:
        print("\n\n\033[91m[EMERGENCY SHUTDOWN!]")
        print("Все соединения разорваны...\033[0m")
