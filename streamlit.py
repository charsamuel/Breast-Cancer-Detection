import subprocess

def handler(event, context):
    subprocess.run(['streamlit', 'run', 'app.py'], check=True, capture_output=True, text=True)
    return {
        'statusCode': 200,
        'body': 'OK'
    }
