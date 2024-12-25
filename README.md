# StreamSaver 📥🎵🎥

A visually appealing Android app built with Python that allows users to download videos, songs, MP3s, and MP4s with ease. This app uses **Kivy** for the user interface and supports dynamic progress tracking for downloads. 💡

---

## Features 🌟
- **Download Media:** Supports downloading MP3 and MP4 formats.
- **Clean Interface:** Intuitive and user-friendly design powered by **Kivy** and **KivyMD**.
- **Progress Tracking:** Live progress bar for tracking download status.
- **Multi-purpose:** Works for videos, songs, and other downloadable content.
- **Cross-platform:** Android-ready APK built with Python.

---

## Screenshots 📸
<p align="center">
  <img src="assets/screenshots/home_screen.png" width="250" alt="Home Screen"/>
  <img src="assets/screenshots/downloading.png" width="250" alt="Downloading"/>
  <img src="assets/screenshots/completed.png" width="250" alt="Download Completed"/>
</p>

---

## Technologies Used 🚀
- **Python**: Core programming language.
- **Kivy & KivyMD**: For UI/UX design and Material Design components.
- **Requests**: For downloading content from URLs.
- **Buildozer**: For packaging the Python app into an APK.
- **yt-dlp**: For downloading media from platforms like YouTube.

---

## How to Use 🛠️
1. Clone the repository:
   ```bash
   git clone https://github.com/Nikosane/StreamSaver.git
   cd StreamSaver
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Run the app locally (for testing):
```
python main.py
```
4. To build the APK:
- Install Buildozer:
```
pip install buildozer
```
- Initialize Buildozer:
```
buildozer init
```
- Build the APK:
```
buildozer android debug
```
- Transfer the APK to your Android device and install it.

## Requirements 📋

Python 3.8+
,Kivy 2.1.0+
,Buildozer for APK generation
,Android device for testing the APK.

## Contributing 🤝

Contributions are welcome! Feel free to open issues or submit pull requests. Please ensure your code adheres to the project's style and guidelines.

## License 📄

This project is licensed under the MIT License.

## Acknowledgments 🙌

- Inspired by the versatility of Python and Kivy.
- Thanks to the open-source community for amazing tools like yt-dlp and Kivy.
