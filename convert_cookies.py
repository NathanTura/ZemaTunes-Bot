#!/usr/bin/env python3
import json
import sys
import os

def convert_json_to_netscape(json_path, netscape_path):
    if not os.path.exists(json_path):
        print(f"Error: Source file '{json_path}' does not exist.")
        return False
        
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if not isinstance(data, list):
            print("Error: JSON cookies must be a list of cookie objects.")
            return False
            
        lines = [
            "# Netscape HTTP Cookie File",
            "# This file was generated automatically by ZemaTunes-Bot cookies converter.",
            ""
        ]
        
        for cookie in data:
            domain = cookie.get('domain', '')
            path = cookie.get('path', '/')
            secure = 'TRUE' if cookie.get('secure', False) else 'FALSE'
            expires = str(int(cookie.get('expirationDate', 0)))
            name = cookie.get('name', '')
            value = cookie.get('value', '')
            subdomains = 'TRUE' if domain.startswith('.') else 'FALSE'
            
            lines.append(f"{domain}\t{subdomains}\t{path}\t{secure}\t{expires}\t{name}\t{value}")
            
        with open(netscape_path, 'w', encoding='utf-8') as out:
            out.write("\n".join(lines))
            
        print(f"Success! Converted '{json_path}' -> '{netscape_path}' (Netscape format).")
        return True
    except Exception as e:
        print(f"Error: Conversion failed. {e}")
        return False

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] in ('-h', '--help'):
            print("Usage: python convert_cookies.py [input_json_path] [output_txt_path]")
            print("Default: converts 'cookies.json' to 'cookies.txt'")
            sys.exit(0)
            
    input_file = 'cookies.json'
    output_file = 'cookies.txt'
    
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
        
    if not os.path.exists(input_file):
        # Scan current directory for any .json file if default cookies.json is not found
        json_files = [f for f in os.listdir('.') if f.endswith('.json') and f != 'package.json']
        if json_files:
            input_file = json_files[0]
            print(f"Default 'cookies.json' not found. Using alternative: '{input_file}'")
            
    success = convert_json_to_netscape(input_file, output_file)
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
