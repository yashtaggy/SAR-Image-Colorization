import ee

# Initialize
ee.Initialize(project="eighth-parity-455109-a1")

# List all active tasks
task_list = ee.data.getTaskList()

if not task_list:
    print("[INFO] No tasks found.")
else:
    print(f"[INFO] Found {len(task_list)} tasks:")
    for t in task_list:
        desc = t.get("description", "N/A")
        state = t.get("state", "UNKNOWN")
        err = t.get("error_message", "")
        print(f"- {desc}: {state}")
        if err:
            print(f"   ⚠️ Error: {err}")
