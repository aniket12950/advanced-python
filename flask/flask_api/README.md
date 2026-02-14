# 🚀 Flask Authentication API – Thunder Client Testing Guide

This guide explains how to install Thunder Client and test the Register and Login APIs.

---

## ⚡ Step 1: Install Thunder Client

Thunder Client is a VS Code extension (similar to Postman).

### Installation Steps:

1. Open **VS Code**
2. Click the **Extensions** icon (left sidebar)
3. Search for:

   Thunder Client

4. Click **Install**
5. You will see a ⚡ icon in the left sidebar after installation.

---

## ▶ Step 2: Start the Flask Server

Before testing APIs, make sure your server is running.

Open terminal inside your project folder and run:
python run.py
**If successful, you will see:**
Running on http://127.0.0.1:5000
**📝 Step 3: Test Register API**

**1**Click ⚡ Thunder Client

**2**Click New Request

**3**Configure Request:

**Method: POST**

URL:
http://127.0.0.1:5000/api/auth/register

**4**Go to Body

**5**Select JSON

Paste:
{
  "username": "test",
  "email": "test@gmail.com",
  "password": "123456"
}


**6**Click Send

**✅ Expected Response:**

Status: 201 Created

{
  "message": "User registered successfully"
}


**🔐 Step 4: Test Login API**

Click New Request

Configure Request:

**Method: POST**

URL:

http://127.0.0.1:5000/api/auth/login

Body → JSON:


{
  "email": "test@gmail.com",
  "password": "123456"
}


Click Send

**✅ Expected Response:**
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIs..."
}

**⚠ Important Notes**

❌ Do NOT open API URLs in the browser
(Browsers send GET requests by default)

✅ Register/Login require POST requests

✅ Always select JSON in Thunder Client

✅ Make sure the Flask server is running before testing
