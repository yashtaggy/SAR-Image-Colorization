import ee
PROJECT = "eighth-parity-455109-a1"
ee.Initialize(project=PROJECT)

tasks = ee.batch.Task.list()
for t in tasks:
    print(t.status())
