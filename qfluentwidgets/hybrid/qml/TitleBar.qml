import QtQuick 2.15

Rectangle {
    id: root
    height: 48
    property var safeBridge: bridge
    property var safeStyle: safeBridge ? safeBridge.style : ({
        surface: "#F3F3F3",
        hover: "#22000000",
        pressed: "#33000000",
        text: "#1A1A1A"
    })
    property string safeTheme: safeBridge ? safeBridge.theme : "Light"
    property bool safeIsMaximized: safeBridge ? safeBridge.isMaximized : false
    property string safeWindowEffect: safeBridge ? safeBridge.windowEffect : "None"
    property real revealProgress: 1
    property color _bgOldColor: safeStyle.surface
    property color _bgNewColor: safeStyle.surface
    color: "transparent"

    property point lastPos: Qt.point(0, 0)
    property string appTitle: Qt.application.displayName && Qt.application.displayName.length > 0
        ? Qt.application.displayName
        : (Qt.application.name && Qt.application.name.length > 0 ? Qt.application.name : "Application")

    children: [
        Item {
            anchors.fill: parent
            visible: safeWindowEffect === "None" || revealProgress < 1
            z: 0
            children: [
                Rectangle {
                    anchors.fill: parent
                    color: _bgOldColor
                },
                Rectangle {
                    anchors.left: parent.left
                    anchors.top: parent.top
                    width: parent.width * revealProgress
                    height: parent.height
                    color: _bgNewColor
                }
            ]
        },
        MouseArea {
            id: dragArea
            anchors.fill: parent
            acceptedButtons: Qt.LeftButton
            onPressed: function(mouse) { lastPos = Qt.point(mouse.x, mouse.y) }
            onPositionChanged: function(mouse) {
                if (mouse.buttons & Qt.LeftButton) {
                    if (safeBridge) {
                        safeBridge.moveWindow(mouse.x - lastPos.x, mouse.y - lastPos.y)
                    }
                }
            }
            onDoubleClicked: {
                if (safeBridge) {
                    safeBridge.requestWindowMaximize()
                }
            }
            z: 1
        },
        Item {
            anchors.fill: parent
            z: 2

            children: [
                Text {
                    id: titleText
                    anchors.left: parent.left
                    anchors.leftMargin: 20
                    anchors.verticalCenter: parent.verticalCenter
                    text: appTitle
                    color: safeStyle.text
                    font.family: "Segoe UI Variable Text"
                    font.pixelSize: 13
                    verticalAlignment: Text.AlignVCenter
                },
                Item {
                    id: closeButton
                    width: 46
                    height: parent.height
                    anchors.right: parent.right
                    anchors.verticalCenter: parent.verticalCenter
                    property bool hovered: false
                    property bool pressed: false

                    children: [
                        Rectangle {
                            anchors.fill: parent
                            color: closeButton.pressed ? safeStyle.pressed : (closeButton.hovered ? safeStyle.hover : "transparent")
                            radius: 4
                        },
                        Image {
                            anchors.centerIn: parent
                            source: "image://FluentIcons/Close/" + safeTheme + "/" + safeStyle.text
                            width: 12
                            height: 12
                            sourceSize: Qt.size(12, 12)
                        },
                        MouseArea {
                            anchors.fill: parent
                            hoverEnabled: true
                            onEntered: closeButton.hovered = true
                            onExited: closeButton.hovered = false
                            onPressed: closeButton.pressed = true
                            onReleased: {
                                closeButton.pressed = false
                                if (safeBridge) {
                                    safeBridge.requestWindowClose()
                                }
                            }
                        }
                    ]
                },
                Item {
                    id: maxButton
                    width: 46
                    height: parent.height
                    anchors.right: closeButton.left
                    anchors.verticalCenter: parent.verticalCenter
                    property bool hovered: false
                    property bool pressed: false

                    children: [
                        Rectangle {
                            anchors.fill: parent
                            color: maxButton.pressed ? safeStyle.pressed : (maxButton.hovered ? safeStyle.hover : "transparent")
                            radius: 4
                        },
                        Image {
                            anchors.centerIn: parent
                            source: "image://FluentIcons/" + (safeIsMaximized ? "fullscreen-exit" : "FullScreen") + "/" + safeTheme + "/" + safeStyle.text
                            width: 12
                            height: 12
                            sourceSize: Qt.size(12, 12)
                        },
                        MouseArea {
                            anchors.fill: parent
                            hoverEnabled: true
                            onEntered: maxButton.hovered = true
                            onExited: maxButton.hovered = false
                            onPressed: maxButton.pressed = true
                            onReleased: {
                                maxButton.pressed = false
                                if (safeBridge) {
                                    safeBridge.requestWindowMaximize()
                                }
                            }
                        }
                    ]
                },
                Item {
                    id: minButton
                    width: 46
                    height: parent.height
                    anchors.right: maxButton.left
                    anchors.verticalCenter: parent.verticalCenter
                    property bool hovered: false
                    property bool pressed: false

                    children: [
                        Rectangle {
                            anchors.fill: parent
                            color: minButton.pressed ? safeStyle.pressed : (minButton.hovered ? safeStyle.hover : "transparent")
                            radius: 4
                        },
                        Image {
                            anchors.centerIn: parent
                            source: "image://FluentIcons/Minimize/" + safeTheme + "/" + safeStyle.text
                            width: 12
                            height: 12
                            sourceSize: Qt.size(12, 12)
                        },
                        MouseArea {
                            anchors.fill: parent
                            hoverEnabled: true
                            onEntered: minButton.hovered = true
                            onExited: minButton.hovered = false
                            onPressed: minButton.pressed = true
                            onReleased: {
                                minButton.pressed = false
                                if (safeBridge) {
                                    safeBridge.requestWindowMinimize()
                                }
                            }
                        }
                    ]
                },
                Item {
                    id: themeButton
                    width: 40
                    height: parent.height
                    anchors.right: minButton.left
                    anchors.verticalCenter: parent.verticalCenter
                    property bool hovered: false
                    property bool pressed: false

                    children: [
                        Rectangle {
                            anchors.fill: parent
                            color: themeButton.pressed ? safeStyle.pressed : (themeButton.hovered ? safeStyle.hover : "transparent")
                            radius: 4
                        },
                        Image {
                            anchors.centerIn: parent
                            source: "image://FluentIcons/bulb/" + safeTheme + "/" + safeStyle.text
                            width: 16
                            height: 16
                            sourceSize: Qt.size(16, 16)
                        },
                        MouseArea {
                            anchors.fill: parent
                            hoverEnabled: true
                            onEntered: themeButton.hovered = true
                            onExited: themeButton.hovered = false
                            onPressed: themeButton.pressed = true
                            onReleased: {
                                themeButton.pressed = false
                                if (safeBridge) {
                                    safeBridge.requestThemeToggle()
                                }
                            }
                        }
                    ]
                }
            ]
        }
    ]

    NumberAnimation on revealProgress {
        id: titleAnim
        duration: safeBridge ? safeBridge.transitionDurationMs : 600
        from: 0
        to: 1
        easing.type: Easing.OutCubic
    }

    onSafeStyleChanged: {
        _bgOldColor = _bgNewColor
        _bgNewColor = safeStyle.surface
        revealProgress = 0
        titleAnim.start()
    }
}
