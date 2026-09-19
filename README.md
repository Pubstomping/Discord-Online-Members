# 🤖 Discord Multi-Account Human Persona Selfbot

A modular Python-based multi-account selfbot using `discord.py-self` designed to simulate human online behavior. It automatically rotates statuses, plays custom lists of games (Call of Duty, Rainbow Six, Fortnite, GTA V, etc.), cycles through curated music tracks, and manages statuses (`Online`, `Idle`, `DnD`, and `Offline`/Sleep) dynamically.

---

## ⚠️ Important Warning
* **Terms of Service:** This tool runs on **normal user accounts (selfbots)**. Automating personal user accounts violates Discord's Terms of Service and carries a **high risk of permanent account bans**. Use at your own risk and avoid using your main personal account.

---

## 📂 Project Structure

Make sure you have all three of these files in the same project directory:
1. `selfbot.py` - The main automation and status-rotation script.
2. `data.py` - The master database containing massive lists of games and music tracks.
3. `start.bat` - The interactive Windows batch menu to manage accounts and tokens.

---

## 🚀 Setup & Installation

### 1. Prerequisites
Ensure you have **Python 3.8+** installed on your system. Install the required selfbot library via your command prompt/terminal:
```bash
pip install discord.py-self
