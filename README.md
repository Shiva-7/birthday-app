# birthday-app | Birthday Sparkle – Know Your Shine Time!|

GitHub + GitHubActions + Docker + AWS(EC2)

🛠️ What We Built: A Full CI/CD Pipeline for a Flask App (Birthday Sparkle)

# 🐍 1. Python + Flask: The Heart of Our App

This is where we began.
Flask is the micro web framework we used to create our birthday app.
We wrote a Python script (app.py) where:
It had a form to accept name, DOB, and gender.
Based on the inputs, we calculated the user’s age and days until their next birthday.
Displayed a cute, gender-specific message too 🎉

📂 Files involved: app.py, requirements.txt (for Flask dependency)


# 🐳 2. Dockerizing the App: Boxing the Love
Once the app worked locally, we Dockerized it. That means we packed our app in a container so it can run anywhere!

We wrote a Dockerfile:
It defined a Python base image
Installed Flask using pip
Copied our app files into the container
Exposed port 5000 and ran the app
Then we used docker-compose.yml to:
Build the image
Run the container
Manage it with simple up/down commands

🧠 This made our app platform-independent, portable, and ready for EC2 hosting.

# ☁️ 3. EC2: Our Cloud Home

This is where our app went live!
We launched an Ubuntu-based EC2 instance.
Installed Docker and Docker Compose on it.
Created a key pair to access it securely.
Exposed port 5000 in the security group so people could visit our app.

🌍 After deploying, the app became accessible at:
http://<EC2-IP>:5000

# 🧠 4. GitHub Actions: The Smart Automation

Here comes the CI/CD magic!
We created a .github/workflows/deploy.yml file.
This workflow:
Triggered on every git push to main
SSH’ed into EC2 using secrets like EC2_USER, EC2_HOST, and EC2_KEY
Did a git pull on EC2
Ran docker-compose down && docker-compose up --build -d

🚀 This automated our deployment. So now, whenever we push new code — it goes live automatically 💥

Thanks for the reading !!! hope this was insightful.
