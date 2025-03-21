# File-sharing-Bot-For_Termux

<p align="center">
  <a href="https://www.python.org">
    <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" width ="250">
  </a>
  <a href="https://t.me/CodeXBotz">
    <img src="https://github.com/CodeXBotz/PyrogramGenStr/blob/main/resources/madebycodex-badge.svg" width="250">
  </a><br>
  <a href="https://t.me/CodeXBotz">
    &nbsp;<img src="https://img.shields.io/badge/Code%20%F0%9D%95%8F%20Botz-Channel-blue?style=flat-square&logo=telegram" width="130" height="18">&nbsp;
  </a>
  <a href="https://t.me/codexbotzsupport">
    &nbsp;<img src="https://img.shields.io/badge/Code%20%F0%9D%95%8F%20Botz-Group-blue?style=flat-square&logo=telegram" width="130" height="18">&nbsp;
  </a>
  <br>
  <a href="https://github.com/CodeXBotz/File-Sharing-Bot/stargazers">
    <img src="https://img.shields.io/github/stars/CodeXBotz/File-Sharing-Bot?style=social">
  </a>
  <a href="https://github.com/CodeXBotz/File-Sharing-Bot/fork">
    <img src="https://img.shields.io/github/forks/CodeXBotz/File-Sharing-Bot?label=Fork&style=social">
  </a>  
</p>

Telegram Bot to store Posts and Documents and it can Access by Special Links.
I Guess This Will Be Usefull For Many People.....😇. 

---

## About This Fork

This is a **fork** of the original [File-Sharing-Bot](https://github.com/CodeXBotz/File-Sharing-Bot) project by [CodeXBotz](https://github.com/CodeXBotz). The primary focus of this fork is to make the bot **run on Termux** without requiring a **MongoDB URI**. Instead, this version uses **SQLite** as the local database.

### Key Differences:
- **SQLite Database**: The database code has been rewritten to use SQLite, making it easier to run locally without needing a cloud-based MongoDB setup.
- **Termux Compatibility**: This fork is optimized for running on Termux (Android) or other local environments.
- **No Cloud Deployment**: Due to the use of SQLite, this fork is **not suitable for cloud deployment** (e.g., Heroku, Railway, etc.). If you need cloud deployment, please use the [original project](https://github.com/CodeXBotz/File-Sharing-Bot).

---

### Features
- Fully customisable.
- Customisable welcome & Forcesub messages.
- More than one Posts in One Link.
- Protect Content to Prevent Forwarding
- Auto-Delete Files After a Configurable Time

## What’s Next

These features are in the pipeline, and contributions from the community are welcome!

- [x] **Channel Join Request**  
  Implement a feature that prompts users to join a specified Telegram channel before accessing the bot's functionalities.

---

### How to Contribute
1. Check the [contribution guidelines](https://github.com/CodeXBotz/File-Sharing-Bot/blob/main/CONTRIBUTING.md) for detailed instructions.  
2. Pick any feature and create a new issue or comment on an existing one.  
3. Discuss your implementation plan with maintainers to align your contributions with project goals.  

We encourage all developers to contribute ideas, report bugs, and share improvements. Together, we can make this project even better! 🚀

---

### Setup

- Add the bot to Database Channel with all permission
- Add bot to ForceSub channel as Admin with Invite Users via Link Permission if you enabled ForceSub 

---

### Installation

#### Deploy on Termux (Local)
1. Install Termux from the Play Store or F-Droid.
2. Run the following commands in Termux:

```bash
pkg update && pkg upgrade
pkg install git python
git clone https://github.com/YourUsername/File-Sharing-Bot
cd File-Sharing-Bot
pip install -r requirements.txt
```

3. Create a `config.py` file with the required variables (see below).
4. Run the bot:

```bash
python3 main.py
```

---

### Admin Commands

```
/start - start the bot or get posts

/batch - create link for more than one posts

/genlink - create link for one post

/users - view bot statistics

/broadcast - broadcast any messages to bot users

/stats - checking your bot uptime
```

---

### Variables

* `API_HASH` Your API Hash from my.telegram.org
* `APP_ID` Your API ID from my.telegram.org
* `TG_BOT_TOKEN` Your bot token from @BotFather
* `OWNER_ID` Must enter Your Telegram Id
* `CHANNEL_ID` Your Channel ID eg:- -100xxxxxxxx
* `ADMINS` Optional: A space separated list of user_ids of Admins, they can only create links
* `START_MESSAGE` Optional: start message of bot, use HTML and <a href='https://github.com/codexbotz/File-Sharing-Bot/blob/main/README.md#start_message'>fillings</a>
* `START_PIC` Optional: URL or file path of the image to be sent as the start message
* `FORCE_SUB_MESSAGE`Optional:Force sub message of bot, use HTML and Fillings
* `FORCE_SUB_CHANNEL` Optional: ForceSub Channel ID, leave 0 if you want disable force sub
* `PROTECT_CONTENT` Optional: True if you need to prevent files from forwarding
* `AUTO_DELETE_TIME `  Set the time in seconds for automatic file deletion. Default is False, which disables auto-deletion.
* `JOIN_REQUEST_ENABLED` Optional: Set to "True" to enable join request for the channel. Default is "False".

---

### Support   
Join Our [Telegram Group](https://www.telegram.dog/codexbotzsupport) For Support/Assistance And Our [Channel](https://www.telegram.dog/codexbotz) For Updates.   
   
Report Bugs, Give Feature Requests There..   

---

### Credits

- Thanks To Dan For His Awsome [Libary](https://github.com/pyrogram/pyrogram)
- Our Support Group Members

---

### Licence
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0.en.html)  

[FILE-SHARING-BOT](https://github.com/CodeXBotz/File-Sharing-Bot/) is Free Software: You can use, study share and improve it at your
will. Specifically you can redistribute and/or modify it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/gpl.html) as
published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version. 

---

**Star this Repo if you Liked it ⭐⭐⭐**

---