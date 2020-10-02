# wifinder

Google Location services uses multiple methods to physically locate end devices and provide additional context for developers of location-aware software. In addition to IP geolocation, GPS, and cell tower triangulation, Google also exposes a method for trilateralization via wifi access points in the Google Geolocation API which can be used to locate a target based on the basic service set identifiers, or BSSIDs, it is in range of.<sup>[1](https://developers.google.com/maps/documentation/geolocation/overview)</sup>

By setting the "considerIP" key to false in the Geolocation API request and adding the BSSIDs of two or more nearby access points, a set of latitude and longitude coordinates can be retrieved (provided the BSSIDs exist in Google's database) which can then be forwarded to Google's Geocoding API to obtain an approximate street address.<sup>[2](https://developers.google.com/maps/documentation/geocoding/overview)</sup>

Likely the most effective way of obtaining a list of BSSIDs in range of a target device would be through social engineering as the basic service set identifiers of access points are not considered sensitive by the majority of people. Other more exotic ideas might include the use of CSRF to access a router with default credentials and obtain a list of BSSIDs using the wireless site survey function included in most soho networking equipment to diagnose channel interference issues. 

Of course if you have local access to a device, the following commands will list access points in range for each operating system:

Windows:
```
netsh wlan show networks mode=bssid
```
Mac OS:
```
/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport scan
```
Linux:
```
nmcli dev wifi
```

## Notes
It is possible to opt an access point out of inclusion in Google Location services by appending the “_nomap” tag to the wireless access point name (SSID) and then using Google Maps to establish a location fix while connected to the renamed AP.<sup>[3](https://support.google.com/maps/answer/1725632)</sup> Of course, in areas with dense wireless traffic, it might not be possible to change every AP within range thereby still allowing approximate geolocation based on other nearby BSSIDs.

If you absolutely must expose a list of wireless access points around you, best practice would be to obfuscate *at least* the first three bytes of the BSSIDs, also known as the Organizationally Unique Identifier (OUI), which can additionally be used to enumerate your wireless access point's vendor name / manufacturer.<sup>[4](https://www.adminsub.net/mac-address-finder)</sup>

## References
1. https://developers.google.com/maps/documentation/geolocation/overview
2. https://developers.google.com/maps/documentation/geocoding/overview
3. https://support.google.com/maps/answer/1725632
4. https://www.adminsub.net/mac-address-finder
