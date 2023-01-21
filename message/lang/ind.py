from json import loads
from src.utils import Dict2Obj
from colorama import Fore

config = Dict2Obj(loads(open("config.json", "r").read()))


MENU = Dict2Obj({
    "menu": (
        f"♯ {config.prefix}help | {config.prefix}menu - Menampilkan menu bot\n"
        f"♯ {config.prefix}ping - Menampilkan ping bot\n\n"
        f"♯ {config.prefix}usage - Menampilkan penggunaan perintah bot\n\n"
        f"♯ {config.prefix}menu downloader - Untuk menampilkan menu downloader\n"
        f"♯ {config.prefix}menu sticker - Untuk menampilkan menu sticker\n"
    ),
    "downloader": (
        f"♯ {config.prefix}tiktok - Mendownload video tiktok\n"
    ),
    "sticker": (
        f"♯ {config.prefix}take - Mengambil stiker\n"
        f"♯ {config.prefix}stiker | {config.prefix}s - Mengubah gambar menjadi stiker\n"
        f"♯ {config.prefix}stikergif | {config.prefix}sgif - Mengubah gif/video menjadi stiker\n"
        f"♯ {config.prefix}achievement | {config.prefix}ach - Membuat achievement genshin dan menjadikannya stiker\n"
    )
})

USAGE = Dict2Obj({
    "help": f"{config.prefix}help | {config.prefix}menu",
    "ping": f"{config.prefix}ping",
    "usage": (
        f"Perintah: {config.prefix}usage - {config.prefix}penggunaan\n"
        f"Contoh: {config.prefix}usage downloader\n"
    ),
    "take": (
        f"Balas stiker dengan perintah dibawah\n"
        f"Perintah: {config.prefix}take <author stiker> <pack stiker>\n\n"
        f"Contoh: {config.prefix}take Hitori-Bot @mhankbarbar"
    ),
    "sticker": (
        f"Kirim gambar dengan caption atau balas gambar dengan perintah dibawah\n"
        f"Perintah: {config.prefix}stiker - {config.prefix}s - {config.prefix}sticker"
    ),
    "stickergif": (
        f"Kirim gif/video dengan caption atau balas gif/video dengan perintah dibawah\n"
        f"Perintah: {config.prefix}stikergif - {config.prefix}sgif - {config.prefix}stickergif\n\n"
        f"Catatan: Jika video lebih dari 5 detik, maka akan diambil 5 detik pertama saja"
    ),
    "achievement": (
        f"Perintah: {config.prefix}achievement - {config.prefix}ach - {config.prefix}giachievement\n"
        f"Contoh: {config.prefix}achievement Hitori-Bot adalah bot terbaik yang pernah ada"
    ),
    "toanime": (
        f"Kirim gambar dengan caption atau balas gambar dengan perintah dibawah\n"
        f"Perintah: {config.prefix}jadianime - {config.prefix}toanime"
    ),
    "tiktok": (
        f"Perintah: {config.prefix}tiktok - {config.prefix}tt\n"
        f"Contoh: {config.prefix}tiktok https://vt.tiktok.com/xxxxxxxx/"
    )
})

PROCESSING = "Sedang diproses..."

CAPTION = Dict2Obj({
    "tiktok": (
        f"👤 *Author*: %s\n"
        f"✦ *Title*: %s\n"
        f"✦ *View(s)*: %s\n"
        f"✦ *Like(s)*: %s\n"
        f"✦ *Comment(s)*: %s\n"
        f"✦ *Share*: %s\n"
        f"✦ *Duration*: %s\n"
        f"♬ *Music Title*: %s\n"
    )
})

INFO = (
    f"Bot ini dibuat menggunakan Python.\n\n"
    f"Owner Bot: {config.owner.split('@')[0]}\n"
    f"Source Code: https://github.com/MhankBarBar/hitori-bot\n\n"
    f"© 2023 by *MhankBarBar* made with ❤️"
)

BANNER = (
    f"{Fore.CYAN}╦ ╦{Fore.WHITE}┬┌┬┐┌─┐┬─┐┬  {Fore.CYAN}╦ ╦{Fore.WHITE}┬ ┬┌─┐┌┬┐┌─┐{Fore.CYAN}╔═╗{Fore.WHITE}┌─┐┌─┐  {Fore.CYAN}╔╗ {Fore.WHITE}┌─┐┌┬┐\n"
    f"{Fore.CYAN}╠═╣{Fore.WHITE}│ │ │ │├┬┘│  {Fore.CYAN}║║║{Fore.WHITE}├─┤├─┤ │ └─┐{Fore.CYAN}╠═╣{Fore.WHITE}├─┘├─┘  {Fore.CYAN}╠╩╗{Fore.WHITE}│ │ │\n" 
    f"{Fore.CYAN}╩ ╩{Fore.WHITE}┴ ┴ └─┘┴└─┴  {Fore.CYAN}╚╩╝{Fore.WHITE}┴ ┴┴ ┴ ┴ └─┘{Fore.CYAN}╩ ╩{Fore.WHITE}┴  ┴    {Fore.CYAN}╚═╝{Fore.WHITE}└─┘ ┴"
)
