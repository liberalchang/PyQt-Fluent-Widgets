import QtQuick 2.15
import "."

Rectangle {
    id: root
    
    property string currentTheme: "Light"
    property bool isCompact: width < 100
    property int edgeMargin: isCompact ? 0 : 4
    property string currentRoute: bridge ? bridge.currentRoute : ""

    color: bridge.style.background
    
    children: [
        Item {
            id: header
            height: 48
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.leftMargin: edgeMargin
            anchors.rightMargin: edgeMargin
            anchors.topMargin: edgeMargin
            children: [
                Item {
                    id: hamburger
                    width: 40
                    height: 40
                    anchors.left: parent.left
                    anchors.verticalCenter: parent.verticalCenter
                    property bool hovered: false
                    property bool pressed: false

                    children: [
                        Rectangle {
                            anchors.fill: parent
                            color: hamburger.pressed ? bridge.style.pressed : (hamburger.hovered ? bridge.style.hover : "transparent")
                            radius: 4
                        },
                        Image {
                            anchors.centerIn: parent
                            source: "image://FluentIcons/Menu/" + bridge.theme + "/" + (bridge.theme === "Dark" ? "#FFFFFF" : "#000000")
                            width: 16
                            height: 16
                            sourceSize: Qt.size(16, 16)
                        },
                        MouseArea {
                            anchors.fill: parent
                            hoverEnabled: true
                            onEntered: hamburger.hovered = true
                            onExited: hamburger.hovered = false
                            onPressed: hamburger.pressed = true
                            onReleased: {
                                hamburger.pressed = false
                                bridge.requestMenuToggle()
                            }
                        }
                    ]
                },
                Text {
                    visible: false
                    anchors.left: hamburger.right
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.leftMargin: 6
                    text: Qt.application.displayName && Qt.application.displayName.length > 0
                        ? Qt.application.displayName
                        : (Qt.application.name && Qt.application.name.length > 0 ? Qt.application.name : "Application")
                    color: bridge.style.text
                    font.family: "Segoe UI Variable Text"
                    font.pixelSize: 13
                }
            ]
        },
        ListView {
            id: navList
            anchors.top: header.bottom
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.bottom: parent.bottom
            anchors.leftMargin: edgeMargin
            anchors.rightMargin: edgeMargin
            anchors.bottomMargin: edgeMargin
            clip: true
            model: navItems
            spacing: 2

            delegate: NavigationItem {
                text: modelData.text
                iconSymbol: modelData.icon
                isCompact: root.isCompact
                isSelected: modelData.routeKey === root.currentRoute

                onClicked: {
                    bridge.requestMenuClicked(modelData.routeKey)
                }
            }
        }
    ]
}
