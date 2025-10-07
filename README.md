# TQWT for Edge Impulse 🧠⚡

**High-performance feature extraction for TinyML using the Tunable Q-Factor Wavelet Transform (TQWT) within Edge Impulse.**

This repository provides a custom processing block that allows you to use TQWT for advanced feature engineering, unlocking new levels of accuracy for signal classification on microcontrollers.

---

## 🎯 Project Overview

Standard feature extraction methods like FFT are powerful but can struggle with signals that are **oscillatory and non-stationary** (e.g., biomedical signals like ECG/EEG or machine vibration data). The **Tunable Q-Factor Wavelet Transform (TQWT)** is specifically designed to analyze such signals by decomposing them into sub-bands with tunable oscillatory behavior.

By integrating TQWT into an **Edge Impulse** pipeline, we can build highly efficient and accurate machine learning models that run directly on edge devices. This project makes that integration seamless.



---

## ✨ Key Features

* **Custom TQWT Processing Block:** Easily add TQWT feature extraction to any Edge Impulse project.
* **Tunable Parameters:** Configure the Q-factor, redundancy, and number of sub-bands to perfectly match your signal's characteristics.
* **Improved Accuracy:** Extract more meaningful features from complex signals, leading to better model performance.
* **Efficient Implementation:** Optimized for deployment on resource-constrained microcontrollers.
* **Example Projects:** Includes sample datasets and impulse projects (e.g., ECG arrhythmia detection, bearing fault analysis) to get you started.

---

## ⚙️ How It Works

1.  **Data Ingestion:** Collect raw time-series data using the Edge Impulse CLI or Studio.
2.  **Custom Processing Block:** Our custom block ingests the raw signal data.
3.  **TQWT Feature Extraction:** The block applies the TQWT algorithm, decomposing the signal. It then calculates statistics (e.g., energy, entropy) from the resulting sub-bands to create a feature vector.
4.  **Model Training:** This feature vector is fed into a neural network or other classifier within Edge Impulse for training.
5.  **Deployment:** The entire pipeline, including the TQWT block and the trained model, is compiled into an efficient library for deployment on your target device.

---

## 🚀 Getting Started

### Prerequisites

* An [Edge Impulse](https://www.edgeimpulse.com/) account (free for developers).
* [Edge Impulse CLI](https://docs.edgeimpulse.com/docs/cli-installation).
* Python 3.8+ and necessary libraries.

### Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/TQWT_Edge_impulse.git](https://github.com/YourUsername/TQWT_Edge_impulse.git)
    cd TQWT_Edge_impulse
    ```

2.  **Follow the setup guide:**
    Detailed instructions for adding this as a custom block to your Edge Impulse project can be found in the `docs/SETUP.md` file.

3.  **Run an example project:**
    Check out the `/examples` directory to test the block with pre-configured datasets for ECG or vibration analysis.

---

## 💡 Potential Applications

This technique is ideal for any project involving complex oscillatory signals on an edge device:

* **🩺 Biomedical:** ECG arrhythmia classification, EEG seizure detection, fetal heart rate monitoring.
* **🏭 Predictive Maintenance:** Detecting faults in motors, bearings, and gears through vibration analysis.
* **🔊 Audio Processing:** Complex sound event detection (e.g., glass breaking, specific alarms).
* **🔬 Structural Health Monitoring:** Analyzing stress and strain wave propagation in materials.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve the TQWT implementation, add new examples, or enhance the documentation, please feel free to fork the repository and submit a pull request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

