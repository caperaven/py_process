def clean_google_recording(recording_json):
    result_json = {
        "title": recording_json["title"],
        "steps": []
    }

    steps = recording_json["steps"]
    length = len(steps)
    index = 0

    while index < length:
        result = parse_selectors(index, steps)

        if result is None:
            break

        new_step = result[0]
        index = result[1]
        result_json["steps"].append(new_step)

    return result_json


def parse_selectors(index, steps):
    step = steps[index]

    if step["type"] == "change":
        return create_change_step(index, steps)

    next_step = steps[index + 1]

    if step["type"] == "keyDown" and next_step["type"] == "keyUp":
        return ({
            "type": "keyPress",
            "key": step["key"]
        }, index + 2)

    return step, index + 1


def create_change_step(index, steps):
    step = steps[index]
    new_index = find_last_index_of_selector(index, steps, step["selectors"][0])

    step = steps[new_index]

    return ({
        "type": "change",
        "selectors": [step["selectors"][0]],
        "value": step["value"]
    }, new_index + 1)


def find_last_index_of_selector(index, steps, selector):
    # watch for overflow of the list
    if index + 1 >= len(steps):
        return index

    next_step = steps[index + 1]

    # if the next step has different selectors than we expect, we have reached the end of the change
    if "selectors" in next_step and next_step["selectors"][0] != selector:
        return index

    if "key" in next_step:
        if next_step["key"] == "Tab" or next_step["key"] == "Enter":
            return index

    return find_last_index_of_selector(index + 1, steps, selector)
