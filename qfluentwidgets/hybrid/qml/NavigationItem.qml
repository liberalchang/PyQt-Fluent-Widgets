import QtQuick 2.15

Item {
    id: control

    property var safeBridge: bridge
    property var safeStyle: safeBridge ? safeBridge.style : ({
        hover: "#22000000",
        pressed: "#33000000",
        text: "#1A1A1A",
        textSecondary: "#666666",
        accent: "#3C7DFF"
    })
    property string safeTheme: safeBridge ? safeBridge.theme : "Light"

    property string iconSymbol: ""
    property bool isCompact: false
    property bool isSelected: false
    property bool hovered: false
    property bool pressed: false
    property alias text: label.text

    signal clicked

    width: parent ? parent.width : 200
    height: 40

    children: [
        Rectangle {
            anchors.fill: parent
            color: control.pressed ? safeStyle.pressed : (control.hovered ? safeStyle.hover : "transparent")
            radius: 4
            children: [
                Rectangle {
                    visible: isSelected
                    width: 3
                    height: 16
                    radius: 1.5
                    color: safeStyle.accent
                    anchors.left: parent.left
                    anchors.leftMargin: 0
                    anchors.verticalCenter: parent.verticalCenter
                }
            ]
        },
        Item {
            id: iconBox
            width: 48
            height: parent.height
            anchors.left: parent.left
            anchors.verticalCenter: parent.verticalCenter
            children: [
                Image {
                    anchors.centerIn: parent
                    source: "image://FluentIcons/" + control.iconSymbol + "/" + safeTheme + "/" + (isSelected ? (safeStyle.accent ? safeStyle.accent : safeStyle.text) : safeStyle.text)
                    width: 20
                    height: 20
                    sourceSize: Qt.size(20, 20)
                    visible: true
                }
            ]
        },
        Text {
            id: label
            visible: !isCompact
            font.family: "Segoe UI Variable Text"
            font.pixelSize: 14
            color: isSelected ? safeStyle.text : safeStyle.textSecondary
            anchors.left: iconBox.right
            anchors.verticalCenter: parent.verticalCenter
            leftPadding: 0
        },
        MouseArea {
            anchors.fill: parent
            hoverEnabled: true
            onEntered: control.hovered = true
            onExited: control.hovered = false
            onPressed: control.pressed = true
            onReleased: {
                control.pressed = false
                control.clicked()
            }
        }
    ]
}
