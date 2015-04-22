from __future__ import division

import csv
import numpy as np
import os
import pandas as pd

file_path = os.path.abspath(".")
dataset = os.path.join(file_path, "orders.tsv")
nutrition = os.path.join(file_path, "nutrition.csv")
print dataset

if __name__ == "__main__":
    with open(dataset, 'rb') as f:
        r = csv.DictReader(f, delimiter="\t")
        results = dict()
        for line in r:
            if line['order_id'] not in results:
                results[line['order_id']] = float(line['item_price'][1:])
            else:
                results[line['order_id']] += float(line['item_price'][1:])

    with open(dataset, 'rb') as f:
        r = csv.DictReader(f, delimiter="\t")
        unique_items = dict()
        for line in r:
            if line['item_name'] not in unique_items:
                unique_items[line['item_name']] = True

    # average order price
    print "average order: $%.2f" % (sum([v for k,v in results.iteritems()]) / len(results))
    # number of unique items on the menu
    print "unique items: %d" % (len(unique_items))

