class GoogleRecording:
    def __init__(self, recording_json):
        self.recording_json = recording_json
        self.steps = []

        for step in recording_json["steps"]:
            selenium_step = selenium_lookup_table[step["type"]]
            self.steps.append(inflate_step(selenium_step, step))

    def clean_recording(self, recording_json):
        pass

    def to_json(self):
        return {
            "id": self.recording_json["title"],
            "main": {
                "steps": {
                    "start": {

                    }
                }
            }
        }


selenium_lookup_table = {
    "navigate": {
        "type": "perform",
        "action": "navigate",
        "args": {
            "url": "${url}"
        }
    },
    "click": {
        "type": "perform",
        "action": "click",
        "args": {
            "query": "${selectors}"
        }
    },
    "change": {
        "type": "perform",
        "action": "type_text",
        "args": {
            "query": "${selectors}",
            "value": "${value}"
        }
    }
}


def inflate_step(selenium_step, step):
    for arg in selenium_step["args"]:
        s_arg_value = selenium_step["args"][arg]

        if isinstance(s_arg_value, str) and s_arg_value.startswith("${"):
            property_name = s_arg_value[2:-1]
            if property_name == "selectors":
                selenium_step["args"][arg] = parse_selectors(step)
            else:
                selenium_step["args"][arg] = step[property_name]

    return selenium_step

def parse_selectors(step):
    return " ".join(step["selectors"][0])
