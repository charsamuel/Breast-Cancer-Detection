import subprocess

def main():
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    subprocess.run(["streamlit", "run", "app.py"])

if __name__ == "__main__":
    main()
