import QtQuick 2.15
import "."

Rectangle {
    id: root
    
    property string currentTheme: "Light"
    property bool isCompact: width < 100
    property int edgeMargin: isCompact ? 0 : 8
    property var safeBridge: bridge
    property var safeStyle: safeBridge ? safeBridge.style : ({
        background: "#F3F3F3",
        hover: "#22000000",
        pressed: "#33000000",
        text: "#1A1A1A",
        border: "#33000000"
    })
    property string safeTheme: safeBridge ? safeBridge.theme : "Light"
    property string safeWindowEffect: safeBridge ? safeBridge.windowEffect : "None"
    property string currentRoute: safeBridge ? safeBridge.currentRoute : ""

    color: (safeWindowEffect === "Mica" || safeWindowEffect === "Acrylic") ? "transparent" : safeStyle.background
    
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
                            color: hamburger.pressed ? safeStyle.pressed : (hamburger.hovered ? safeStyle.hover : "transparent")
                            radius: 4
                        },
                        Image {
                            anchors.centerIn: parent
                            source: "image://FluentIcons/Menu/" + safeTheme + "/" + (safeTheme === "Dark" ? "#FFFFFF" : "#000000")
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
                                if (safeBridge) {
                                    safeBridge.requestMenuToggle()
                                }
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
                    color: safeStyle.text
                    font.family: "Segoe UI Variable Text"
                    font.pixelSize: 13
                }
            ]
        },
        ListView {
            id: topList
            anchors.top: header.bottom
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.leftMargin: edgeMargin
            anchors.rightMargin: edgeMargin
            height: contentHeight
            clip: true
            interactive: false
            model: navItems
            spacing: 8

            delegate: NavigationItem {
                property string itemPosition: modelData.position ? modelData.position : "scroll"
                text: modelData.text
                iconSymbol: modelData.icon
                isCompact: root.isCompact
                isSelected: modelData.routeKey === root.currentRoute
                visible: itemPosition === "top"
                height: visible ? 40 : 0

                onClicked: {
                    if (safeBridge) {
                        safeBridge.requestMenuClicked(modelData.routeKey)
                    }
                }
            }
        },
        Rectangle {
            id: topSeparator
            anchors.top: topList.bottom
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.leftMargin: edgeMargin
            anchors.rightMargin: edgeMargin
            height: 1
            color: safeStyle.border
            visible: topList.contentHeight > 0
        },

        ListView {
            id: bottomList
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.bottom: parent.bottom
            anchors.leftMargin: edgeMargin
            anchors.rightMargin: edgeMargin
            anchors.bottomMargin: edgeMargin
            height: contentHeight
            clip: true
            interactive: false
            model: navItems
            spacing: 8

            delegate: NavigationItem {
                property string itemPosition: modelData.position ? modelData.position : "scroll"
                text: modelData.text
                iconSymbol: modelData.icon
                isCompact: root.isCompact
                isSelected: modelData.routeKey === root.currentRoute
                visible: itemPosition === "bottom"
                height: visible ? 40 : 0

                onClicked: {
                    if (safeBridge) {
                        safeBridge.requestMenuClicked(modelData.routeKey)
                    }
                }
            }
        },

        ListView {
            id: scrollList
            anchors.top: topSeparator.bottom
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.bottom: bottomList.top
            anchors.leftMargin: edgeMargin
            anchors.rightMargin: edgeMargin
            clip: true
            model: navItems
            spacing: 8

            delegate: NavigationItem {
                property string itemPosition: modelData.position ? modelData.position : "scroll"
                text: modelData.text
                iconSymbol: modelData.icon
                isCompact: root.isCompact
                isSelected: modelData.routeKey === root.currentRoute
                visible: itemPosition === "scroll"
                height: visible ? 40 : 0

                onClicked: {
                    if (safeBridge) {
                        safeBridge.requestMenuClicked(modelData.routeKey)
                    }
                }
            }
        }
    ]
}
