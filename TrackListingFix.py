import mwclient, ConfigParser
import mwparserfromhell
def main():
    site = mwclient.Site(('https','en.wikipedia.org'), '/w/')
    config = ConfigParser.RawConfigParser()
    config.read('credentials.txt')
    #TODO: site.login(config.get('enwiki','username'), config.get('enwiki', 'password'))
    page = site.Pages['0 to 1 no Aida']#'3 (Bo Bice album)']
    text = page.text()
    wikicode = mwparserfromhell.parse(text)
    templates = wikicode.filter_templates()
    #for template in templates:
     # print("Found template %s" % template.name)
      #for param in template.params:
        # print("\tFound param %s with value %s" % (param.name, param.value))
    text_file = open("Input.txt","w")
    text_file.write(text)
    text_file.close()
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
    text_file = open("Output.txt", "w")
    text_file.write(text)
    text_file.close()
    
if __name__ == "__main__":
    main()
