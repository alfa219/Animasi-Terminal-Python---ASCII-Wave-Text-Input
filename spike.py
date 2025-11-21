import time
import sys
import os
from colorama import Fore, Style, init
import pyfiglet

init(autoreset=True)

AVAILABLE_FONTS = {
    '1': ('Standard', 'standard'),
    '2': ('Big', 'big'),
    '3': ('Block', 'block'),
    '4': ('Slant', 'slant'),
    '5': ('Small', 'small'),
}

def clear_screen():
    """Membersihkan layar terminal dan memindahkan kursor ke pojok kiri atas."""
    print('\033c', end='')

def get_terminal_size():
    """Mendapatkan lebar dan tinggi terminal saat ini."""
    try:
        return os.get_terminal_size()
    except OSError:
        return os.terminal_size((80, 24)) # Ukuran standar

def get_user_settings():
    """Fungsi untuk mendapatkan pengaturan dari pengguna dengan antarmuka yang lebih baik."""
    clear_screen()
    print("--- Selamat Datang di Program Animasi Sempurna ---\n")
    
    print("Pilih jenis animasi yang Anda inginkan:")
    print("  1. Animasi Karakter (misal: *, #, @)")
    print("  2. Animasi Teks Sempurna (menggunakan font profesional)")
    
    while True:
        anim_type = input("\nMasukkan pilihan Anda (1 atau 2): ")
        if anim_type in ['1', '2']:
            break
        print("Pilihan tidak valid. Silakan masukkan angka 1 atau 2.")

    settings = {'animation_type': anim_type}

    if anim_type == '1':
        while True:
            char = input("\nMasukkan karakter untuk animasi: ")
            if char:
                settings['char'] = char
                break
            print("Input tidak boleh kosong. Silakan coba lagi.")
    else: 
        while True:
            text = input("\nMasukkan teks untuk animasi: ").upper()
            if text:
                settings['text'] = text
                break
            print("Input tidak boleh kosong. Silakan coba lagi.")
        
        print("\nPilih gaya font untuk teks Anda:")
        for num, (name, _) in AVAILABLE_FONTS.items():
            print(f"  {num}. {name.capitalize()}")
        
        while True:
            choice = input("\nMasukkan nomor pilihan font (1-5): ")
            if choice in AVAILABLE_FONTS:
                settings['font'] = AVAILABLE_FONTS[choice][1]
                break
            print("Pilihan tidak valid. Silakan masukkan nomor antara 1 dan 5.")
        
    while True:
        try:
            max_zoom = int(input("\nMasukkan level zoom maksimal (angka, antara 3-8): "))
            if 3 <= max_zoom <= 8:
                settings['max_zoom'] = max_zoom
                break
            else:
                print("Level zoom harus antara 3 dan 8. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

    while True:
        try:
            speed = float(input("\nMasukkan kecepatan animasi dalam detik (contoh: 0.3): "))
            if speed > 0:
                settings['speed'] = speed
                break
            else:
                print("Kecepatan harus lebih dari 0. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Harap masukkan angka desimal.")
            
    print("\nPilih warna untuk animasi:")
    colors = {
        '1': ('Merah', Fore.RED), '2': ('Hijau', Fore.GREEN), '3': ('Kuning', Fore.YELLOW),
        '4': ('Biru', Fore.BLUE), '5': ('Magenta', Fore.MAGENTA), '6': ('Cyan', Fore.CYAN),
        '7': ('Putih', Fore.WHITE)
    }
    for num, (name, _) in colors.items():
        print(f"  {num}. {name}")
    
    while True:
        choice = input("\nMasukkan nomor pilihan warna (1-7): ")
        if choice in colors:
            settings['color'] = colors[choice][1]
            break
        print("Pilihan tidak valid. Silakan masukkan nomor antara 1 dan 7.")

    return settings

def draw_character_animation(settings):
    """Fungsi untuk menjalankan animasi karakter tunggal yang terpusat."""
    term_size = get_terminal_size()
    try:
        while True:
            for i in range(1, settings['max_zoom'] + 1):
                clear_screen()
                line = settings['char'] * (i * i)
                padding = (term_size.columns - len(line)) // 2
                print(f"{' ' * padding}{settings['color']}{line}{Style.RESET_ALL}")
                time.sleep(settings['speed'])
            
            for i in range(settings['max_zoom'] - 1, 0, -1):
                clear_screen()
                line = settings['char'] * (i * i)
                padding = (term_size.columns - len(line)) // 2
                print(f"{' ' * padding}{settings['color']}{line}{Style.RESET_ALL}")
                time.sleep(settings['speed'])
    except KeyboardInterrupt:
        clear_screen()
        print(f"{Fore.YELLOW}--- Animasi Dihentikan. Sampai Jumpa! ---{Style.RESET_ALL}")
        sys.exit()

def draw_text_animation(settings):
    """Fungsi untuk menjalankan animasi teks yang sempurna, terpusat, dan halus."""
    term_size = get_terminal_size()
    try:
        while True:
            for zoom in range(1, settings['max_zoom'] + 1):
                clear_screen()
                ascii_text = pyfiglet.figlet_format(settings['text'], font=settings['font'])
                lines = ascii_text.splitlines()
                
                v_padding_top = (zoom - 1) * 2
                print('\n' * v_padding_top)

                for line in lines:
                    if line: 
                        padding = (term_size.columns - len(line)) // 2
                        print(f"{' ' * padding}{settings['color']}{line}{Style.RESET_ALL}")
                    else:
                        print()
                
                time.sleep(settings['speed'])

            for zoom in range(settings['max_zoom'] - 1, 0, -1):
                clear_screen()
                ascii_text = pyfiglet.figlet_format(settings['text'], font=settings['font'])
                lines = ascii_text.splitlines()

                v_padding_top = (zoom - 1) * 2
                print('\n' * v_padding_top)

                for line in lines:
                    if line:
                        padding = (term_size.columns - len(line)) // 2
                        print(f"{' ' * padding}{settings['color']}{line}{Style.RESET_ALL}")
                    else:
                        print()
                
                time.sleep(settings['speed'])

    except KeyboardInterrupt:
        clear_screen()
        print(f"{Fore.YELLOW}--- Animasi Dihentikan. Sampai Jumpa! ---{Style.RESET_ALL}")
        sys.exit()

def main():
    """Fungsi utama yang mengatur alur program."""
    user_settings = get_user_settings()
    
    if user_settings['animation_type'] == '1':
        draw_character_animation(user_settings)
    else:
        draw_text_animation(user_settings)

if __name__ == "__main__":
    main()