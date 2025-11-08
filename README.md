# 🗂️ File Organizer in Python

A simple automation script that organizes files in a selected folder by their type.  
It automatically detects file extensions (images, videos, documents, music, etc.),  
creates corresponding folders, and moves files into them — helping you keep your  
Downloads or Desktop clean and organized. 💾✨

---

## 🚀 Features
- Detects file types automatically  
- Creates folders (Images, Videos, Documents, Music, Others)  
- Moves files into the correct folder  
- Handles missing folders safely using `os.makedirs()`  
- Uses `try/except` for error handling  

---

## 🧠 Technologies
- Python 3  
- Modules: `os`, `shutil`  

---

## ⚙️ How to Use
1. Clone this repository  
   ```bash
   git clone https://github.com/YOUR_USERNAME/File-Organizer.git
Run the script

bash
Копировать код
python main.py
Enter the path of the folder you want to organize

Sit back and watch the magic happen ✨

📸 Example
Before:

css
Копировать код
Downloads/
│── photo.jpg
│── music.mp3
│── video.mp4
│── notes.pdf
After:

bash
Копировать код
Downloads/
│── Images/photo.jpg
│── Music/music.mp3
│── Videos/video.mp4
│── Documents/notes.pdf
