# Visit us at [mun.amb.sch.ae](https://mun.amb.sch.ae)

# Accessible Pages
- Home
- Schedule
- Procedures
- Committees and individual committee details
- Gallery
- Contact
- FAQ

## Accessing Admin Portal
1. Go to the `/admin` endpoint of the website or press this link: [https://mun.amb.sch.ae/admin](https://mun.amb.sch.ae/admin)
2. Enter your credentials and log in.

# Modifying Data On the Site
## Home Page Banner
In the admin page go to `Misc` -> `main_banner_text` or `sub_banner_text`, change the `value` key and press `SAVE`

## Main Home Page Button (Default: Schedule)
1. In the admin page go to `Misc` -> `registration_link_text` and change the `value` text to whatever you want the button to say.
2. In the admin page go to `Misc` -> `registration_link_url` and change the `value` url to wherever you want the button to send the user when clicked, you can replace it all and put a google forms link if you want to put AMBMUN's registration form for example or if you want it to point to another part of the site, just set it to the endpoint of that page, example: The schedule page would be: `/Schedule` and procedures would be: `/Rules` etc. 

> [!TIP]
> Check the url bar of your browser on the page you want to set for what comes after the slash and copy that

> [!WARNING]
> All URLs are case sensitive, `/Schedule` and `/schedule` are NOT the same

## Home Page Board Letter
1. In the admin page go to `Misc` -> `board_letter_title` and change the `value` text to whatever you want the First line to be.
2. In the admin page go to `Misc` -> `board_letter_body` and change the `value` text to whatever you want the letter to say.

> [!NOTE]
> The content in `board_letter_body` supports HTML formatting so if you want to make some elements bold or italic you can use `<b>Content goes here</b>` and `<i>Content goes here</i>` respectively. Also, HTML does not support making new lines using the enter key, if u want to create a new line, just add `<br>` to where u want the new line to be.

## Executive Board Members
Go to `Boards` and click on the name of the board member you want to change. Press `SAVE` when you are done
To add a member, just click on the `ADD BOARD` button at the top right.

> [!NOTE]
> To change the order of the members, this requires the whole site to be updated, it cannot be done from the admin portal.

## Chairs
Go to `Chairs` and click on the name of the chair you want to change. Press `SAVE` when you are done
To add a member, just click on the `ADD CHAIR` button at the top right.

> [!CAUTION]
> Do not try to delete a chair without disassociating them from their committee first as it will cause it to delete the chair AND the whole committee aswell. Please read the committees section first.

## Pagers
Go to `Pagers` and click on the name of the pager you want to change. Press `SAVE` when you are done
To add a member, just click on the `ADD PAGER` button at the top right.

> [!CAUTION]
> Do not try to delete a pager without disassociating them from their committee first as it will cause it to delete the pager AND the whole committee aswell. Please read the committees section first.



## Committees
Go to `Committees` and click on the name of the committee you want to change. Press `SAVE` when you are done
To add a member, just click on the `ADD COMMITTEE` button at the top right.

When selecting the chairs: 
- Selecting only **1** chair: Just click on the member u want.
- Selecting **2 or more** chairs: Click on the first member u want then for all subsequent chairs, hold `ctrl` on Windows and `cmd` on Mac and then click on the other chairs.
- Deselecting specific chairs when **2 or more** chairs selected already: Hold `ctrl` on Windows and `cmd` on Mac and then click on the chair you want to remove.

> [!NOTE]
> Committees require atleast 1 chair, if you are creating a new committee, make sure to create the chair first then the committee.

> [!NOTE]
> Same instructions for selecting and deselecting chairs applies to the pagers aswell.

> [!WARNING]
> Make sure the background guide is in either PDF or DOCX format, preferably PDF for ease of access for delegates.

## FAQs
Go to `Faqs` and click on the question of the faq you want to change. Press `SAVE` when you are done
To add a question, just click on the `ADD FAQ` button at the top right.

## Schedule
Go to `Schedule entrys` and click on the ID of the schedule entry you want to change. Press `SAVE` when you are done
To add a schedule entry, just click on the `ADD SCHEDULE ENTRY` button at the top right.

The schedule system calculates the days of the event based on the days specified by the schedule entries, example: if there are 2 schedule entries, one with the date *Jan 15* and another with *Jan 16* then the calculated days of the MUN will be *January 15th 2026 & January 16th 2026* and it will show this at the home page.

The Schedule page automatically adds columns based on the entries aswell, they are grouped by day so each column has the events of that specific day.

> [!NOTE]
> Ignore the message about under the time selectors about the server being 4 hours ahead, it does not affect the schedule. 

> [!NOTE]
> The time selector format is in 24 hour format but will show up as proper 12 hour on the schedule page, the text format inputted is `HH:MM:SS`, `SS` is optional and can be just written as `HH:MM`

> [!NOTE]
> The date selector format inputted is `YYYY-MM-DD`

> [!NOTE]
> You can use the little calender and clock icons to help you set the times for the event more easily.

## Gallery
The gallery contains different albums which those contain the actual media.

### Creating the Album
1. Go to `Albums` and click on the name of the album you want to change or press on the `ADD ALBUM` button at the top right.
2. Set the name and short description for the album and optionally add a cover photo (preferred).
3. Press on `Add another Media item`
4. If you want to add a photo item, click on the `Choose File` button in the photo section and set the `Media Type` dropdown to `Photo` and add a description and select whether it is shown or not. If you want to add a video item, First upload the video to a website that allows embedding the video using a link (for simplicity, use google drive, copy the link of the video and replace the `/view` at the end with `/preview`) paste that link in the `Video` box and set the `Media Type` dropdown to `Video` and add a description and select whether it is shown or not.

> [!NOTE]
> The description shows up underneath the media item in the album page similar to a file name.