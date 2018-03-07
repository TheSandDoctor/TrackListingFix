#!/usr/bin/env python3
import mwclient, configparser
import mwparserfromhell
#import sys

def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

def main():
    from sys import argv
    myargs = getopts(argv)
    dry_run = False
    if '-dry-run' in myargs:  # Example usage.
        print(myargs['-dry-run'])
        dry_run = True
    print(myargs)
    site = mwclient.Site(('https','en.wikipedia.org'), '/w/')
    #config = configparser.RawConfigParser()
    #config.read('credentials.txt')
    #TODO: site.login(config.get('enwiki','username'), config.get('enwiki', 'password'))
    page = site.Pages['0 to 1 no Aida']#'3 (Bo Bice album)']
    text = page.text()
    wikicode = mwparserfromhell.parse(text)
    templates = wikicode.filter_templates()

    #TODO: Testing (dry run) only
    if dry_run:
        text_file = open("Input.txt","w")
        text_file.write(text)
        text_file.close()
    #TODO: End dry run only

    code = mwparserfromhell.parse(text)
    for template in code.filter_templates():#Tracklist, Track, Soundtrack, Tlist, Track list
        template.name = template.name.lower()
        if (template.name.matches("track listing") or template.name.matches("tracklisting")
        or template.name.matches("tracklist") or template.name.matches("track") or template.name.matches("soundtrack")
        or template.name.matches("tlist") or template.name.matches("track list")):
            if template.has("writing_credits"):
                template.remove("writing_credits",False)
                print("Removed writing_credits")
            if template.has("lyrics_credits"):
                template.remove("lyrics_credits",False)
                print("Removed lyrics_credits")
            if template.has("music_credits"):
                template.remove("music_credits",False)
                print("Removed music_credits")
    text = str(code)
    #TODO: save page here with summary
    if dry_run:
        print("DRY")
        text_file = open("Output.txt", "w")
        text_file.write(text)
        text_file.close()
    else:
        print("REAL")
if __name__ == "__main__":
    main()
