# Rythukart

🌐 **Live App:** [https://app-f6157d3c-5350-47b5-9efc-b1aa3bbc99ee.cleverapps.io/](https://your-app-link-her) <!-- Replace with your actual deployed URL -->

A smart voice-assisted e-commerce platform where users can interact hands-free—searching and adding products to their cart using natural speech, with personalized greetings and real-time stock feedback.

---

## ✅ Features

- **User Authentication:**  
  Registration and login using mobile number and password.  
  Session-based user tracking using Django's session framework.

- **Product Browsing:**  
  Products are categorized into Vegetables, Pulses, and Rice.  
  Users can browse product categories with stock visibility and images.

- **Cart Management:**  
  Logged-in users can add items to their cart.  
  Quantity updates (increase/decrease) and item removal supported.  
  A cart page displays total price and selected delivery address.

- **Checkout & Address:**  
  Users can add delivery addresses (via live GPS or manually).  
  Checkout page calculates total and confirms orders.  
  Payment simulation leads to cart clearing and order saving.

- **Order Management:**  
  Orders are saved with item details, address, total, and status.  
  Users can view order history.  
  Stock automatically reduces after each successful order.

- **Invoice Download:**  
  Users can download PDF invoices using WeasyPrint.  
  Invoices include product list, quantities, price, and order metadata.

- **Voice Assistant (AI-Enabled):**  
  AI Assistant greets users by name when they click the mic 🎤.  
  Recognizes spoken product names using browser SpeechRecognition API.  
  Matches spoken input with trained product aliases (in English, Hindi, Telugu).  
  Adds items to cart or informs the user if an item is out of stock.  
  Asks if the user wants to continue shopping; redirects to cart if they say "no".

- **Cloud Deployment & Dependency Management:**  
  Cleaned and minimal `requirements.txt` for faster builds and reduced errors.  
  Deployed to a production-ready cloud server.

---

## ⚙️ Tech Stack

| Component         | Technology                      |
| ----------------- | ------------------------------ |
| Backend           | Django, Python                 |
| Frontend          | HTML, CSS, JavaScript          |
| Database          | MySQL                          |
| Voice Assistant   | Web Speech API (JS)            |
| PDF Generation    | WeasyPrint                     |
| AI Voice Matching | Custom logic + knownProducts.js |
| Hosting           | Clever Cloud / Custom server   |

---

## 🌐 Multilingual Support

- Voice recognition supports English, Telugu, and Hindi.
- Responses are spoken in the same language the user uses.
- Known product names are matched using alias and phonetic variants.

---

## 🔒 Security

- CSRF protection on all form submissions.
- Session-based login system.
- Restricted cart access only to logged-in users.

---

## 🚀 Recent Changes

- Cleaned up and minimized `requirements.txt` (unused dependencies removed).
- Cloud deployment enabled (Clever Cloud/MySQL).
- Improved build reliability and faster deployment.


---
