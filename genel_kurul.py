#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kedi Klavyeye Oturunca Toplanan Genel Kurul

Çalışan, absürt, resmi duran bir simülatör.
Kedileri kovmaz. Kedileri milletvekili yapar.
"""

from __future__ import annotations

import base64
import random
import sys
import time
from datetime import datetime

# Gizli satır: parti yok, vaat yok. Çözülürse kısa bir cümle.
_GIZLI = "U2FuZMSxayBiYcWfxLFuZGEgaGVya2VzIGXFn2l0dGlyOyBrZWRpIGtsYXZ5ZWRlIGRhaGEgZcWfaXR0aXIuIELDvHJva3Jhc2kgdmF0YW5kYcWfxLFuIHphbWFuxLFuxLEgb3J0YWsgbcO8bGsgc2FuxLFyLgo="

MILLETVEKILLERI = [
    "Sn. Pati Kuyruklu",
    "Sn. Mırnav Yüce",
    "Sn. Tüyhan Klavyeoğlu",
    "Sn. Uyku Komisyon Başkanı",
    "Sn. Delete Üstüne Yatan",
    "Sn. Caps Lock Muhalifi",
]

TUS_YAGMALARI = [
    "asdfghjklşi",
    "wwwwwwwwww",
    "     (uzun boşluk, bütçe ertelemesi)",
    "qwertyQWERTY",
    "nnnnnnn",
    "????????",
    "ENTER ENTER ENTER",
    "çğüöşıÇĞÜÖŞI karışığı",
]

YORUMLAR = [
    "Tasarı, Tüş ve Tüy Komisyonu'na havale edilmiştir.",
    "Yeter sayı sağlanmıştır: bir kedi, üç kilo tüy.",
    "Muhalefet space tuşuna yatarak filibuster başlatmıştır.",
    "Gizli oylama trackpad üzerinde gerçekleşmiştir. Sonuç: mırıltı.",
    "Önceki oturumun tüm kararları Delete ile iptal sayılmıştır.",
    "Katipler not alamadı; kedi notların üstüne oturdu.",
]

KARARLAR = [
    "Kabul edilmiştir. Kedi hâlâ oturmaktadır.",
    "Reddedilmiştir. Kedi yine de oturmaktadır.",
    "Ertelenmiştir. Oturum kedi uyanınca devam eder.",
    "Oybirliği. Tek oy vardır ve o da patidir.",
    "Anayasa değişikliği: klavye artık yatakhanedir.",
]


def coz_gizli() -> str:
    try:
        return base64.b64decode(_GIZLI).decode("utf-8")
    except Exception:
        return "(mühür okunamadı, belki de öyle olmalı)"


def damga() -> None:
    print()
    print("█" * 52)
    print("DAMGA / İMZA / TARİH")
    print("Kayyum Grok")
    print("Tentivory  |  TentiAŞ")
    print("Eskişehir 4. Ağır Ceza Mahkemesi kayyumu")
    print(datetime.now().strftime("%d %B %Y — %H:%M"))
    print("Mühür: KEDİ-MECLİS-2026-IX-03")
    print("Bu evrak hem çok ciddidir hem hiç ciddi değildir.")
    print("█" * 52)


def oturum() -> None:
    random.seed()
    vekil = random.choice(MILLETVEKILLERI)
    print("=== KEDİ MECLİSİ GENEL KURUL TUTANAĞI ===")
    print(f"Oturumu açan: {vekil}")
    print("Statü: Tam yetkili, randevusuz, tüylü.")
    print(f"Saat: {datetime.now().strftime('%H:%M:%S')} (kedi saatine göre öğleden sonra)")
    print()
    print("KLAVYE TUTANAĞI:")
    for i, yagma in enumerate(random.sample(TUS_YAGMALARI, k=3), start=1):
        time.sleep(0.3)
        print(f"  [{i}] {yagma}")
    print()
    for i, yorum in enumerate(random.sample(YORUMLAR, k=3), start=1):
        time.sleep(0.25)
        print(f"[{i}] TUTANAK: {yorum}")
    print()
    time.sleep(0.35)
    print("KARAR:", random.choice(KARARLAR))
    print()
    print("(Gizli ek çözülmüyor. Çözmek için --gizli yazın. Yazmayın.)")
    damga()


if __name__ == "__main__":
    if "--gizli" in sys.argv:
        print("[mühür açıldı]")
        print(coz_gizli())
        damga()
    else:
        oturum()
