import tkinter as tk
from tkinter import ttk, messagebox
import random
import threading
import time
from datetime import datetime

class CameraHacker:
    def __init__(self, root):
        self.root = root
        self.root.title("🔴 CameraHack Pro v3.0 - BY MrLader")
        self.root.geometry("850x650")
        self.root.configure(bg='#0a0a0a')
        self.root.resizable(False, False)
        
        self.scanning = False
        self.cameras_found = []
        self.current_camera = None
        
        self.create_interface()
        
    def create_interface(self):
        # Header
        header_frame = tk.Frame(self.root, bg='#0a0a0a')
        header_frame.pack(fill='x', padx=10, pady=5)
        
        title_label = tk.Label(header_frame,
                             text="🔴 CAMERA HACK PRO v3.0",
                             font=("Courier", 18, "bold"),
                             fg="#ff0000",
                             bg="#0a0a0a")
        title_label.pack()
        
        dev_label = tk.Label(header_frame,
                           text="👨‍💻 Разработано MrLader",
                           font=("Arial", 10, "italic"),
                           fg="#00ff00",
                           bg="#0a0a0a")
        dev_label.pack()
        
        # Control Panel
        control_frame = tk.LabelFrame(self.root,
                                    text="ПАНЕЛЬ УПРАВЛЕНИЯ",
                                    font=("Arial", 10, "bold"),
                                    fg="#00ffff",
                                    bg="#0a0a0a",
                                    bd=2)
        control_frame.pack(fill='x', padx=10, pady=5)
        
        # IP Configuration
        ip_frame = tk.Frame(control_frame, bg="#0a0a0a")
        ip_frame.pack(fill='x', padx=5, pady=5)
        
        tk.Label(ip_frame, text="Диапазон IP:", fg="white", bg="#0a0a0a").pack(side='left')
        self.ip_combo = ttk.Combobox(ip_frame,
                                   values=[
                                       "192.168.1.1-255",
                                       "192.168.0.1-255", 
                                       "10.0.0.1-255",
                                       "172.16.1.1-255"
                                   ],
                                   width=20)
        self.ip_combo.set("192.168.1.1-255")
        self.ip_combo.pack(side='left', padx=5)
        
        tk.Label(ip_frame, text="Порты:", fg="white", bg="#0a0a0a").pack(side='left', padx=(20,0))
        self.port_combo = ttk.Combobox(ip_frame,
                                     values=[
                                         "80,443,554",
                                         "8000,8080,34567",
                                         "21,22,23,25,53,80,443,554,993,995,1433,1723,3389,8080"
                                     ],
                                     width=25)
        self.port_combo.set("80,443,554")
        self.port_combo.pack(side='left', padx=5)
        
        # Buttons
        btn_frame = tk.Frame(control_frame, bg="#0a0a0a")
        btn_frame.pack(fill='x', padx=5, pady=5)
        
        self.scan_btn = tk.Button(btn_frame,
                                text="🚀 НАЧАТЬ СКАНИРОВАНИЕ",
                                command=self.start_scan,
                                bg="#ff0000",
                                fg="white",
                                font=("Arial", 10, "bold"),
                                width=20)
        self.scan_btn.pack(side='left', padx=5)
        
        self.stop_btn = tk.Button(btn_frame,
                                text="⏹️ ОСТАНОВИТЬ",
                                command=self.stop_scan,
                                bg="#555555",
                                fg="white",
                                state="disabled")
        self.stop_btn.pack(side='left', padx=5)
        
        self.view_btn = tk.Button(btn_frame,
                                text="👁️ ПРОСМОТР",
                                command=self.view_camera,
                                bg="#0055ff",
                                fg="white")
        self.view_btn.pack(side='left', padx=5)
        
        # Progress
        progress_frame = tk.Frame(self.root, bg="#0a0a0a")
        progress_frame.pack(fill='x', padx=10, pady=5)
        
        self.progress = ttk.Progressbar(progress_frame,
                                      orient="horizontal",
                                      length=800,
                                      mode="determinate")
        self.progress.pack(pady=5)
        
        self.status_label = tk.Label(progress_frame,
                                   text="🔴 Готов к сканированию...",
                                   fg="#ffff00",
                                   bg="#0a0a0a",
                                   font=("Arial", 9))
        self.status_label.pack()
        
        # Results
        results_frame = tk.LabelFrame(self.root,
                                    text="📹 ОБНАРУЖЕННЫЕ КАМЕРЫ",
                                    font=("Arial", 10, "bold"),
                                    fg="#00ff00",
                                    bg="#0a0a0a")
        results_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Treeview for cameras
        columns = ("IP", "Порт", "Производитель", "Модель", "Расположение", "Статус")
        self.tree = ttk.Treeview(results_frame, columns=columns, show="headings", height=8)
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        
        self.tree.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Camera View
        view_frame = tk.LabelFrame(self.root,
                                 text="ПРЯМАЯ ТРАНСЛЯЦИЯ",
                                 font=("Arial", 10, "bold"),
                                 fg="#ff00ff",
                                 bg="#0a0a0a")
        view_frame.pack(fill='x', padx=10, pady=5)
        
        self.camera_display = tk.Label(view_frame,
                                     text="Выберите камеру для просмотра\n\n"
                                          "🔴 КАМЕРА НЕ ВЫБРАНА\n\n"
                                          "Разработано MrLader - в образовательных целях",
                                     bg="black",
                                     fg="white",
                                     font=("Courier", 10),
                                     width=80,
                                     height=8,
                                     relief="sunken")
        self.camera_display.pack(padx=5, pady=5)
        
        # Footer
        footer = tk.Label(self.root,
                        text="⚠️ Инструмент создан в образовательных целях. Разработчик: MrLader",
                        fg="#888888",
                        bg="#0a0a0a",
                        font=("Arial", 8))
        footer.pack(pady=5)
    
    def generate_camera_info(self):
        brands = {
            "HikVision": ["DS-2CD2143", "DS-2DE3220", "DS-2CD2085"],
            "Dahua": ["IPC-HFW1230", "IPC-HDW2230", "SD22204T"],
            "Axis": ["M3045", "P3225", "Q1615"],
            "Bosch": ["MIC-710", "FLEXIDOME", "AUTODOME"],
            "Sony": ["SNC-VB770", "SNC-EM600"]
        }
        
        locations = ["Гостиная", "Улица", "Офис", "Парковка", "Вход", "Задний двор"]
        statuses = ["🔴 Уязвима", "🟡 Защищена", "🔴 Стандартные учетные данные"]
        
        brand = random.choice(list(brands.keys()))
        model = random.choice(brands[brand])
        location = random.choice(locations)
        status = random.choice(statuses)
        
        return brand, model, location, status
    
    def scan_network(self):
        self.status_label.config(text="🟡 Сканирование сети...")
        self.progress['value'] = 0
        
        total_ips = 254
        found = 0
        
        for i in range(total_ips):
            if not self.scanning:
                break
                
            time.sleep(0.03)
            self.progress['value'] = (i / total_ips) * 100
            self.root.update()
            
            # Случайное обнаружение камер
            if random.random() < 0.08:
                found += 1
                ip = f"192.168.1.{random.randint(1, 254)}"
                port = random.choice([80, 443, 554, 8000, 8080])
                brand, model, location, status = self.generate_camera_info()
                
                camera_data = (ip, str(port), brand, model, location, status)
                self.cameras_found.append(camera_data)
                self.tree.insert("", "end", values=camera_data)
                
                self.status_label.config(text=f"🟢 Найдено камер: {found}")
        
        self.status_label.config(text=f"✅ Сканирование завершено! Найдено: {found} камер")
        self.scanning = False
        self.scan_btn.config(state="normal", bg="#ff0000")
        self.stop_btn.config(state="disabled", bg="#555555")
        self.progress['value'] = 100
    
    def start_scan(self):
        self.scanning = True
        self.scan_btn.config(state="disabled", bg="#555555")
        self.stop_btn.config(state="normal", bg="#ff0000")
        self.cameras_found = []
        self.tree.delete(*self.tree.get_children())
        
        scan_thread = threading.Thread(target=self.scan_network)
        scan_thread.daemon = True
        scan_thread.start()
    
    def stop_scan(self):
        self.scanning = False
        self.status_label.config(text="🔴 Сканирование остановлено")
        self.scan_btn.config(state="normal", bg="#ff0000")
        self.stop_btn.config(state="disabled", bg="#555555")
    
    def view_camera(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Внимание", "Сначала выберите камеру из списка!")
            return
        
        item = self.tree.item(selected[0])
        camera_data = item['values']
        self.current_camera = camera_data
        
        self.status_label.config(text=f"🟣 Подключение к {camera_data[0]}:{camera_data[1]}...")
        
        # Имитация задержки подключения
        self.root.after(1500, self.show_camera_stream)
    
    def show_camera_stream(self):
        if self.current_camera:
            ip, port, brand, model, location, status = self.current_camera
            
            stream_text = f"""
╔══════════════════════════════════════════════════╗
║               ПРЯМАЯ ТРАНСЛЯЦИЯ                 ║
║         {ip}:{port} - {brand} {model}        ║
║             Расположение: {location}            ║
║             Статус: {status}                    ║
║                                                  ║
║     [СИМУЛИРОВАННЫЙ ПРОСМОТР]                    ║
║                                                  ║
║   📡 Подключение: RTSP поток                    ║
║   🔓 Уровень доступа: Администратор             ║
║   📊 Разрешение: 1920x1080 @ 30fps              ║
║   🕒 Время: {datetime.now().strftime("%H:%M:%S")}              ║
║                                                  ║
║          Разработано MrLader © 2024             ║
╚══════════════════════════════════════════════════╝
"""
            self.camera_display.config(text=stream_text, fg="#00ff00")
            self.status_label.config(text=f"✅ Подключено к {ip} - Трансляция активна")

def main():
    root = tk.Tk()
    app = CameraHacker(root)
    root.mainloop()

if __name__ == "__main__":
    main()