import os
from flask import Flask, render_template, request, redirect, url_for
from azure.data.tables import TableServiceClient
import uuid

app = Flask(__name__)

connection_string = os.environ.get("AZURE_STORAGE_CONNECTION_STRING")
table_service = TableServiceClient.from_connection_string(connection_string)
table_client = table_service.get_table_client(table_name="tasks")

@app.route("/")
def index():
    tasks = list(table_client.list_entities())
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task_name = request.form.get("task")
    if task_name:
        task = {
            "PartitionKey": "tasks",
            "RowKey": str(uuid.uuid4()),
            "name": task_name
        }
        table_client.create_entity(entity=task)
    return redirect(url_for("index"))

@app.route("/delete/<row_key>")
def delete_task(row_key):
    table_client.delete_entity(partition_key="tasks", row_key=row_key)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)