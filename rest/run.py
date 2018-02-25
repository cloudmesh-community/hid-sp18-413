from eve import Eve
from flask import jsonify
import platform
import psutil

app = Eve()

@app.route('/processor')
def processor():
    
                    details = (platform.processor(),
                               psutil.virtual_memory(), 
                               platform.version(),  
                               platform.system(),  
                               platform.node(), 
                               platform.machine(), 
                               psutil.cpu_percent())
                   

                    return jsonify(details)



if __name__ == '__main__':
    app.run()
