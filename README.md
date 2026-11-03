# Datheon Python Programming Internship

This repository contains the core technical deliverables completed during the **4-Week Python Programming Internship**. The projects focus on building foundational scripting mechanics, game engineering architecture, clean error handling, data logging routines, and modular software designs.

---

## 📂 Project Structure

```text
Datheon_Python_Programming_Internship/
│
├── hangman.py               # Task 1: Interactive Console Hangman Game
├── portfolio.py             # Task 2: Live Stock Portfolio Performance Tracker
├── portfolio_summary.csv    # Generated data output sheet from Task 2
└── README.md                # Project documentation and setup guide
```

---

## 🎮 Task 1: Hangman Word Guessing Game (`hangman.py`)

An interactive, modular terminal-based game engine implementing control flows, user sanitation checks, custom word pools, and dynamic UI state render loops.

### 🌟 Key Features
* **Dynamic Visual Engine:** Progressively updates and displays a 7-stage structural ASCII gallows schematic on every wrong turn.
* **Input Validation Guardrails:** Prevents crash bugs by blocking numeric entries, multi-character strings, or repeated inputs.
* **Smart Penalty Rules:** Keeps track of previously guessed letters and flags duplicate guesses without losing a turn.
* **Clean State Loops:** Uses continuous evaluations to handle win/loss conditions smoothly.

### 🚀 How to Run
```bash
python hangman.py
```

---

## 📈 Task 2: Stock Portfolio Tracker (`portfolio.py`)

A data-driven investment tracking system utilizing structured dictionary memory caches, valuation arithmetic arrays, error catching blocks, and persistent CSV reporting logs.

### 🌟 Key Features
* **Automated Data Processing:** Calculates real-time cost-basis metrics, market value shifts, and individual stock gains/losses.
* **Formatted Terminal Matrix:** Prints out live account statistics cleanly inside an aligned layout for easy viewing.
* **Dynamic IO Export Engine:** Automatically pipes processing operations out into a clean structural `portfolio_summary.csv` document.
* **Production-Ready Architecture:** Designed using isolated lookup functions, making it ready to connect to real-world live financial APIs.

### 🚀 How to Run
```bash
python portfolio.py
```

---

## 💻 Tech Stack & Environment Specs
* **Language Environment:** `Python 3.x`
* **Development IDE Option:** VS Code / PyCharm / Terminal Editors
* **Core Modules Utilized:** `random`, `csv`, `os` (All part of Python Standard Library—no external dependencies required)

---

## 🛠️ Verification Setup Guide

1. **Clone the Repository:**
   ```bash
   git clone https://github.com
   cd Datheon_Python_Programming_Internship
   ```
2. **Execute & Test Files Locally:** Run the commands provided in the task sections above to verify terminal outputs match implementation rules.
3. **Check Output Sheets:** Ensure `portfolio_summary.csv` automatically updates its entries locally on script completion.
• python • automation • terminal-game • data-logging • csv-processing • software-architecture • internship-project
