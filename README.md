# TrackListingFix
This was in relation to
[my second ever](https://en.wikipedia.org/wiki/Wikipedia:Bots/Requests_for_approval/DeprecatedFixerBot_1) [Bot Request
for Approval](https://en.wikipedia.org/wiki/Wikipedia:Bots/Requests_for_approval) on the English Wikipedia. The purpose of this task was to remove deprecated parameters
(of [Template:Track listing](https://en.wikipedia.org/wiki/Template:Track_listing)) from pages in [Category:Track listings with deprecated parameters](https://en.wikipedia.org/wiki/Category:Track_listings_with_deprecated_parameters).
The specific parameters to be removed by this task were `|writing_credits=`, `|lyrics_credits=` and `|music_credits=`.
These were to be removed where ever found. The bot worked using the following steps.

1. Select a page from [Category:Track listings with deprecated parameters](https://en.wikipedia.org/wiki/Category:Track_listings_with_deprecated_parameters)
2. Scan all instances of [Template:Track listing](https://en.wikipedia.org/wiki/Template:Track_listing) within the page
    1. If a given instance contained any of the three deprecated parameters (`|writing_credits=`, `|lyrics_credits=` and `|music_credits=`) that were now automated, remove the deprecated parameters and their values. Continue on to the next instance. 
    2. If a given instance did not contain any of the deprecated parameters, then move on to the next instance.
    3. Once all instances on the page were reviewed and any occurrences of the deprecated parameters were removed, save the page.
6. Move on to the next page within the category
