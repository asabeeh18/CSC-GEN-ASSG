import json
import sys

def get_insertion_order(input_json: str) -> str:
    """
    Function returns the optimal order of insertion for the given JSON string of categories, the algorithm in the function
    relies on the fact that each category can only have AT MOST 1 parent category.
    The algorithm uses this fact and simplifies the logic to find the optimal ordering using just a stack
    :param input_json: is the input JSON that contains the product categories to be sorted
    :return:
        str: JSON string, which has the optimal order of insertion
    """
    input_json = json.loads(input_json)
    lookup_dict = {}
    ordered_categ = []  # Stores the final result
    is_done = set()  # If all the parents of a category are inserted add it to this set

    for i in range(len(input_json)):
        # Store the id and this item in the lookup_dict
        item_id = input_json[i]['id']
        lookup_dict[item_id] = input_json[i]

    for item_id in lookup_dict:
        stack = []

        """ 
        While we don't reach an item id without a parent OR an item id which is already good-for-insertion
        add the item id to stack, store parent of item id in item id
        """
        while item_id is not None and item_id not in is_done:
            stack.append(item_id)
            item_id = lookup_dict[item_id]['parent_id']

        """
        Dump the stack to ordered_categ, since we have added parents to the top of stack doing pop on stack will 
        give us the correct insertion order 
        """
        while stack:
            item = stack.pop()
            is_done.add(item)
            ordered_categ.append(lookup_dict[item])

    return json.dumps(ordered_categ)


"""
Run this python script with the JSON file as the command line argument OR
create a file 'ip_json' which has the JSON string and place it in the same directory as the python script
"""
if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = 'ip_json'

    with open(file_path, 'r') as my_file:
        data = my_file.read()

    x = get_insertion_order(data)
    print(x)
