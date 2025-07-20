# ✈️ CloudFare Airlines – Flight Reservation System

📘 A Python console application for managing domestic airline flight bookings — built for the **DOC 333 - Introduction to Programming Principles** module.  
This system simulates real-world booking operations from flight creation to customer registration, booking, and viewing reports.

---

## 🧰 Features

- 🔐 **Staff Login** (username/password)
- 🛫 **Add Flights** (fixed origin: JFK → multiple destinations)
- 🧑 **Register Customers**
- 🔍 **Search Available Flights** (by date, time, and class)
- 📥 **Book Seats** in Economy or Business Class
- 📄 **View Booking Summary** by Date

---

## 🎮 Console Interface Preview

Below are ASCII-style diagrams representing what users will see in the terminal. This mimics the coursework Figures 1–7.

### 🔐 Login Screen

+–––––––––––––––––––––––––+
|         CloudFare Airlines - Staff Login         |
+–––––––––––––––––––––––––+
| Username -                                       |
| Password -                                       |
| Do you want to login (Yes/No)?                  |
+–––––––––––––––––––––––––+

### 🏠 Main Menu

+–––––––––––––––––––––––––+
|           CloudFare Airlines - Main Menu         |
+–––––––––––––––––––––––––+
| 1) Add flight details                            |
| 2) Register a customer                           |
| 3) Search for available flight details           |
| 4) Booking a flight                              |
| 5) View booking details                          |
| 6) Exit                                          |
|                                                  |
| Your Choice:                                     |
+–––––––––––––––––––––––––+

### 🛫 Add Flight Details

Flight No       : JFK001
Arrival (To)    : Miami
Departure Date  : 19/07/2025
Departure Time  : 20:00
Economy Seats   : 5
Business Seats  : 3
Fare (Economy)  : $500
Fare (Business) : $1000

### 👤 Register Customer

Customer ID     : C001
Name            : Sanuka
Passport No     : N123456
Address         : Colombo
Telephone       : 0771234567
Do you want to save (Yes/No)?

### 🔍 Search Flights

Departure Date  : 19/07/2025
Departure Time  : 20:00
From            : JFK
To              : Miami
Travel Class    : Business Class
Flight No       : JFK001
Seats Available : 2

### 🧾 Booking a Flight

Flight No       : JFK001
Customer Name   : Sanuka
Passport No     : N123456
Class           : Business Class
Do you want to book (Yes/No)?

### 📊 View Booking Details

Departure Date  : 19/07/2025

Flight No   Departure Time  Destination     No of passengers
JFK001      20:00            Miami          2

---

## 🗂️ Project Structure

📁 DOC 333 Coursework Report – 2024XXXX
├── cloudfare_airlines.py     # Main Python source file
├── README.md                 # This file
└── report.pdf                # Your written coursework report

---

## 🧪 Test Case Examples

| Test Case | Input | Expected Output |
|-----------|-------|-----------------|
| Login success | Username: `Staff`, Password: `Cloud123` | `Login successful.` |
| Add flight | JFK001, Miami, 19/07/2025, 20:00 | `Flight JFK001 added successfully.` |
| Book flight | C001 → JFK001 (Business) | `Flight booked successfully.` |
| View bookings | Date: 19/07/2025 | JFK001 appears with 1+ passengers |
| Search typo | `Business clss` instead of `Business Class` | `No matching flights found.` (Fixed with partial matching logic) |

---

## 🖥️ Requirements

- ✅ Python 3.x
- No external libraries needed — works with standard Python IDLE.

---

## 🙋 Author

- 👨‍🎓 **[Your Name]**
- 📚 **Foundation Certificate in Higher Education**
- 📘 **DOC 333 – Introduction to Programming Principles**
- 🧑‍🏫 Guided by: *Ms. Tharushi Amarasinghe*

---

## 🏁 How to Run

```bash
python cloudfare_airlines.py


⸻

📌 Notes
	•	Customer IDs should follow format C001, C002 etc.
	•	Flight numbers follow JFK001, JFK002 etc.
	•	Departure airport is always JFK.
	•	Seat limits: Economy – 5, Business – 3

⸻

🛫 Thank you for flying with CloudFare Airlines!
