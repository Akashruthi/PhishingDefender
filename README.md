# PhishingDefender
step 1  - To create Virtual Environment in your system : python -m venv venv

step 2  - To activate the virtual environment : venv\Scripts\activate

step 3  - If not, install your dependencies manually : pip install -r requirements.txt 

	  it is in the Phishing folder..

step 4  - Then run the ( model.py ) Train the model : It will generate two files

	  python main.py :

	  [ phishing_model.pkl , vectorizer.pkl ]

step 5  - Then  run the ( main.py ) 

		python main.py


---------------------Before running this We should configure some options ---------------------

ngrok http 5000 ( in other tab)

(i.e)

.Create an account in the WhatsappMeta Api ( https://developers.facebook.com/docs/whatsapp/ ) and then configure all those things 

.Download Ngrok 

# ✅ How to Install Ngrok on Windows

Step 1: Download Ngrok

1. Go to: [https://ngrok.com/download](https://ngrok.com/download)
2. Click **Download for Windows**
3. Extract the downloaded `.zip` file (you'll get a `ngrok.exe`)

---

Step 2: Add ngrok.exe to Your PATH 

Option A: Temporarily Run from Folder

* Open Command Prompt
* Navigate to the folder where `ngrok.exe` is located:


cd C:\path\to\your\ngrok-folder.\ngrok.exe http 5000

Option B: Add to System PATH Permanently

1. Copy `ngrok.exe` to a permanent folder (e.g., `C:\ngrok\`)
2. Press **Windows + S**, search for **"Environment Variables"**
3. In **System Variables**, find and edit the `Path`
4. Click **New** and add:

   ```
   C:\ngrok\
   ```
5. Click OK on all windows
6. Restart your terminal or Command Prompt
7. Now you can run:

```bash
ngrok http 5000
```

---

Once it's installed, re-run:


ngrok http 5000

## https://github.com/Akashruthi/PhishingDefender/issues/1


Then use the given HTTPS URL as your Webhook Callback URL

step 6  - Finally the messgaes will come in the whatsapp using meta api

	  safe or phishing

