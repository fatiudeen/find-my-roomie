import subprocess       
import os                                                        
                                                                                   
def start():                                                                   
    cmd =['uvicorn', 'app.main:app', '--reload', '--port', os.getenv('PORT', '5000'), '--forwarded-allow-ips', '*' ]                                                                 
    subprocess.run(cmd) 
