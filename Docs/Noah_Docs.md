# 11/16/25

## General Ideas

Check for a comma in the url, it's an easy typo. It would be nice if that was pointed out to the user when they input a comma instead of a period.

If I click scan headers and then immediately click scan images, there is no indication which one is actually running. Other observation: when you click multiple buttons one after another, the outputs will show all clicked. For example:
		
If I click scan broken links, then scan images, then scan headings all right after another. The output goes in this order > 1. links 2. images 3. headings. Sometimes it will show the reverse order. It would be nice if it took only your last input and used that as the final choice. If you click the buttons too fast one after another, it may not register the last click from the looks of it.

## Vulnerability Scanner

### Port Probe

I inputed 8.8.8.8 into port probe and get results. If you just add a .8 to the end of that and repress the button, all the ports just change to closed, doesn't seem to try to reconnect for some reason. If I give it bogus input (asdfe), it returns all closed ports. Port probe does work on LAN services and IP's. I manually added port 53 in the code for testing pihole on my LAN, it did pick 53 up as open. Main issue for port probe it that it doesn't detect and invalid IP, it just shows all closed.

### Full Scan

Full Scan - If I do the same thing(above) for the full scan, the fingerprinting returns expected (Could not connect to server.) SSL returns expected (SSL check failed: [Errno 11001] getaddrinfo failed) Port Probe has the same issue, it says all ports are closed even though the address is invalid.

## Website Scanner

### Scan Broken Links

Tried google.com, it worked, but the resulting URL it says it checks is http://google.com, NOT https. This seems to be the case for every site. Browser will automatically upgrade to https, so not a huge deal. If you manually put https:// then the output will have https://, but only if you specify in the input. 

### Full Scan

When inputting a valid URL (youtube.com), I get "name 'scan_headers' is not defined" as the output. I tried Google.com and got the same thing. When I first press Full Scan with a good url, it does say Scanning... | This may take a while. It does this before the scan_headers output. I tried 1.1.1.1 and got the exact same output. Scanning... and then scan_headers is the result. 

First output for web scan > full scan
<img width="1095" height="722" alt="Image" src="https://github.com/user-attachments/assets/35937bc0-5987-4ebf-a31f-0d51931c5bd6" />


name 'scan_headers' is not defined pictured below
<img width="1099" height="723" alt="Image" src="https://github.com/user-attachments/assets/e495a2d6-c14b-4879-8e86-d6c3715bc43f" />


These screen shots were taken about 5 seconds apart.
I need to test more edge cases here soon.

# 11/17/25

## Fixed Some Bugs

I fixed the port probe bug we had. All I had to do was add a try/except clause to test connection right after the function was called. It was very simple as we had used the same try/except clause in other modules to prevent this bug. Here was the few lines of code I added below:
```python
try:
    r = requests.get(url, timeout=10)
except Exception:
    return "Could not connect to server."
```

**Matthew** also fixed the scan headers bug as well. That feature now works as expected. 