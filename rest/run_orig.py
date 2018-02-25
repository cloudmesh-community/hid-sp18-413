
from eve import Eve
import platform
import psutil
 
app = Eve()

@app.route('/processor')
def processor():
    
    details = (platform.processor(),
                               psutil.virtual_memory(), 
                               psutil.disk_usage('/'), 
                               platform.version(),  
                               platform.system(),  
                               platform.node(), 
                               platform.machine(), 
                               psutil.cpu_percent())
    
    
    return details


if __name__ == '__main__':
    app.run()
