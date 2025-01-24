
import psutil
from flask import Flask, render_template

app = Flask("__name__")

@app.route("/")
def index():
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent
    message = None

    # Check if CPU or Memory is above the threshold
    if cpu_metric > 80 or mem_metric > 80:
        message = "High CPU or Memory Detected, scale up!"
    #return f"CPU Utilization: {cpu_metric} and Memory_Utilization: {mem_metric}"
    return render_template("index1.html", cpu_metric=cpu_metric, mem_metric=mem_metric, message=message)

    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
