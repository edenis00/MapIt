#!/usr/bin/env python3
import webbrowser, sys, pyperclip, urllib.parse

# A program for launching the map using an address

def main():
    if len(sys.argv) > 1:
        # Get the address from command line
        address = ' '.join(sys.argv[1:])

    else:
        # Get the address from the clipboard
        address = pyperclip.paste()
        print('No address was providied. Using address from clipboard')

    print(f"Address: {address}")
    encoded_address = urllib.parse.quote(address)
    
    url = 'https://maps.google.com/maps?q=' + encoded_address
    webbrowser.open(url)

if __name__ == '__main__':
    main()