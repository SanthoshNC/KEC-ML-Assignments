## 1 Advanced Git commands 
###  url : https://dev.to/surya_cca7c59900971f19c9b/git-ai-docker-day-2-of-my-ml-journey-was-a-wild-ride-kli
-----


# 🐳 2. Docker Image Creation and Pushing to Docker Hub

---

## Step 1: 🛠️ Create a Dockerfile

- Inside your project folder, create a file named `Dockerfile`.
- Add the following basic instructions:

```dockerfile
FROM python:3.9
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

---

## Step 2: 🏗️ Build the Docker Image

- Open a terminal in your project directory and run:

```bash
docker build -t yourdockerhubusername/yourimagename:tag .
```

✅ Example:

```bash
docker build -t surya2k42/mlproject:latest .
```

---

## Step 3: 🔑 Log In to Docker Hub

- Log in to your Docker Hub account from the terminal:

```bash
docker login
```
(Enter your **Docker Hub username** and **password** when prompted.)

---

## Step 4: 🚀 Push the Image to Docker Hub

- Push your Docker image using:

```bash
docker push yourdockerhubusername/yourimagename:tag
```

✅ Example:

```bash
docker push surya2k42/mlproject:latest
```

-----
## 3 Poster Creation
###  Topic : Improving accuracy in Regression Models
###  image 
-----

