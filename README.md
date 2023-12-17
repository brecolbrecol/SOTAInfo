## ToDo

* [ ] Create class Activator
* [ ] SOTAInfo.activators must be a dict { callsign: Activator } instead of a list
* [ ] Retrieve summits years list for each activator method: `'https://api-db.sota.org.uk/admin/activator_log_by_id?id=45997'`
* [x] Download activators ids json `curl 'https://api-db.sota.org.uk/admin/activator_roll?associationID=48'  |jq ".[] | .Callsign, .UserID"`
* [x] We don't want to abuse that URL, cache it.
