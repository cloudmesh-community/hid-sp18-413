
from eve import Eve
import platform
import psutil

app = Eve()

@app.route('/processor')
def processor():

    details = (platform.processor(),
              psutil.virtual_memory(),
              psutil.cpu_stats(),
              psutil.virtual_memory(),
              psutil.disk_partitions(),
              platform.processor(),
              platform.machine(),
              platform.python_version(),
              platform.system())
    return details

if __name__ == '_main_':
    app.run()