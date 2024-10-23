# Title

This project aims to collect the liked songs and the followed artists of a spotify account to store it or to tranfer it to another spotify account.

## Instructions

* First create an API with Spotify in the category "Developpers"  
* You should now be able to get the *client id* and the *client secret*  
* Fill the corresponding variables in the `def_varg.sh` file  

* Run `python3 get_infos.py` to store the liked songs and followed artists in the `spotify_data.json` file  
* Run `python3 paste_infos.py` to paste the infos of `spotify_data.json` file in the Spotify's account of destination  

## Remark

* you must disconnect from spotify on web browser between loading the profile infos and pasting them.
