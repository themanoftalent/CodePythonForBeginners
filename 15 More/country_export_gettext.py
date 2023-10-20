##################################################
#### **************************************** ####
#### !/usr/bin/python3                        ####
#### -*- coding: utf-8 -*-                    ####
#### @Time    : 2023/20/10 11:40              ####
#### @Author  : themanoftalent                ####
#### @Site:https://github.com/themanoftalent  ####
#### @Project : python-app                    ####
#### **************************************** ####
##################################################


from django.core.management.base import BaseCommand
from django.utils.encoding import smart_str



class Command(BaseCommand):
    help = "Exports a gettext file to translate the country names (only translation without header)"

    def handle(self, *args, **options):
        with open('country_translations.po', 'w') as po_file:
            for country in Country.objects.all():
                po_file.write('# country {}\n'.format(smart_str(country.iso)))
                po_file.write('msgid "{}"\n'.format(smart_str(country.printable_name.replace('"', '\\"'))))
                po_file.write('msgstr ""\n')
                po_file.write('\n')

        self.stdout.write(self.style.SUCCESS('Successfully exported translations to country_translations.po'))


