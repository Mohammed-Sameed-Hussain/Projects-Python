# Auto Tinder Swiper (Failed Attempt 💀)

This repository contains my attempt to build a Python bot using Selenium to automate swiping on Tinder. The goal was to create a script that would log in via Google, handle the UI, and automatically swipe right.

**Current Status:** ❌ **FAILED / ABANDONED**

## 🛑 Why it Failed

Despite successfully automating the browser navigation, the project hit a wall due to Tinder's aggressive anti-bot measures. Specifically:

1.  **CAPTCHA Hell:** Almost immediately after entering the phone number, Tinder triggers visual CAPTCHAs (pick the orientation of the animal, etc.) which are extremely difficult to solve with basic Selenium scripts.
2.  **SMS Verification:** The bot can enter the phone number, but automating the retrieval and entry of the OTP code is complex without third-party APIs.
3.  **Dynamic XPaths:** Tinder's frontend is heavily obfuscated. IDs and Classes change frequently (e.g., `q1388376490`), making XPaths fragile and prone to breaking every few days.
4.  **Google Login Security:** Google often blocks automated browsers from logging in ("This browser or app may not be secure"), requiring lower security settings or complex workarounds.

## 🛠️ Tech Stack Used

* **Python**
* **Selenium WebDriver** (Chrome)

## 💻 How to Run (If you dare)

If you want to witness the failure yourself:

1.  Clone the repo.
2.  Install requirements:
    ```bash
    pip install selenium
    ```
3.  Update `my_gmail`, `my_password`, and `phone_number` in the script.
4.  Run the script:
    ```bash
    python tinder_bot.py
    ```
5.  Watch as it clicks a few buttons and then gets blocked by a CAPTCHA.

## 📝 Lessons Learned

* Web scraping modern SPAs (Single Page Applications) with high security is painful.
* Selenium is great for testing, but easily detected by major platforms.
* Sometimes, it's just easier to swipe with your thumb.

## License

Free to use, modify, or weep over.
