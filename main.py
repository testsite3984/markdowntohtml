import markdown
import os
import sys
import fileinput


def parseMarkdown(markdownTableFilePath, firstHTMLfilePath):
    with open(markdownTableFilePath) as infile, open(firstHTMLfilePath, 'w') as outfile:
        oldContent = infile.read()
        outfile.write("B_E_G_I_N\n")
        newContent = markdown.markdown(oldContent, extensions=['tables'])
        outfile.write(newContent)
        outfile.write("E_N_D\n")
        infile.close()


def parseHTML(firstHTMLfilePath, bootstrapHTMLfilePath):
    replacements = {'B_E_G_I_N': "<!doctype html>\n" +
                " <!--\n" +
                " Material Design Lite\n" +
                " Copyright 2015 Google Inc. All rights reserved.\n" +
                " Licensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License.\n" +
                " You may obtain a copy of the License at\n" +
                " https://www.apache.org/licenses/LICENSE-2.0\n" +
                " Unless required by applicable law or agreed to in writing, software\n" +
                " distributed under the License is distributed on an \"AS IS\" BASIS,\n" +
                " WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n" +
                " See the License for the specific language governing permissions and\n" +
                " limitations under the License\n" +
                " NOTICE in compliance with the License - modified by max\n" +
                "-->\n" +
                "<html lang=\"en\">\n" +
                " <head>\n" +
                "<title>Toddios</title>\n" +
                "<!--MDL-->\n" +
                "<link rel=\"stylesheet\" href=\"https://fonts.googleapis.com/icon?family=Material+Icons\">\n" +
                "<link rel=\"stylesheet\" href=\"https://code.getmdl.io/1.3.0/material.blue_grey-orange.min.css\">\n" +
                " <!--bootstrap-->\n" +
                "<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css\" integrity=\"sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm\" crossorigin=\"anonymous\">\n" +
                " <!--fixes and customization-->\n" +
                "<link rel=\"stylesheet\" href=\"stylishtoddios.scss\">\n" +
                "\n" +
                "<meta charset=\"utf-8\">\n" +
                "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\">\n" +
                "</head>\n" +
                "<body class=\"mdl-demo mdl-color--grey-100 mdl-color-text--grey-700 mdl-base\">\n" +
                "<div class=\"mdl-layout mdl-js-layout\">\n" +
                "<header class=\"mdl-layout__header mdl-layout__header--scroll\">\n" +
                " <div class=\"mdl-layout__header-row\">\n" +
                " <!-- title - left empty for now -->\n" +
                "<span class=\"mdl-layout-title\"></span>\n" +
                " <!-- navigation to the right -->\n" +
                "<div class=\"mdl-layout-spacer\"></div>\n" +
                " <!-- extra navigation -->\n" +
                "<nav class=\"mdl-navigation\">\n" +
                " <a class=\"mdl-navigation__link\" href=\"index.html\">Home</a>\n" +
                " <a class=\"mdl-navigation__link\" href=\"https://notwhorosethinks.com/faq.html\">FAQ</a>\n" +
                " <a class=\"mdl-navigation__link\" href=\"https://www.patreon.com/notwhorosethinks\">Patreon</a>\n" +
                " <a class=\"mdl-navigation__link\" href=\"https://docs.google.com/forms/d/16pvofg2HoMDkAh2JWW_nXkaJGnuVNhC7H5JHFje4Cj0/viewform?edit_requested=true\">NonConditional Love</a>\n" +
                " </nav>\n" +
                "</div>\n" +
                "</header>\n" +
                "<!-- drawer sidebar -->\n" +
                "<div class=\"mdl-layout__drawer\">\n" +
                "<span class=\"mdl-layout-title\">Toddios</span>\n" +
                "<nav class=\"mdl-navigation\">\n" +
                "<a class=\"mdl-navigation__link\" href=\"megatable.html\">Entire Table</a>\n" +
                "<a class=\"mdl-navigation__link\" href=\"1patreonExclusives.html\">Patreon Exclusives</a>\n" +
                "<a class=\"mdl-navigation__link\" href=\"2syrinExclusives.html\">Syrin Exclusives</a>\n" +
                "<a class=\"mdl-navigation__link\" href=\"3publicAudios.html\">Public Audios</a>\n" +
                "<a class=\"mdl-navigation__link\" href=\"4youtube.html\">YouTube</a>\n" +
                "<a class=\"mdl-navigation__link\" href=\"5subExclusives.html\">Subreddit Exclusives</a>\n" +
                "<a class=\"mdl-navigation__link\" href=\"6candid.html\">Candid</a>\n" +
                "<a class=\"mdl-navigation__link\" href=\"7reading.html\">Reading</a>\n" +
                "<a class=\"mdl-navigation__link\" href=\"8shitposts.html\">Shitposts</a>\n" +
                "<a class=\"mdl-navigation__link\" href=\"9nonconLove.html\">NonConditional Love</a>\n" +
                "<a class=\"mdl-navigation__link\" href=\"10unrec.html\">Old (And Unrecommended) Audios</a>\n" +
                "<a class=\"mdl-navigation__link\" href=\"11TSC.html\">Todd's Story Cubes Series</a>\n" +
                "<a class=\"mdl-navigation__link\" href=\"12bucket.html\">Bucket</a>\n" +
                " <a class=\"mdl-navigation__link\" href=\"13graveyard.html\">Graveyard</a>\n" +
                " </nav>\n" +
                "</div>\n" +
                "<!-- table opens -->\n" +
                "<center>\n", '<h2>': '<h4 style=\"padding-bottom: 10px; padding-top: 10px;\">',
                    '</h2>': '</h4>', '<table>': '<div class=\"table-responsive\">\n<table class=\"table table-bordered\">',
                    '<th>': '<th scope="col">', 'E_N_D': ' </div>\n' +
                "</div>\n" +
                " </center>\n" +
                " <!-- end table -->\n" +
                "<!--MDL-->\n" +
                "<script defer src=\"https://code.getmdl.io/1.3.0/material.min.js\"></script>\n" +
                "<!--bootstrap-->\n" +
                "<script src=\"https://code.jquery.com/jquery-3.2.1.slim.min.js\" integrity=\"sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN\" crossorigin=\"anonymous\"></script>\n" +
                "<script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js\" integrity=\"sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q\" crossorigin=\"anonymous\"></script>\n" +
                "<script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js\" integrity=\"sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl\" crossorigin=\"anonymous\"></script>\n" +
                "</body></html>"}

    with open(firstHTMLfilePath) as infile, open(bootstrapHTMLfilePath, 'w') as outfile:
        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, target)
            outfile.write(line)


# parseMarkdown(os.path.join('S:', 'truetestytable.txt'), os.path.join('S:', 'HTMLinput.txt'))
# parseHTML(os.path.join('S:', 'HTMLinput.txt'), os.path.join('S:', 'testsite3984', 'test-site', 'htmltest.html'))
parseMarkdown(input("Markdown table's file path: "), os.path.join('C:', 'HTMLinput.txt'))
parseHTML(os.path.join('C:', 'HTMLinput.txt'), input("File path of HTML to overwrite: "))
