## ToDo

* [x] Download activators ids json `curl 'https://api-db.sota.org.uk/admin/activator_roll?associationID=48'  |jq ".[] | .Callsign, .UserID"`
* [x] We don't want to abuse that URL, cache it.
