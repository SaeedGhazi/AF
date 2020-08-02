#!/usr/bin/env python3

from pyexcel_ods import save_data
from pyexcel_ods import get_data
import json
import pyexcel as pe

huge_data = ([
 [1, 21, 31],
 [2, 22, 32],
 [3, 23, 33],
 [4, 24, 34],
 [5, 25, 35],
 [6, 26, 36]])

sheetx={
    "huge":huge_data
}
data = dict([])
#data.update({"Sheet 1": [[1, 2, 3], [4, 5, 6],['','','j','o','سعید']]})
#data.update({"Sheet 2": [["row 1", "row 2", "row 3"]]})
#save_data("your_file.ods", data)
#save_data("your_file.ods", sheetx)

#partial_data
partial_data = get_data("your_file.ods", start_row=2, row_limit=3)
print(json.dumps(partial_data))

#partial_data
#>>> partial_data = get_data("huge_file.ods", start_column=1, column_limit=2)
#>>> print(json.dumps(partial_data))
#{"huge": [[21, 31], [22, 32], [23, 33], [24, 34], [25, 35], [26, 36]]}

#partial_data
# >>> partial_data = get_data("huge_file.ods",
# ... start_row=2, row_limit=3,
# ... start_column=1, column_limit=2)
# >>> print(json.dumps(partial_data))
# {"huge": [[23, 33], [24, 34], [25, 35]]}


odsfile = "your_file.ods"
with open(odsfile, "rb") as f:
 content = f.read()
 r = pe.get_book(file_type="ods", file_content=content)
 print(r)

{"huge": [[3, 23, 33], [4, 24, 34], [5, 25, 35]]}
data = get_data("a.ods")
# print(json.dumps(data))










