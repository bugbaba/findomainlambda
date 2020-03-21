import json
import subprocess
import random
import os


rand_int = random.randint(1,99999)
filename = "/tmp/tmp_subs"+str(rand_int)

def lambda_handler(event, context):
    targetdomain = event['queryStringParameters']['domain']

    cmd = "./findomain-linux -t "+ targetdomain +" -u "+ filename +" --threads 30"
    subprocess.call(cmd, shell=True)
    with open(filename, 'r') as f:
        main_list = f.read().lower().splitlines()
        
    sorted(main_list)
    
    if os.path.exists(filename):
        os.remove(filename)
        print("Deleted file:", filename)
    else:
        print("File doesn't exits", filename)

    return {
        'statusCode': 200,
        'body': json.dumps(main_list)
    }
