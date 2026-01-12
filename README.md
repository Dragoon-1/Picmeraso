# 🖼️ PicMeraso  
### Image Metadata Viewer & Remover (Python)
<p align="center">
  <img src="assets/banner.png" alt="PicMeraso Banner" width="600">
</p>
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)

> **PicMeraso** is a Python-based desktop application that allows users to **view and remove image metadata (EXIF data)** instantly, without saving or creating a new image file.

---

## ✨ Features

✅ View complete image metadata (EXIF)  
✅ Remove metadata with a single click  
✅ No new image file is saved  
✅ Original image remains untouched  
✅ Supports JPG, JPEG, PNG formats  
✅ Fully offline & privacy-focused  
✅ Simple and user-friendly GUI  

---

## 🧠 What is Image Metadata?

Image metadata is hidden information stored inside images, such as:
- 📍 GPS location
- 📷 Camera model
- 🕒 Date and time
- 🧑 Author or software details

When images are shared online, this data can **leak personal information**.  
**PicMeraso helps you inspect and remove this data safely.**

---

## 🖥️ Project Structure

PicMeraso/
│
├── picmeraso.py              # Main application logic + ui design
├── assets/              # Screenshots / GIFs 
├── requirements.txt     # Required Python libraries
└── README.md            # Project documentation


🚀 How It Works

User selects an image file

Application reads embedded metadata

Metadata is displayed in the UI

User clicks Remove Metadata

Metadata is cleared in memory

🔹 No duplicate image is created
🔹 No file is saved automatically

🛠️ Tech Stack

Python 3

PyQt6 – Graphical User Interface

Pillow – Image handling

ExifRead – Metadata extraction

Piexif – Metadata removal

📦 Installation & Run
git clone https://github.com/your-username/PicMeraso.git
cd PicMeraso
pip install -r requirements.txt
python main.py

🔐 Privacy & Safety

🔒 Works completely offline

📁 No image copies are created

🧠 Metadata handled only in memory

🚫 No user data stored or shared

PicMeraso is designed with privacy-first principles🚀 How It Works

User selects an image file

Application reads embedded metadata

Metadata is displayed in the UI

User clicks Remove Metadata

Metadata is cleared in memory

🔹 No duplicate image is created
🔹 No file is saved automatically

🛠️ Tech Stack

Python 3

PyQt6 – Graphical User Interface

Pillow – Image handling

ExifRead – Metadata extraction

Piexif – Metadata removal

📦 Installation & Run
git clone https://github.com/your-username/PicMeraso.git
cd PicMeraso
pip install -r requirements.txt
python main.py

🔐 Privacy & Safety

🔒 Works completely offline

📁 No image copies are created

🧠 Metadata handled only in memory

🚫 No user data stored or shared

PicMeraso is designed with privacy-first principles
