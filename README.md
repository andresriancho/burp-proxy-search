# Burp proxy search 
Burp suite HTTP history advanced search and statistics.

This command line tool will process the output of Burp's 
"Proxy / HTTP history / Save items" and extract any information
you need.

The tool is provided with one example plugin that will show all
the unique content security policies found in the HTTP traffic,
but you should be able to quickly extend this tool using new
plugins to extract any information you need.

# Installation

```
git clone git@github.com:andresriancho/burp-proxy-search.git
cd burp-proxy-search
pip install -r requirements.txt
```

# Usage

```
usage: burp-proxy-search.py [-h] [--plugin {unique_csp}] filename
``` 

Example:

```
python burp-proxy-search.py ~/current-project/burp/saved.data
python burp-proxy-search.py ~/current-project/burp/saved.data --plugin your-amazing-plugin
```

# Extending using plugins

1. Create the plugin inheriting from `Plugin`
2. Edit `plugin_manager.py` to add a reference to the new plugin
3. Test and send a pull request ;-)

The plugin needs to implement `process_item` to process each HTTP request
and response, and an `end` method which is called at the end to show the
result.

`process_item` takes a rather complex object as input, I recommend you
inspect it using `print(item.__dict__)`.
