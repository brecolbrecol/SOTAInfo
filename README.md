## ToDo

* [ ] Method in Activator to retrieve summits years list for each activator method: `'https://api-db.sota.org.uk/admin/activator_log_by_id?id=45997'`
* [ ] Class that:
    * [ ] Reads activator candidates from list
    * [ ] Reads summits candidates from list
    * [ ] Order the list by less activated
* [x] Download activators ids json `curl 'https://api-db.sota.org.uk/admin/activator_roll?associationID=48'  |jq ".[] | .Callsign, .UserID"`
* [x] We don't want to abuse that URL, cache it.
* [x] Create class Activator
* [x] SOTAInfo.activators must be a dict { callsign: Activator } instead of a list
