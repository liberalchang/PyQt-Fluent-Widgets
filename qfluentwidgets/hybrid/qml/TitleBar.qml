import QtQuick 2.15

Rectangle {
    id: root
    height: 48
    color: bridge.style.surface

    property point lastPos: Qt.point(0, 0)
    property string appTitle: Qt.application.displayName && Qt.application.displayName.length > 0
        ? Qt.application.displayName
        : (Qt.application.name && Qt.application.name.length > 0 ? Qt.application.name : "Application")

    children: [
        MouseArea {
            id: dragArea
            anchors.fill: parent
            acceptedButtons: Qt.LeftButton
            onPressed: lastPos = Qt.point(mouse.x, mouse.y)
            onPositionChanged: {
                if (mouse.buttons & Qt.LeftButton) {
                    bridge.moveWindow(mouse.x - lastPos.x, mouse.y - lastPos.y)
                }
            }
            onDoubleClicked: bridge.requestWindowMaximize()
            z: 0
        },
        Item {
            anchors.fill: parent
            z: 1

            children: [
                Text {
                    id: titleText
                    anchors.left: parent.left
                    anchors.leftMargin: 20
                    anchors.verticalCenter: parent.verticalCenter
                    text: appTitle
                    color: bridge.style.text
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
                            color: closeButton.pressed ? bridge.style.pressed : (closeButton.hovered ? bridge.style.hover : "transparent")
                        },
                        Image {
                            anchors.centerIn: parent
                            source: "image://FluentIcons/Close/" + bridge.theme + "/" + bridge.style.text
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
                                bridge.requestWindowClose()
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
                            color: maxButton.pressed ? bridge.style.pressed : (maxButton.hovered ? bridge.style.hover : "transparent")
                        },
                        Image {
                            anchors.centerIn: parent
                            source: "image://FluentIcons/" + (bridge.isMaximized ? "fullscreen-exit" : "FullScreen") + "/" + bridge.theme + "/" + bridge.style.text
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
                                bridge.requestWindowMaximize()
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
                            color: minButton.pressed ? bridge.style.pressed : (minButton.hovered ? bridge.style.hover : "transparent")
                        },
                        Image {
                            anchors.centerIn: parent
                            source: "image://FluentIcons/Minimize/" + bridge.theme + "/" + bridge.style.text
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
                                bridge.requestWindowMinimize()
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
                            color: themeButton.pressed ? bridge.style.pressed : (themeButton.hovered ? bridge.style.hover : "transparent")
                        },
                        Image {
                            anchors.centerIn: parent
                            source: "image://FluentIcons/bulb/" + bridge.theme + "/" + bridge.style.text
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
                                bridge.requestThemeToggle()
                            }
                        }
                    ]
                }
            ]
        }
    ]
}
