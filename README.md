
# ✈️ CloudFare Airlines – Flight Reservation System

📘 A Python console application for managing domestic airline flight bookings. 
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

Below are ASCII-style diagrams representing what users will see in the terminal. These mimic Figures 1–7 in your coursework.

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

CloudFare Airlines
Add flight details
	1.	Flight No      - JFK001
	2.	Departure (From) - JFK
	3.	Arrival (To)   - Miami
	4.	Departure Date - 19/07/2025
	5.	Departure Time - 20:00
	6.	Economy Seats  - 5
	7.	Business Seats - 3
	8.	Fare Economy   - $500
	9.	Fare Business  - $1000

Do you want to add (Yes/No)?

### 👤 Register Customer

CloudFare Airlines
Register Customer

Customer ID     - C001
Name            - Sanuka
Passport Number - N123456
Address         - Colombo
Telephone Number- 0712345678

Do you want to save (Yes/No)?

### 🔍 Search Flights

CloudFare Airlines
Search for available flights
	1.	Departure Date - 19/07/2025
	2.	Departure Time - 20:00
	3.	Flying From    - JFK
	4.	Flying To      - Miami
	5.	Flight No      - JFK001
	6.	Travel Class   - Business Class
	7.	Seats Available- 2

Do you want to search (Yes/No)?

### 🧾 Booking a Flight

CloudFare Airlines
Booking a flight
	1.	Flight No       - JFK001
	2.	Customer Name   - Sanuka
	3.	Passport Number - N123456
	4.	Destination     - Miami
	5.	Departure Date  - 19/07/2025
	6.	Departure Time  - 20:00
	7.	Travel Class    - Business Class

Do you want to book (Yes/No)?

### 📊 View Booking Details

CloudFare Airlines
View booking details

Departure Date : 19/07/2025

Flight No   Departure Time  Destination     No of passengers
JFK001      20:00            Miami           2

Do you want to view (Yes/No)?

---

## 🗂️ Project Structure

📁 Project
├── cloudfare_airlines.py     # Main Python source file
├── README.md                 # This file
└── report.pdf                # Your coursework report

---

## 🧪 Test Case Examples

| Test Case | Input | Expected Output |
|-----------|-------|-----------------|
| ✅ Login success | Username: `Staff`, Password: `Cloud123` | Login successful |
| ✅ Add flight | JFK001 → Miami | Flight added successfully |
| ✅ Book flight | Customer C001 books JFK001 | Flight booked successfully |
| ✅ View bookings | Date: 19/07/2025 | JFK001 appears with 2 passengers |
---

## 🖥️ Requirements

- Python 3.x
- No external libraries required (works with standard Python IDLE)

---

## 🙋 Author

- 👨‍🎓 **Sanuka Witharana**

---

## 💻 How to Run

```bash
python cloudfare_airlines.py


⸻

🛫 Thank you for flying with CloudFare Airlines!

---
