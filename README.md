# sti2017

Fadhli [SKU && MetricPollers]

============Rack-HD Token============================

GET-TOKEN:

curl http://localhost:5000/rackhd/login -d '{"username":"admin","password":"admin123"}' -H "Content-Type: application/json" -X POST | python -m json.tool

============SKUs=====================================

SKU-CREATE:

curl http://localhost:5000/rackhd/skus/create -d '{"name":"Intel 32GB RAM","path":"dmi.Base Board Information.Manufacturer","contains":"Intel","discoveryGraphName":"Graph.InstallCoreOS","path2":"ohai.dmi.memory.total","equals":"32946864kB","username":"testuser","password":"hello","hostname":"mycoreos"}' -H "Content-type: application/json" -X POST -H 'token:<token>' | python -m json.tool

SKU-READ:

curl http://localhost:5000/rackhd/skus/read -X GET -H 'token:<token>' | python -m json.tool

SKU-UPDATE:

curl http://localhost:5000/rackhd/skus/update -d '{"skuId":"<SKU ID>","field":"password","data":"testpassword"}' -H "Content-type: application/json" -X PATCH -H 'token:<token>' | python -m json.tool

SKU-DELETE:

curl http://localhost:5000/rackhd/skus/delete -d '{"skuId":"<SKU ID>"}' -H "Content-type: application/json" -X DELETE -H 'token:<token>' | python -m json.tool

============METRIC POLLERS============================

METRICPOLLER-READ:

curl http://localhost:5000/rackhd/metricpollers/read -X GET -H 'token:<token>' | python -m json.tool

METRICPOLLER-CREATE:

curl http://localhost:5000/rackhd/metricpollers/create -d '{"type":"snmp","node":"54daadd764f1a8f1088fdc42","metric":"snmp-interface-bandwidth-poller"}' -H "Content-type: application/json" -X POST -H 'token:<token>' | python -m json.tool

METRICPOLLER-UPDATE:

curl http://localhost:5000/rackhd/metricpollers/update -d '{"pollerId":"<Poller ID>", "paused":"true", "pollInterval":"1000", "type":"snmp"}' -H "Content-type: application/json" -X PATCH -H 'token:<token>' -u admin:python | python -m json.tool

METRICPOLLER-DELETE:

curl http://localhost:5000/rackhd/metricpollers/delete -d '{"pollerId":"<Poller ID>"}' -H "Content-type: application/json" -X DELETE -H 'token:<token>' | python -m json.tool
