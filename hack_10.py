"""
text: "fooziman"  output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    modified_result = []

    for char in result:
        if char == 'o':
            modified_result.extend(['0'])
        elif char == 'i':
            modified_result.extend(['1'])
        elif char == 'a':
            modified_result.extend(['@'])
        else:
            modified_result.extend([char.upper()])

    return modified_result

