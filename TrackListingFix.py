#!/usr/bin/env python3
import mwclient, configparser, mwparserfromhell

def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts
def call_home(site):#config):
    #page = site.Pages['User:' + config.get('enwiki','username') + "/status"]
    page = site.Pages['User:TweetCiteBot/status']
    text = page.text()
    if "false" in text.lower():
        return False
    return True
def allow_bots(text, user):
    user = user.lower().strip()
    text = mwparserfromhell.parse(text)
    for tl in text.filter_templates():
        if tl.name in ('bots', 'nobots'):
            break
    else:
        return True
    for param in tl.params:
        bots = [x.lower().strip() for x in param.value.split(",")]
        if param.name == 'allow':
            if ''.join(bots) == 'none': return False
            for bot in bots:
                if bot in (user, 'all'):
                    return True
        elif param.name == 'deny':
            if ''.join(bots) == 'none': return True
            for bot in bots:
                if bot in (user, 'all'):
                    return False
    return True
def save_edit(site, original_text,dry_run):#,config):
    #if not allow_bots(original_text, config.get('enwiki','username')):
    #    print("Page editing blocked as template preventing edit is present.")
    #    return
     #print("{}".format(dry_run))
     if not call_home(site):#config):
         raise ValueError("Kill switch on-wiki is false. Terminating program.")
     while True:
         #text = page.edit()
         #text = text.replace('[[Category:Apples]]', '[[Category:Pears]]')
         text = remove_param(original_text,dry_run)
         try:
             if dry_run:
                 print("Dry run")
                 text_file = open("Output.txt", "w")
                 text_file.write(text)
                 text_file.close()
                 break
             else:
                print("Would have saved here")
                break
                #TODO: Enable
                #page.save(text, summary='Removed deprecated parameter(s) from [[Template:Track listing]]', bot=True, minor=True)
         except [[EditError]]:
             print("Error")
             continue
         except [[ProtectedPageError]]:
             print('Could not edit ' + page.page_title + ' due to protection')
         break

def remove_param(text,dry_run):
#    print("In remove {}".format(dry_run))
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
    return str(code) # get back text to save
def main():
    from sys import argv
    myargs = getopts(argv)
    #dry_run = False
    if '--dry-run' in myargs:  # Example usage.
        print(myargs['--dry-run'])
        dry_run = True
    else:
        dry_run = False

    site = mwclient.Site(('https','en.wikipedia.org'), '/w/')
    #config = configparser.RawConfigParser()
    #config.read('credentials.txt')
    #TODO: site.login(config.get('enwiki','username'), config.get('enwiki', 'password'))
    page = site.Pages['0 to 1 no Aida']#'3 (Bo Bice album)']
    text = page.text()

    try:
        save_edit(site, text, dry_run)#, config)
    except ValueError as err:
        print(err)
if __name__ == "__main__":
    main()
