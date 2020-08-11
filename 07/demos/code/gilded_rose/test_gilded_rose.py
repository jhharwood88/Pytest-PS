import csv

import pytest

from gilded_rose import Item, GildedRose


def read_items():
    cases = []
    with open("items.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row['name']
            sell_in = int(row['sell_in'])
            quality = int(row['quality'])
            expected_sell_in = int(row['expected_sell_in'])
            expected_quality = int(row['expected_quality'])

            case = (name, sell_in, quality, expected_sell_in, expected_quality)
            cases.append(case)
    return cases


@pytest.mark.parametrize("name, sell_in, quality, expected_sell_in, expected_quality",
                         read_items())
def test_update_items(name, sell_in, quality, expected_sell_in, expected_quality):
    item = Item(name, sell_in, quality)
    gr = GildedRose([item])
    gr.update_quality()
    assert item.sell_in == expected_sell_in
    assert item.quality == expected_quality

# We read in the items from a spreadsheet, where each test case contains a row from the spreadsheet. This will give values for pre and post argument being called. We use a paramataraized test where the arguemnts will be a list of original arguemtsn as well as the read items argument that reads from the spreadsheet. The item consturctor will create the items, and then put them in the gilded rose item list. We can then update the quality, and then asser that the update quality method is working correctly. This will validate the spreadsheet, and then we can evaluate the tests themselves by using a coverage report to make sure its fully covering the gilded rose methods. We can see from full to partially covered items, as well as uncovered meaning we can then go back and refine our tests cases.