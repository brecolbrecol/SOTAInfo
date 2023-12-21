# SOTAInfo

Fetchs activations related info from SOTA API

## Example

![Example of use](https://github.com/brecolbrecol/SOTAInfo/blob/main/examples/example.png?raw=true)

## ToDo

* [ ] Fetch full summit name (reference + common name) from API.
* [x] Read activators and proposed summits from file.
* [x] Method in Activator to retrieve summits years list for each activator method: `'https://api-db.sota.org.uk/admin/activator_log_by_id?id=45997'`
* [x] ~~Class~~ Script that:
    * [x] Reads activator candidates from list
    * [x] Reads summits candidates from list
    * [x] Order the list by less activated
* [x] Download activators ids json `curl 'https://api-db.sota.org.uk/admin/activator_roll?associationID=48'  |jq ".[] | .Callsign, .UserID"`
* [x] We don't want to abuse that URL, cache it.
* [x] Create class Activator
* [x] SOTAInfo.activators must be a dict { callsign: Activator } instead of a list
