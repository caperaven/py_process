recording_key_press = {
    "title": "Key Press Recording",
    "steps": [
        {
            "type": "keyDown",
            "target": "main",
            "key": "Tab"
        },
        {
            "type": "keyUp",
            "key": "Tab",
            "target": "main"
        }
    ]
}

recording_change = {
    "title": "Change Recording",
    "steps": [
        {
            "type": "change",
            "value": "H",
            "selectors": [
                [
                    "container-component",
                    "child-component",
                    "label:nth-of-type(1) > input"
                ],
                [
                    "aria/First Name"
                ]
            ],
            "target": "main"
        },
        {
            "type": "keyUp",
            "key": "h",
            "target": "main"
        },
        {
            "type": "change",
            "value": "Hello W",
            "selectors": [
                [
                    "container-component",
                    "child-component",
                    "label:nth-of-type(1) > input"
                ],
                [
                    "aria/First Name"
                ]
            ],
            "target": "main"
        },
        {
            "type": "keyUp",
            "key": "w",
            "target": "main"
        },
        {
            "type": "change",
            "value": "Hello World",
            "selectors": [
                [
                    "container-component",
                    "child-component",
                    "label:nth-of-type(1) > input"
                ],
                [
                    "aria/First Name"
                ]
            ],
            "target": "main"
        }
    ]
}

recording_large = {
    "title": "Large Recording",
    "selectorAttribute": "id",
    "steps": [
        {
            "type": "setViewport",
            "width": 918,
            "height": 1315,
            "deviceScaleFactor": 1,
            "isMobile": False,
            "hasTouch": False,
            "isLandscape": False
        },
        {
            "type": "navigate",
            "url": "http://127.0.0.1:8080/web/",
            "assertedEvents": [
                {
                    "type": "navigation",
                    "url": "http://127.0.0.1:8080/web/",
                    "title": "Document"
                }
            ]
        },
        {
            "type": "click",
            "target": "main",
            "selectors": [
                [
                    "[id='cbCSS']"
                ]
            ],
            "offsetY": 7.125,
            "offsetX": 5
        },
        {
            "type": "click",
            "target": "main",
            "selectors": [
                [
                    "container-component",
                    "child-component",
                    "label:nth-of-type(1) > input"
                ]
            ],
            "offsetY": 0.3125,
            "offsetX": 71
        },
        {
            "type": "change",
            "value": "H",
            "selectors": [
                [
                    "container-component",
                    "child-component",
                    "label:nth-of-type(1) > input"
                ]
            ],
            "target": "main"
        },
        {
            "type": "keyUp",
            "key": "h",
            "target": "main"
        },
        {
            "type": "change",
            "value": "Hello W",
            "selectors": [
                [
                    "container-component",
                    "child-component",
                    "label:nth-of-type(1) > input"
                ]
            ],
            "target": "main"
        },
        {
            "type": "keyUp",
            "key": "w",
            "target": "main"
        },
        {
            "type": "change",
            "value": "Hello World",
            "selectors": [
                [
                    "container-component",
                    "child-component",
                    "label:nth-of-type(1) > input"
                ]
            ],
            "target": "main"
        },
        {
            "type": "keyDown",
            "target": "main",
            "key": "Tab"
        },
        {
            "type": "keyUp",
            "key": "Tab",
            "target": "main"
        },
        {
            "type": "keyDown",
            "target": "main",
            "key": "Tab"
        },
        {
            "type": "keyUp",
            "key": "Tab",
            "target": "main"
        },
        {
            "type": "keyDown",
            "target": "main",
            "key": "Tab"
        },
        {
            "type": "keyUp",
            "key": "Tab",
            "target": "main"
        },
        {
            "type": "keyDown",
            "target": "main",
            "key": "Enter"
        },
        {
            "type": "keyUp",
            "key": "Enter",
            "target": "main"
        }
    ]
}

recording_click_sequence = {
    "title": "click",
    "selectorAttribute": "id",
    "steps": [
        {
            "type": "click",
            "target": "main",
            "selectors": [
                [
                    "container-component",
                    "child-component",
                    "label:nth-of-type(1) > input"
                ]
            ],
            "offsetY": 14.3125,
            "offsetX": 121
        },
        {
            "type": "click",
            "target": "main",
            "selectors": [
                [
                    "container-component",
                    "child-component",
                    "label:nth-of-type(2) > input"
                ]
            ],
            "offsetY": 7.3125,
            "offsetX": 123
        },
        {
            "type": "click",
            "target": "main",
            "selectors": [
                [
                    "container-component",
                    "child-component",
                    "label:nth-of-type(3) > input"
                ]
            ],
            "offsetY": 16.3125,
            "offsetX": 125
        },
        {
            "type": "doubleClick",
            "target": "main",
            "selectors": [
                [
                    "container-component",
                    "child-component",
                    "label:nth-of-type(1) > input"
                ]
            ],
            "offsetY": 14.3125,
            "offsetX": 47
        },
        {
            "type": "doubleClick",
            "target": "main",
            "selectors": [
                [
                    "container-component",
                    "child-component",
                    "label:nth-of-type(2) > input"
                ]
            ],
            "offsetY": 6.3125,
            "offsetX": 57
        },
        {
            "type": "doubleClick",
            "target": "main",
            "selectors": [
                [
                    "container-component",
                    "child-component",
                    "label:nth-of-type(3) > input"
                ]
            ],
            "offsetY": 5.3125,
            "offsetX": 64
        }
    ]
}
