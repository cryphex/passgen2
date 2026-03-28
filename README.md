# 🔐 PassGen2

A simple, powerful desktop password generator built with Tkinter. Generate secure, random passwords with customizable length and copy them to your clipboard with one click! ✨

## 🚀 Features

- **📏 Customizable Length**: Specify the exact number of characters for your password (default: 12)
- **🔒 Secure Generation**: Uses uppercase, lowercase, digits, and special characters (`!"§$%&()=?-_.,:;<+*#>@€{}[]|`)
- **📋 One-Click Copy**: Instantly copy generated passwords to your clipboard with the blue button
- **🖼️ Centered Window**: Automatically centers on your screen for a clean look
- **❄️ Freeze-Ready**: Includes PyInstaller resource path handling for bundled executables

## 📦 Requirements

```txt
tkinter
pyperclip
```

**💡 Note**: `tkinter` comes pre-installed with Python on most systems. `pyperclip` needs to be installed separately.

## 🛠️ Installation

1. 📥 **Clone or download** this repository 

2. 📩 **Install dependencies**:
   ```bash
   pip install pyperclip
   ```

3. 📱 **Run the application**:
   ```bash
   python main.py
   ```

## 🎁 Building an Executable (Optional)

To create a standalone executable using PyInstaller:

```bash
pip install pyinstaller
pyinstaller --clean --onefile --windowed --name PassGen2 --icon=favicon.ico --add-data "favicon.png;." main.py
```

**🔧 Note**: A built exe is already available at the `Releases` tab.

## 📖 Usage

1. Enter the desired password length in the input field (default is 12) 🔢
2. Click **🟢 Generate Password** to create a random password ✨
3. Click **🔵 Copy Output** to copy the password to your clipboard 📋
4. Paste the password wherever you need it 🔑

## 🖥️ Technical Details

| Aspect | Description |
|--------|-------------|
| **Language** | Python 3 🐍 |
| **GUI Framework** | Tkinter 🎨 |
| **Special Characters** | Includes European symbol € and common punctuation 🌍 |
| **Randomization** | Uses Python's `random` module 🎲 |
| **Clipboard** | Powered by `pyperclip` for cross-platform access 🔄 |
| **Window Size** | 450×250 pixels, centered on screen 📐 |

## 📄 License

This project is licensed under the **MIT License** ⚖️ — feel free to use it for personal or commercial projects! 

See the [LICENSE](LICENSE) file for details.
